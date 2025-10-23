#!/usr/bin/env python3
"""
Demo de Regex Master Pro
Muestra las capacidades de la herramienta con ejemplos predefinidos
"""

import sys
from regex_gui import RegexValidator

def demo_basic_usage():
    """Demo de uso básico"""
    print("🔍 DEMO DE REGEX MASTER PRO")
    print("=" * 60)
    print("Mostrando capacidades básicas de la herramienta...")
    print()
    
    validator = RegexValidator()
    
    # Ejemplo 1: Encontrar números
    print("📊 Ejemplo 1: Encontrar números")
    print("-" * 40)
    regex1 = r"\d+"
    text1 = "Hoy es 15 de marzo de 2024\nEl precio es $299.99\nMi teléfono es 555-1234"
    
    print(f"Regex: {regex1}")
    print(f"Texto: {text1}")
    
    is_valid, error = validator.verify_regex(regex1)
    if is_valid:
        matches, error = validator.find_matches(regex1, text1)
        print(f"✅ Coincidencias: {matches}")
    else:
        print(f"❌ Error: {error}")
    
    print()
    
    # Ejemplo 2: Encontrar palabras con mayúscula
    print("📊 Ejemplo 2: Encontrar palabras con mayúscula")
    print("-" * 40)
    regex2 = r"[A-Z][a-z]+"
    text2 = "Pedro y maria son amigos\nJuan trabaja en la oficina\nAna estudia medicina"
    
    print(f"Regex: {regex2}")
    print(f"Texto: {text2}")
    
    is_valid, error = validator.verify_regex(regex2)
    if is_valid:
        matches, error = validator.find_matches(regex2, text2)
        print(f"✅ Coincidencias: {matches}")
    else:
        print(f"❌ Error: {error}")
    
    print()
    
    # Ejemplo 3: Encontrar emails
    print("📊 Ejemplo 3: Encontrar direcciones de email")
    print("-" * 40)
    regex3 = r"\w+@\w+\.\w+"
    text3 = "Contacto: usuario@ejemplo.com\nTambién: admin@test.org\nY: info@empresa.net"
    
    print(f"Regex: {regex3}")
    print(f"Texto: {text3}")
    
    is_valid, error = validator.verify_regex(regex3)
    if is_valid:
        matches, error = validator.find_matches(regex3, text3)
        print(f"✅ Coincidencias: {matches}")
    else:
        print(f"❌ Error: {error}")
    
    print()

def demo_advanced_features():
    """Demo de características avanzadas"""
    print("🚀 CARACTERÍSTICAS AVANZADAS")
    print("=" * 60)
    
    validator = RegexValidator()
    
    # Ejemplo con alternancia
    print("📊 Alternancia (OR)")
    print("-" * 40)
    regex = r"(perro|gato|pájaro)"
    text = "Tengo un perro y un gato\nTambién un pájaro\nEl perro ladra, el gato maúlla"
    
    print(f"Regex: {regex}")
    print(f"Texto: {text}")
    
    is_valid, error = validator.verify_regex(regex)
    if is_valid:
        matches, error = validator.find_matches(regex, text)
        print(f"✅ Coincidencias: {matches}")
    else:
        print(f"❌ Error: {error}")
    
    print()
    
    # Ejemplo con espacios
    print("📊 Espacios en blanco")
    print("-" * 40)
    regex = r"\s+"
    text = "Hola    mundo\nEste    texto    tiene    espacios"
    
    print(f"Regex: {regex}")
    print(f"Texto: {text}")
    
    is_valid, error = validator.verify_regex(regex)
    if is_valid:
        matches, error = validator.find_matches(regex, text)
        print(f"✅ Coincidencias: {len(matches)} espacios encontrados")
    else:
        print(f"❌ Error: {error}")
    
    print()

def demo_error_handling():
    """Demo de manejo de errores"""
    print("⚠️ MANEJO DE ERRORES")
    print("=" * 60)
    
    validator = RegexValidator()
    
    # Regex inválida
    print("📊 Regex inválida")
    print("-" * 40)
    regex = "(ab"  # Paréntesis sin cerrar
    text = "Texto de prueba"
    
    print(f"Regex: {regex}")
    print(f"Texto: {text}")
    
    is_valid, error = validator.verify_regex(regex)
    if is_valid:
        print("✅ Regex válida (inesperado)")
    else:
        print(f"❌ Error detectado: {error}")
    
    print()

def demo_visual_highlighting():
    """Demo de resaltado visual"""
    print("🎨 RESALTADO VISUAL")
    print("=" * 60)
    print("En la interfaz gráfica, las coincidencias se resaltan con:")
    print("• Fondo amarillo brillante")
    print("• Texto negro en negrita")
    print("• Subrayado simple")
    print("• Colores diferenciados para diferentes elementos")
    print()
    print("Ejemplo visual:")
    print("Texto: 'Hoy es 15 de marzo de 2024'")
    print("Regex: '\\d+'")
    print("Resultado: 'Hoy es [15] de marzo de [2024]'")
    print("         (donde [15] y [2024] aparecerían resaltados)")
    print()

def main():
    """Función principal del demo"""
    print("🔍 REGEX MASTER PRO - DEMOSTRACIÓN")
    print("=" * 80)
    print("Esta demostración muestra las capacidades de la herramienta")
    print("Para la experiencia completa, ejecute: python launcher.py")
    print()
    
    try:
        demo_basic_usage()
        demo_advanced_features()
        demo_error_handling()
        demo_visual_highlighting()
        
        print("🎉 DEMOSTRACIÓN COMPLETADA")
        print("=" * 60)
        print("Para usar la interfaz gráfica completa:")
        print("python launcher.py")
        print()
        print("¡Gracias por probar Regex Master Pro!")
        
    except Exception as e:
        print(f"❌ Error durante la demostración: {e}")
        print("Asegúrese de que PyQt6 esté instalado: pip install PyQt6")

if __name__ == "__main__":
    main()