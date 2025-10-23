#!/usr/bin/env python3
"""
Lanzador principal para Regular Expression Verifier
Herramienta Profesional de Expresiones Regulares
"""

import sys
import os

def show_menu():
    """Mostrar menú de opciones"""
    print("=" * 70)
    print("Regular Expression Verifier")
    print("=" * 70)
    print("Herramienta Profesional de Expresiones Regulares")
    print()
    print("Seleccione una opción:")
    print()
    print("1. Iniciar Interfaz Gráfica")
    print("2. Mostrar Información del Sistema")
    print("3. Salir")
    print()
    print("=" * 70)

def check_pyqt6():
    """Verificar si PyQt6 está instalado"""
    try:
        from PyQt6.QtWidgets import QApplication
        return True
    except ImportError:
        return False

def run_pyqt6_gui():
    """Ejecutar interfaz gráfica PyQt6"""
    try:
        from regex_gui import main
        print("Iniciando Regular Expression Verifier...")
        print("Cargando interfaz profesional...")
        main()
    except ImportError as e:
        print(f"Error al importar PyQt6: {e}")
        print("Instale PyQt6 con: pip install PyQt6")
        print("O use: pip install -r requirements.txt")
        input("Presione Enter para continuar...")
    except Exception as e:
        print(f"Error inesperado: {e}")
        input("Presione Enter para continuar...")

def show_system_info():
    """Mostrar información del sistema"""
    print("INFORMACIÓN DEL SISTEMA")
    print("=" * 50)
    print(f"Python: {sys.version}")
    print(f"Directorio actual: {os.getcwd()}")
    print(f"Plataforma: {sys.platform}")
    
    # Verificar dependencias
    print("\nDEPENDENCIAS:")
    
    # PyQt6
    if check_pyqt6():
        try:
            from PyQt6.QtCore import QT_VERSION_STR
            print(f"PyQt6: {QT_VERSION_STR}")
        except:
            print("PyQt6: Instalado")
    else:
        print("PyQt6: No instalado")
    
    # Módulo re (siempre disponible)
    print("re: Incluido con Python")
    
    print("\nCARACTERÍSTICAS:")
    print("• Interfaz gráfica moderna con PyQt6")
    print("• Resaltado de sintaxis en tiempo real")
    print("• Resaltado visual de coincidencias con colores")
    print("• Procesamiento asíncrono")
    print("• Diseño profesional y minimalista")
    
    print("\nINSTALACIÓN:")
    print("pip install PyQt6")
    print("O use: pip install -r requirements.txt")
    
    input("\nPresione Enter para continuar...")

def main():
    """Función principal del lanzador"""
    while True:
        show_menu()
        
        try:
            choice = input("Ingrese su opción (1-3): ").strip()
            
            if choice == "1":
                if check_pyqt6():
                    run_pyqt6_gui()
                else:
                    print("PyQt6 no está instalado.")
                    print("Instale con: pip install PyQt6")
                    print("O use: pip install -r requirements.txt")
                    input("Presione Enter para continuar...")
            
            elif choice == "2":
                show_system_info()
            
            elif choice == "3":
                print("Gracias por usar Regular Expression Verifier!")
                print("Hasta la próxima!")
                break
            
            else:
                print("Opción inválida. Por favor seleccione 1-3.")
                input("Presione Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\nHasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    main()