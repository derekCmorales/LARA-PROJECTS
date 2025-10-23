import itertools
import re

class ExpressionParser:
    OPERATORS = {
        '∧': ' and ',
        '∨': ' or ',
        '¬': ' not ',
        '→': ' or not ',  # p → q ≡ not p or q
        '↔': ' == '       # p ↔ q ≡ p == q
    }

    def __init__(self, expression):
        self.expression = expression
        self.variables = self.extract_variables()
        self.sub_expressions = []
        self.truth_table = []

    def extract_variables(self):
        # Extraer variables únicas (letras minúsculas)
        variables = sorted(set(re.findall(r'\b[a-z]+\b', self.expression)))
        if len(variables) > 10:
            raise ValueError("Máximo 10 variables permitidas")
        return variables

    def evaluate_expression(self, values):
        # Reemplazar variables por sus valores
        expr = self.expression
        for var in self.variables:
            expr = re.sub(r'\b' + var + r'\b', str(values[var]), expr)
        
        # Reemplazar operadores lógicos
        for op, py_op in self.OPERATORS.items():
            if op == '→':  # Manejar la implicación específicamente
                expr = re.sub(r'(\w+)\s*→\s*(\w+)', r'(not \1 or \2)', expr)
            elif op == '↔':  # Manejar la equivalencia específicamente
                expr = re.sub(r'(\w+)\s*↔\s*(\w+)', r'(\1 == \2)', expr)
            else:
                expr = expr.replace(op, py_op)
        
        # Manejar negaciones correctamente
        expr = expr.replace(" not  not ", " ")  # Doble negación
        expr = expr.replace(" not True", "False")
        expr = expr.replace(" not False", "True")
        
        # Evaluar la expresión
        try:
            expr = f"({expr})"  # Envolver en paréntesis para evitar problemas de precedencia
            return eval(expr)
        except Exception as e:
            raise ValueError(f"Error de evaluación: {str(e)}")

    def generate_truth_table(self):
        n = len(self.variables)
        bool_combinations = list(itertools.product([True, False], repeat=n))
        
        # Identificar subexpresiones
        self.identify_subexpressions()
        
        # Generar tabla
        self.truth_table = []
        for combo in bool_combinations:
            row = {}
            values = dict(zip(self.variables, combo))
            
            # Evaluar todas las subexpresiones
            for expr in self.sub_expressions:
                if expr in self.variables:
                    row[expr] = values[expr]
                else:
                    if expr.startswith('¬') and expr[1:] in self.variables:
                        row[expr] = not values[expr[1:]]
                    else:
                        parser = ExpressionParser(expr)
                        row[expr] = parser.evaluate_expression(values)
            
            self.truth_table.append(row)
        
        return self.truth_table

    def identify_subexpressions(self):
        self.sub_expressions = self.variables.copy()
        
        tokens = re.split(r'([()¬∧∨→↔])', self.expression)
        tokens = [t.strip() for t in tokens if t.strip()]
        
        for i in range(len(tokens)):
            if tokens[i] == '¬' and i+1 < len(tokens) and tokens[i+1] in self.variables:
                neg_expr = f'¬{tokens[i+1]}'
                if neg_expr not in self.sub_expressions:
                    self.sub_expressions.append(neg_expr)
        
        stack = []
        current_expr = ""
        for token in tokens:
            if token == '(':
                stack.append(current_expr)
                current_expr = ""
            elif token == ')':
                if stack:
                    parent_expr = stack.pop()
                    full_expr = f"({current_expr})"
                    if full_expr not in self.sub_expressions:
                        self.sub_expressions.append(full_expr)
                    current_expr = parent_expr + full_expr
                else:
                    current_expr += token
            else:
                current_expr += token
        
        if self.expression not in self.sub_expressions:
            self.sub_expressions.append(self.expression)
        
        self.sub_expressions.sort(key=lambda x: len(x))