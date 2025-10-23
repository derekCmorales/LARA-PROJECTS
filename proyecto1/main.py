import sys
from PySide6.QtWidgets import QApplication
from truth_table_view import TruthTableView

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = TruthTableView()
    window.setWindowTitle("Generador de Tablas de Verdad")
    window.resize(1000, 700)
    window.show()
    
    sys.exit(app.exec())