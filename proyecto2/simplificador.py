# Requiere: pip install sympy
import re
from typing import List, Tuple
from sympy import Symbol, simplify_logic, true, false, And, Or, Not

SYMBOLS = {}

def normalizar(expr: str) -> str:
    if not expr:
        return ""
    s = expr.strip().replace(" ", "").upper()
    out = []
    for i, ch in enumerate(s):
        out.append(ch)
        if i + 1 < len(s):
            a, b = ch, s[i+1]
            if (a.isalpha() or a in "01" or a in "')") and (b.isalpha() or b in "01("):
                out.append('*')
    return "".join(out)

def paren_balanceados(expr: str) -> bool:
    stack = []
    for c in expr:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack: return False
            stack.pop()
    return len(stack) == 0

def validar(expr: str) -> bool:
    return bool(expr) and re.match(r"^[A-Z01\+\*\(\)']+$", expr) and paren_balanceados(expr)

def tokenize(expr: str):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isalpha(): tokens.append(("VAR", c)); i+=1; continue
        if c in "01": tokens.append(("CONST", c)); i+=1; continue
        if c == "'": tokens.append(("PRIME", "'")); i+=1; continue
        if c == "+": tokens.append(("OR", '+')); i+=1; continue
        if c == "*": tokens.append(("AND", '*')); i+=1; continue
        if c == "(": tokens.append(("LP", '(')); i+=1; continue
        if c == ")": tokens.append(("RP", ')')); i+=1; continue
        i += 1
    return tokens

class SympyParser:
    def __init__(self, tokens):
        self.toks = tokens; self.i = 0
    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else None
    def consume(self):
        t = self.peek()
        if t: self.i += 1
        return t
    def parse(self):
        return self.parse_or()
    def parse_or(self):
        left = self.parse_and()
        while self.peek() and self.peek()[0] == 'OR':
            self.consume()
            left = Or(left, self.parse_and())
        return left
    def parse_and(self):
        left = self.parse_not()
        while self.peek() and self.peek()[0] == 'AND':
            self.consume()
            left = And(left, self.parse_not())
        return left
    def parse_not(self):
        node = self.parse_primary()
        while self.peek() and self.peek()[0] == 'PRIME':
            self.consume()
            node = Not(node)
        return node
    def parse_primary(self):
        t = self.peek()
        if not t: return false
        if t[0] == 'VAR':
            self.consume()
            v = t[1]
            if v not in SYMBOLS: SYMBOLS[v] = Symbol(v)
            return SYMBOLS[v]
        if t[0] == 'CONST':
            self.consume()
            return true if t[1] == '1' else false
        if t[0] == 'LP':
            self.consume()
            node = self.parse_or()
            if self.peek() and self.peek()[0]=='RP': self.consume()
            return node
        self.consume()
        return false

def sympy_to_custom(e) -> str:
    if e == true: return "1"
    if e == false: return "0"
    from sympy import And, Or, Not, Symbol
    if isinstance(e, Symbol): return str(e)
    if isinstance(e, Not):
        inner = e.args[0]
        s = sympy_to_custom(inner)
        if isinstance(inner, Symbol) or inner in (true,false): return s + "'"
        return "(" + s + ")'"
    if isinstance(e, And):
        parts = []
        for arg in e.args:
            s = sympy_to_custom(arg)
            if isinstance(arg, Or): s = "(" + s + ")"
            parts.append(s)
        return "*".join(parts)
    if isinstance(e, Or):
        return "+".join(sympy_to_custom(arg) for arg in e.args)
    s = str(e).replace("&","*").replace("|","+").replace("~","'")
    return s

def detectar_ley(antes, despues):
    a_str = sympy_to_custom(antes)
    d_str = sympy_to_custom(despues)
    if a_str == d_str: return None
    # heurísticas
    if ("A" in a_str and "A'" in a_str) and ("1" in d_str or "0" in d_str): return "Complemento"
    if "+" in a_str and "*" in a_str and len(d_str) < len(a_str): return "Distribución / Consenso"
    if len(d_str) < len(a_str) and "*" not in a_str and "+" not in a_str: return "Idempotencia"
    if "1" in d_str or "0" in d_str: return "Anulación/Identidad"
    if len(d_str) < len(a_str): return "Absorción"
    return "Simplificación"

def aplicar_leyes(expr: str) -> Tuple[List[Tuple[str,str,str]], str]:
    pasos: List[Tuple[str,str,str]] = []
    s_norm = normalizar(expr)
    if not validar(s_norm):
        return [], expr

    toks = tokenize(s_norm)
    parser = SympyParser(toks)
    parsed = parser.parse()

    current = parsed
    visited = set()
    while True:
        simplificado = simplify_logic(current)
        if sympy_to_custom(simplificado) in visited:
            break
        visited.add(sympy_to_custom(simplificado))
        ley = detectar_ley(current, simplificado)
        antes = sympy_to_custom(current)
        despues = sympy_to_custom(simplificado)
        if antes != despues:
            pasos.append((antes, ley, despues))
        if simplificado == current:
            break
        current = simplificado

    final_str = sympy_to_custom(current)
    return pasos, final_str


if __name__ == "__main__":
    pruebas = [
        "A + A'B",
        "(A + B)(A' + C)",
        "AB + AC + A'B",
        "(A + B)(B + C)",
        "A'B + AB + A",
        "(A + C)(A' + B')",
        "(AB + A'C)(A + B)",
        "(A + B + C)(A' + C)",
        "(AB)' + (A + B)",
        "(A + B)(A' + B')(B + C)",
    ]
    for e in pruebas:
        pasos, final = aplicar_leyes(e)
        print("\nExpresión:", e)
        print("Resultado final:", final)
        if pasos:
            print("Pasos:")
            for i, (antes, ley, despues) in enumerate(pasos, start=1):
                print(f" {i}. {ley}: {antes} -> {despues}")
        else:
            print(" (No se aplicaron transformaciones explícitas)")
