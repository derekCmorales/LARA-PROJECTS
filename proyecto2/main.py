from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt6.QtGui import QFont
from simplificador import normalizar, validar, aplicar_leyes
import sys


class BooleanSimplifierGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simplificador de Expresiones Booleanas")
        self.setGeometry(200, 200, 800, 600)
        self.setStyleSheet("background-color: #f4f6f9;")

        layout = QVBoxLayout()

        lbl = QLabel("Ingresa la expresión booleana:")
        lbl.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        lbl.setStyleSheet("color: #000000;")
        layout.addWidget(lbl)

        self.entry_expr = QLineEdit()
        self.entry_expr.setFont(QFont("Consolas", 16))
        self.entry_expr.setStyleSheet("""
            QLineEdit {
                border: 2px solid #666666;
                border-radius: 8px;
                padding: 8px;
                background-color: #ffffff;
                color: #000000;
            }
            QLineEdit:focus {
                border: 2px solid #1a73e8;
                background-color: #ffffff;
                color: #000000;
            }
        """)
        layout.addWidget(self.entry_expr)

        btn_layout = QHBoxLayout()

        btn_pasos = QPushButton("Simplificar paso a paso")
        btn_pasos.clicked.connect(self.simplificar_pasos)
        btn_layout.addWidget(btn_pasos)

        btn_final = QPushButton("Resultado final")
        btn_final.clicked.connect(self.resultado_final)
        btn_layout.addWidget(btn_final)

        btn_limpiar = QPushButton("Limpiar")
        btn_limpiar.clicked.connect(self.limpiar)
        btn_layout.addWidget(btn_limpiar)

        for b in (btn_pasos, btn_final, btn_limpiar):
            b.setFont(QFont("Arial", 11, QFont.Weight.Bold))
            b.setStyleSheet("""
                QPushButton {
                    background-color: #1a73e8;
                    color: white;
                    border-radius: 10px;
                    padding: 8px 14px;
                }
                QPushButton:hover {
                    background-color: #1669c1;
                }
                QPushButton:pressed {
                    background-color: #0d47a1;
                }
            """)

        layout.addLayout(btn_layout)

        self.text_output = QTextEdit()
        self.text_output.setFont(QFont("Consolas", 13))
        self.text_output.setReadOnly(True)
        self.text_output.setStyleSheet("""
            QTextEdit {
                border: 2px solid #666666;
                border-radius: 8px;
                padding: 10px;
                background-color: #ffffff;
                color: #000000;
            }
        """)
        layout.addWidget(self.text_output)

        self.setLayout(layout)

    def simplificar_pasos(self):
        expr = self.entry_expr.text()
        expr = normalizar(expr)

        if not validar(expr):
            self.mostrar_error("Expresión inválida. Verifica paréntesis y operadores.")
            return

        pasos, _ = aplicar_leyes(expr)
        self.text_output.clear()

        if pasos:
            self.text_output.append("<b>--- Simplificación Paso a Paso ---</b><br>")
            for antes, ley, despues in pasos:
                self.text_output.append(
                    f"<span style='color:#000000;'>{antes}</span> "
                    f"<span style='color:#1a237e;'>--({ley})--></span> "
                    f"<span style='color:#2e7d32;'>{despues}</span>"
                )
        else:
            self.mostrar_error("No se pudo simplificar la expresión.")

    def resultado_final(self):
        expr = self.entry_expr.text()
        expr = normalizar(expr)

        if not validar(expr):
            self.mostrar_error("Expresión inválida. Verifica paréntesis y operadores.")
            return

        _, final = aplicar_leyes(expr)
        self.text_output.clear()
        self.text_output.append(f"<b>Resultado final simplificado:</b><br><br>"
                                f"<span style='color:#b71c1c; font-size:16px;'>{final}</span>")

    def limpiar(self):
        self.entry_expr.clear()
        self.text_output.clear()

    def mostrar_error(self, mensaje):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error")
        msg.setText(mensaje)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #ffffff;
            }
            QLabel {
                color: #000000;
                font-size: 12pt;
            }
            QPushButton {
                background-color: #1a73e8;
                color: white;
                border-radius: 6px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #1669c1;
            }
        """)
        msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BooleanSimplifierGUI()
    window.show()
    sys.exit(app.exec())
