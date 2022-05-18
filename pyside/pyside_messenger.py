import sys
import random
import atexit

from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_messenger import Ui_MainWindow
from PySide6.QtCore import QTimer
# from PySide6.QtGui import QStandardItemModel, QStandardItem

# pyside6-uic ui_messenger.ui -o ui_messenger.py

class MainWindow(QMainWindow):
    last_read = 0
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.model = QStandardItemModel()
        # self.ui.list_chat.setModel(self.model)

        self.ui.btn_send.clicked.connect(self.send)
        self.ui.edit_text.returnPressed.connect(self.send)

        nickname = self.random_nickname()
        self.ui.edit_nickname.setText(nickname)

        with open("./server.txt", "a+", encoding="utf-8") as f:
            f.writelines(f"--------{nickname}님이 입장하셨습니다.\n")

        self.listen()

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.listen)
        self.timer.start()

        atexit.register(self.handle_exit)

    def send(self):
        nickname = self.ui.edit_nickname.text()
        text = self.ui.edit_text.text()
        # self.ui.list_chat.addItem(f"{nickname}: {text}")
        # item = QStandardItem(text)
        # self.model.appendRow(item)
        msg = f"{nickname}: {text}\n"

        with open("./server.txt", "a+", encoding="utf-8") as f:
            f.writelines(msg)

        self.ui.edit_text.clear()

        self.listen()

    def handle_exit(self):
        nickname = self.ui.edit_nickname.text()
        with open("./server.txt", "a+", encoding="utf-8") as f:
            f.writelines(f"--------{nickname}님이 퇴장하셨습니다.\n")

    def random_nickname(self):
        nickname = random.choice(["홍길동", "박보검", "한소희"])
        num = random.randint(1, 1000)
        return f"{nickname}{num}"

    def listen(self):
        try:
            with open("./server.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
            lines = [x.strip() for x in lines]
            self.ui.list_chat.addItems(lines[self.last_read:])
            self.last_read = len(lines)
            self.ui.list_chat.scrollToBottom()
        except:
            pass



if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())