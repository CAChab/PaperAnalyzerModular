import sys
from PyQt6.QtWidgets import QApplication
from pdf_analyzer import initialize_app

def main():
    app = QApplication(sys.argv)
    window = initialize_app()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
