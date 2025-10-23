from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QScrollArea,
    QHBoxLayout, QVBoxLayout, QMessageBox, QFileDialog, QFrame,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QSizePolicy
)
from PySide6.QtGui import QFont, QColor, QBrush
import re
import itertools
import json
from logic_exp import ExpressionParser

class TruthTableView(QWidget):
    def __init__(self):
        super().__init__()
        self.parser = None
        self.init_ui()
        self.configurar_estilos()
        self.conectar_eventos()

    def init_ui(self):
        layout_principal = QVBoxLayout(self)
        layout_principal.setContentsMargins(20, 20, 20, 20)
        layout_principal.setSpacing(15)

        panel_entrada = QFrame()
        panel_entrada.setObjectName("panelEntrada")
        layout_entrada = QVBoxLayout(panel_entrada)
        
        lbl_titulo = QLabel("Ingrese expresión lógica:")
        lbl_titulo.setObjectName("lblTitulo")
        
        self.input_expresion = QLineEdit()
        self.input_expresion.setObjectName("inputExpresion")
        self.input_expresion.setPlaceholderText("Ej: (p ∧ q) ∨ ¬r")
        
        layout_operadores = QHBoxLayout()
        operadores = ["¬", "∧", "∨", "→", "↔", "(", ")"]
        for op in operadores:
            btn = QPushButton(op)
            btn.setObjectName("btnOperador")
            btn.setFixedSize(40, 40)
            btn.clicked.connect(lambda _, o=op: self.insertar_operador(o))
            layout_operadores.addWidget(btn)
        
        layout_botones = QHBoxLayout()
        self.btn_generar = QPushButton("Generar Tabla")
        self.btn_generar.setObjectName("btnGenerar")
        self.btn_limpiar = QPushButton("Limpiar")
        self.btn_limpiar.setObjectName("btnLimpiar")
        self.btn_guardar = QPushButton("Guardar")
        self.btn_guardar.setObjectName("btnGuardar")
        
        layout_botones.addWidget(self.btn_generar)
        layout_botones.addWidget(self.btn_limpiar)
        layout_botones.addWidget(self.btn_guardar)
        layout_botones.addStretch()
        
        layout_entrada.addWidget(lbl_titulo)
        layout_entrada.addWidget(self.input_expresion)
        layout_entrada.addLayout(layout_operadores)
        layout_entrada.addLayout(layout_botones)
        
        self.tabla = QTableWidget()
        self.tabla.setObjectName("tablaVerdad")
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  
        self.tabla.horizontalHeader().setDefaultSectionSize(100)  
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn) 
        
        scroll_container = QFrame()
        scroll_layout = QVBoxLayout(scroll_container)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.tabla)
        scroll_layout.addWidget(scroll_area)
        
        layout_principal.addWidget(panel_entrada)
        layout_principal.addWidget(scroll_container, 1)
        
        panel_info = QFrame()
        panel_info.setObjectName("panelInfo")
        layout_info = QHBoxLayout(panel_info)
        
        self.lbl_variables = QLabel("Variables: ")
        self.lbl_combinaciones = QLabel("Combinaciones: 0")
        
        layout_info.addWidget(self.lbl_variables)
        layout_info.addStretch()
        layout_info.addWidget(self.lbl_combinaciones)
        
        layout_principal.addWidget(panel_info)

    def configurar_estilos(self):
        self.setStyleSheet("""
            QWidget {
                font-family: 'Segoe UI', Arial;
                background-color: #1a202c;
                color: #e2e8f0;
            }
            #panelEntrada, #panelInfo {
                background-color: #2d3748;
                border-radius: 12px;
                padding: 15px;
                border: 1px solid #4a5568;
            }
            #lblTitulo {
                font-size: 16px;
                font-weight: bold;
                color: #ffffff;
            }
            #inputExpresion {
                font-size: 18px;
                padding: 12px;
                border: 2px solid #4a5568;
                border-radius: 8px;
                font-family: 'Consolas', monospace;
                background-color: #1a202c;
                color: #e2e8f0;
            }
            #inputExpresion:focus {
                border-color: #63b3ed;
            }
            #btnOperador {
                font-size: 18px;
                font-weight: bold;
                background-color: #4a5568;
                border-radius: 8px;
                color: #e2e8f0;
            }
            #btnOperador:hover {
                background-color: #718096;
            }
            #btnGenerar, #btnGuardar {
                background-color: #38a169;
                color: white;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 8px;
            }
            #btnGenerar:hover, #btnGuardar:hover {
                background-color: #2f855a;
            }
            #btnLimpiar {
                background-color: #e53e3e;
                color: white;
                font-weight: bold;
                padding: 10px 20px;
                border-radius: 8px;
            }
            #btnLimpiar:hover {
                background-color: #c53030;
            }
            #tablaVerdad {
                background-color: #1a202c;
                border-radius: 12px;
                gridline-color: #4a5568;
                font-size: 14px;
                color: #e2e8f0;
            }
            QHeaderView::section {
                background-color: #2d3748;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
            }
            QTableWidget::item {
                padding: 12px;
                text-align: center;
                color: #e2e8f0;
                border: 1px solid #4a5568;
            }
            QTableWidget {
                gridline-color: #4a5568;
            }
            QScrollArea {
                border: none;
            }
        """)

    def conectar_eventos(self):
        self.btn_generar.clicked.connect(self.generar_tabla)
        self.btn_limpiar.clicked.connect(self.limpiar_tabla)
        self.btn_guardar.clicked.connect(self.guardar_tabla)

    def insertar_operador(self, operador):
        texto_actual = self.input_expresion.text()
        cursor_pos = self.input_expresion.cursorPosition()
        nuevo_texto = texto_actual[:cursor_pos] + operador + texto_actual[cursor_pos:]
        self.input_expresion.setText(nuevo_texto)
        self.input_expresion.setCursorPosition(cursor_pos + len(operador))

    def generar_tabla(self):
        expresion = self.input_expresion.text().strip()
        if not expresion:
            self.mostrar_error("Expresión Vacía", "Ingrese una expresión lógica válida")
            return
        
        try:
            self.parser = ExpressionParser(expresion)
            self.parser.generate_truth_table()
            self.mostrar_tabla()
            self.actualizar_informacion()
        except Exception as e:
            self.mostrar_error("Error de Expresión", str(e))

    def mostrar_tabla(self):
        self.tabla.clear()
        
        headers = self.parser.sub_expressions
        self.tabla.setColumnCount(len(headers))
        self.tabla.setRowCount(len(self.parser.truth_table))
        self.tabla.setHorizontalHeaderLabels(headers)
        
        for row_idx, row_data in enumerate(self.parser.truth_table):
            for col_idx, header in enumerate(headers):
                valor = row_data[header]
                item = QTableWidgetItem("V" if valor else "F")
                item.setTextAlignment(Qt.AlignCenter)
                
                if valor:
                    item.setBackground(QBrush(QColor(56, 161, 105)))  
                else:
                    item.setBackground(QBrush(QColor(229, 62, 62)))  
                
                if header == self.parser.expression:
                    item.setBackground(QBrush(QColor(245, 158, 11)))  
                
                self.tabla.setItem(row_idx, col_idx, item)
        
        for i in range(len(self.parser.truth_table)):
            self.tabla.setRowHeight(i, 40)
        
        if len(headers) > 5:
            for i in range(len(headers)):
                self.tabla.setColumnWidth(i, 100)

    def actualizar_informacion(self):
        variables = ", ".join(self.parser.variables)
        combinaciones = len(self.parser.truth_table)
        self.lbl_variables.setText(f"Variables: {variables}")
        self.lbl_combinaciones.setText(f"Combinaciones: {combinaciones}")

    def limpiar_tabla(self):
        self.input_expresion.clear()
        self.tabla.setRowCount(0)
        self.tabla.setColumnCount(0)
        self.lbl_variables.setText("Variables: ")
        self.lbl_combinaciones.setText("Combinaciones: 0")

    def guardar_tabla(self):
        if not self.parser or not self.parser.truth_table:
            self.mostrar_error("Datos Insuficientes", "Genere una tabla primero")
            return
        
        opciones = "CSV (*.csv);;JSON (*.json)"
        filename, selected_filter = QFileDialog.getSaveFileName(
            self, "Guardar Tabla de Verdad", "", opciones)
        
        if filename:
            try:
                if selected_filter == "CSV (*.csv)":
                    if not filename.endswith('.csv'):
                        filename += '.csv'
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(self.parser.to_csv())
                else:
                    if not filename.endswith('.json'):
                        filename += '.json'
                    with open(filename, 'w', encoding='utf-8') as f:
                        json.dump(self.parser.to_dict(), f, indent=4)
                
                self.mostrar_mensaje("Éxito", f"Tabla guardada en:\n{filename}")
            except Exception as e:
                self.mostrar_error("Error al Guardar", str(e))

    def mostrar_mensaje(self, titulo, mensaje):
        QMessageBox.information(self,
                                titulo, mensaje)

    def mostrar_error(self, titulo, mensaje):
        QMessageBox.critical(self, titulo, mensaje)