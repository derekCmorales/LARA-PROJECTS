#!/usr/bin/env python3
"""
Script de instalación para la Herramienta de Expresiones Regulares
"""

import subprocess
import sys
import os

def check_python_version():
    """Verificar versión de Python"""
    if sys.version_info < (3, 7):
        print("❌ Se requiere Python 3.7 o superior")
        print(f"   Versión actual: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detectado")
    return True

def check_tkinter():
    """Verificar si tkinter está disponible"""
    try:
        import tkinter
        print("✅ Tkinter está disponible (incluido con Python)")
        return True
    except ImportError:
        print("❌ Tkinter no está disponible")
        return False

def install_pyqt6():
    """Instalar PyQt6"""
    try:
        print("📦 Instalando PyQt6...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt6"])
        print("✅ PyQt6 instalado correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar PyQt6: {e}")
        return False

def test_imports():
    """Probar importaciones"""
    print("\n🧪 Probando importaciones...")
    
    # Probar tkinter
    try:
        import tkinter
        print("✅ Tkinter: OK")
    except ImportError:
        print("❌ Tkinter: Error")
    
    # Probar PyQt6
    try:
        from PyQt6.QtWidgets import QApplication
        print("✅ PyQt6: OK")
    except ImportError:
        print("❌ PyQt6: No disponible")
    
    # Probar módulo re
    try:
        import re
        print("✅ Módulo re: OK")
    except ImportError:
        print("❌ Módulo re: Error")

def main():
    """Función principal de instalación"""
    print("=" * 60)
    print("🔧 INSTALADOR - HERRAMIENTA DE EXPRESIONES REGULARES")
    print("=" * 60)
    
    # Verificar Python
    if not check_python_version():
        return
    
    # Verificar tkinter
    if not check_tkinter():
        print("❌ Tkinter es requerido pero no está disponible")
        return
    
    # Preguntar sobre PyQt6
    print("\n¿Desea instalar PyQt6 para la interfaz gráfica avanzada?")
    print("(Tkinter ya está disponible y es suficiente para usar la herramienta)")
    
    while True:
        choice = input("Instalar PyQt6? (s/n): ").strip().lower()
        if choice in ['s', 'si', 'sí', 'y', 'yes']:
            install_pyqt6()
            break
        elif choice in ['n', 'no']:
            print("✅ Continuando sin PyQt6 (usando solo Tkinter)")
            break
        else:
            print("Por favor responda 's' o 'n'")
    
    # Probar importaciones
    test_imports()
    
    print("\n" + "=" * 60)
    print("🎉 INSTALACIÓN COMPLETADA")
    print("=" * 60)
    print("Para usar la herramienta:")
    print("  • Lanzador: python3 launcher.py")
    print("  • Tkinter: python3 regex_tkinter.py")
    print("  • CLI: python3 basic_implementation.py")
    print("  • Demo: python3 demo.py")

if __name__ == "__main__":
    main()
