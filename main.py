import sys
import subprocess
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSpacerItem,
    QSizePolicy, QHBoxLayout, QFrame
)
from PyQt5.QtGui import QFont, QPixmap, QColor, QPalette, QLinearGradient, QBrush
from PyQt5.QtCore import Qt


class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lara Projects - Menú Principal")
        self.setGeometry(250, 100, 750, 650)
        self.setup_ui()

    def setup_ui(self):
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#ffffff"))
        gradient.setColorAt(1.0, QColor("#f7f8fa"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)
        main_layout.setContentsMargins(0, 0, 0, 20)
        main_layout.setSpacing(10)

        header = QLabel()
        header.setFixedHeight(130)
        header.setAlignment(Qt.AlignCenter)
        try:
            banner = QPixmap("header.png").scaledToWidth(600, Qt.SmoothTransformation)
            header.setPixmap(banner)
        except Exception:
            header.setText("Encabezado no encontrado")
            header.setAlignment(Qt.AlignCenter)
            header.setStyleSheet("color: gray; font-size: 14px;")

        main_layout.addWidget(header)

        center_layout = QVBoxLayout()
        center_layout.setAlignment(Qt.AlignCenter)
        center_layout.setContentsMargins(50, 10, 50, 10)
        center_layout.setSpacing(10)

        subtitle = QLabel("By: Derek Calderón, Adrián Matul & Diego Ovalle")
        subtitle.setFont(QFont("Segoe UI", 12))
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #777777;")
        center_layout.addWidget(subtitle)

        center_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        buttons_info = [
            ("Tablas de Verdad", self.run_proyecto1, "Genera tablas de verdad a partir de expresiones lógicas booleanas."),
            ("Simplificación Booleana", self.run_proyecto2, "Aplica métodos de simplificación de expresiones booleanas."),
            ("REGEX", self.run_proyecto3, "Analiza y prueba expresiones regulares de manera interactiva."),
            ("Dijkstra's Algorithm Visualizer (Web)", self.open_web, "Abre un visualizador web interactivo del algoritmo de Dijkstra.")
        ]

        for text, action, tooltip in buttons_info:
            btn = QPushButton(text)
            btn.setFixedHeight(50)
            btn.setFont(QFont("Segoe UI", 11))
            btn.setCursor(Qt.PointingHandCursor)
            btn.setToolTip(tooltip)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #ffffff;
                    border: 2px solid #e0e0e0;
                    border-radius: 12px;
                    color: #333333;
                    padding: 10px 20px;
                    font-weight: 500;
                    transition: 0.3s;
                }
                QPushButton:hover {
                    background-color: #f3f3f3;
                    border: 2px solid #cfcfcf;
                }
                QPushButton:pressed {
                    background-color: #eaeaea;
                }
            """)
            btn.clicked.connect(action)
            center_layout.addWidget(btn)

        center_layout.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Logo inferior
        logo_layout = QHBoxLayout()
        logo_layout.setAlignment(Qt.AlignCenter)
        try:
            pixmap = QPixmap("logo.png").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            logo_label = QLabel()
            logo_label.setPixmap(pixmap)
            logo_layout.addWidget(logo_label)
        except Exception:
            placeholder = QLabel("Logo no encontrado")
            placeholder.setStyleSheet("color: gray; font-size: 12px;")
            logo_layout.addWidget(placeholder)

        center_layout.addLayout(logo_layout)

        main_layout.addLayout(center_layout)
        self.setLayout(main_layout)

    def run_proyecto1(self):
        subprocess.Popen(["python3", "proyecto1/main.py"])

    def run_proyecto2(self):
        subprocess.Popen(["python3", "proyecto2/main.py"])

    def run_proyecto3(self):
        subprocess.Popen(["python3", "proyecto3/regex_gui.py"])

    def open_web(self):
        webbrowser.open("https://dijkstra-algorithm-visualizer-sigma.vercel.app")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec_())
