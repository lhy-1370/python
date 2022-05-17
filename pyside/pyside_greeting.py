import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_greeting import Ui_MainWindow

# pyside6-uic ui_greeting.ui -o ui_greeting.py

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_hi.clicked.connect(self.click)

    def click(self):
        # self.ui.btn_hi.setText("인사했어요")
        # print("클릭되었습니다.")
        mb_hi = QMessageBox()
        mb_hi.setText("안녕하세요")
        mb_hi.exec()

        mb_quiz = QMessageBox()
        mb_quiz.setText("1+1?")
        btn_answer_2 = mb_quiz.addButton("2", QMessageBox.ActionRole)
        btn_answer_3 = mb_quiz.addButton("3", QMessageBox.ActionRole)
        mb_quiz.exec()

        if mb_quiz.clickedButton() == btn_answer_2:
            mb_success = QMessageBox()
            mb_success.setText("정답입니다!")
            mb_success.exec()
        elif mb_quiz.clickedButton() == btn_answer_3:
            mb_fail = QMessageBox()
            mb_fail.setText("오답입니다!")
            mb_fail.exec()

        self.ui.chk_1.setChecked(True)
        self.ui.chk_2.setChecked(True)
        self.ui.chk_3.setChecked(True)

        if self.ui.radio_1.isChecked():
            self.ui.radio_2.setChecked(True)
        elif self.ui.radio_2.isChecked():
            self.ui.radio_1.setChecked(True)
        else:
            self.ui.radio_1.setChecked(True)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())