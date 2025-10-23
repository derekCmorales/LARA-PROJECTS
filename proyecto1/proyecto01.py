import itertools
import re

def detectar_variables(expresion):
    variables = []
    for char in expresion:
        if char.isalpha() and char not in variables:
            variables.append(char)
    return sorted(variables)

def extraer_subexpresiones(expresion):
    subexpresiones = []
    p = []
    
    for i, char in enumerate(expresion):
        if char == '¬' and i + 1 < len(expresion) and expresion[i + 1].isalpha():
            subexpresion = f"¬{expresion[i + 1]}"
            if subexpresion not in subexpresiones:
                subexpresiones.append(subexpresion)
    
    for i, char in enumerate(expresion):
        if char == '(':
            p.append(i)
        elif char == ')':
            inicio = p.pop()
            subexpresion = expresion[inicio:i + 1]
            if subexpresion not in subexpresiones:
                subexpresiones.append(subexpresion)
    
    return subexpresiones

def reemplazar_operadores(expresion, valores):
    for variable, valor in valores.items():
        # Reemplazar variables completas con sus valores (True o False)
        expresion = re.sub(rf'\b{variable}\b', str(valor), expresion)
    # Reemplazar operadores lógicos con sus equivalentes en Python
    expresion = expresion.replace("∧", "and")
    expresion = expresion.replace("∨", "or")
    # Envolver la negación en paréntesis para evitar problemas de precedencia
    expresion = re.sub(r"¬\((.*?)\)", r"(not (\1))", expresion)  # Negación con paréntesis
    expresion = re.sub(r"¬(\w+)", r"(not \1)", expresion)  # Negación sin paréntesis
    # Envolver la implicación en paréntesis para evitar problemas de precedencia
    expresion = re.sub(r"(\S+)\s*→\s*(\S+)", r"(\1 <= \2)", expresion)
    expresion = expresion.replace("↔", "==")
    expresion = expresion.replace("→", "<=")

    return expresion

def generar_tabla_verdad(expresion):
    variables = detectar_variables(expresion)
    if len(variables) > 10:
        print("Error: La expresión contiene más de 10 variables.")
        return
    combinaciones = list(itertools.product([True, False], repeat=len(variables)))
    subexpresiones = extraer_subexpresiones(expresion)
    encabezado = variables + subexpresiones + ["Resultado"]
    ancho_columna = 15
    print(" | ".join(col.ljust(ancho_columna) for col in encabezado))
    print("-" * (len(encabezado) * (ancho_columna + 3) - 3))
    for combinacion in combinaciones:
        valores = {}
        for i in range(len(variables)):
            valores[variables[i]] = combinacion[i]
        resultados_fila = []
        for variable in variables:
            if valores[variable]:
                resultados_fila.append("V".ljust(ancho_columna))
            else:
                resultados_fila.append("F".ljust(ancho_columna))
        resultados_subexpresiones = {}
        for subexpresion in subexpresiones:
            subexpresion_evaluada = reemplazar_operadores(subexpresion, valores)
            try:
                # Validar que la subexpresión no esté vacía o incompleta
                if not subexpresion_evaluada.strip():
                    raise SyntaxError("Subexpresión vacía o incompleta")
                resultado_subexpresion = eval(subexpresion_evaluada)
            except SyntaxError:
                print(f"Error al evaluar la subexpresión: {subexpresion_evaluada}")
                return
            resultados_subexpresiones[subexpresion] = resultado_subexpresion
            if resultado_subexpresion:
                resultados_fila.append("V".ljust(ancho_columna))
            else:
                resultados_fila.append("F".ljust(ancho_columna))
        expresion_evaluada = reemplazar_operadores(expresion, valores)
        try:
            # Validar que la expresión completa no esté vacía o incompleta
            if not expresion_evaluada.strip():
                raise SyntaxError("Expresión vacía o incompleta")
            resultado_final = eval(expresion_evaluada)
        except SyntaxError:
            print(f"Error al evaluar la expresión: {expresion_evaluada}")
            return
        if resultado_final:
            resultados_fila.append("V".ljust(ancho_columna))
        else:
            resultados_fila.append("F".ljust(ancho_columna))
        print(" | ".join(resultados_fila))

print("Ingresa una expresión lógica")
print("Usa los símbolos: ∧ (AND), ∨ (OR), ¬ (NOT), → (implicación), ↔ (equivalencia)")
expresion = input("Expresión lógica: ")
# Validar que el usuario use los operadores correctos
expresion = expresion.replace("v", "∨")  # Reemplazar 'v' por '∨' si el usuario comete un error
generar_tabla_verdad(expresion)