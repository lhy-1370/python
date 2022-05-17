from PySide6.QtWidgets import QMainWindow, QApplication
from ui import Ui_MainWindow
import sys

# pyside6-uic ui.ui -o ui.py

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())