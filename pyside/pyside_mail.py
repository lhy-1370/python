import sys
import random
import atexit
import datetime

from PySide6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PySide6 import QtWidgets
from ui_mail import Ui_MainWindow
from PySide6.QtCore import QTimer

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import os
import pyperclip

# pyside6-uic ui_mail.ui -o ui_mail.py

def find(chrome, css):
    wait = WebDriverWait(chrome, 5)
    return wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

def find_all(chrome, css):
    find(chrome, css)
    return chrome.find_elements_by_css_selector(css)

naver_mails = []
daum_mails = []

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        chrome = webdriver.Chrome(r"C:\Users\LHY\Documents\python\Selenium\chromedriver")
        self.chrome = chrome

        chrome.get("https://mail.naver.com")

        input_id = find(chrome, "input#id")
        input_pw = find(chrome, "input#pw")

        pyperclip.copy("lhy1370")
        input_id.send_keys(Keys.CONTROL, "v")

        pyperclip.copy("wngml11!!Wkd")
        input_pw.send_keys(Keys.CONTROL, "v")

        input_pw.send_keys("\n")

        find(chrome, "li#gnb_my_layer")

        for mail in find_all(chrome, "ol.mailList > li"):
            date = mail.find_element_by_css_selector("li.iDate").text
            now = datetime.datetime.now()
            if len(date) < 6:
                date = f"{now.month}-{now.day} {date}"
            date = f"{now.year}-{date}"
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M")
            site = "네이버"
            sender = mail.find_element_by_css_selector(".mTitle .name a").text
            try:
                mail.find_element_by_css_selector("li.file span.spr:not([title=''])").text
                attached = True
            except:
                attached = False
            title = mail.find_element_by_css_selector("strong.mail_title").text
            link = mail.find_element_by_css_selector("div.subject > a").get_attribute("href")

            naver_mails.append({
                "date": date,
                "site": site,
                "sender": sender,
                "attached": attached,
                "title": title,
                "link": link,
            })

        # table show
        self.ui.table.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        self.ui.table.setRowCount(len(naver_mails))
        for r, m in enumerate(naver_mails):
            self.ui.table.setItem(r, 0, QTableWidgetItem(str(m["date"])))
            self.ui.table.setItem(r, 1, QTableWidgetItem(m["site"]))
            self.ui.table.setItem(r, 2, QTableWidgetItem(m["sender"]))
            self.ui.table.setItem(r, 3, QTableWidgetItem(str(m["attached"])))
            self.ui.table.setItem(r, 4, QTableWidgetItem(m["title"]))

        self.ui.table.cellDoubleClicked.connect(self.open_link)

    def open_link(self, r, c):
        mail = naver_mails[r]
        link = mail["link"]

        self.chrome.get(link)
        content = find(self.chrome, "#readFrame").text

        self.ui.lb_title.setText(mail["title"])
        self.ui.lb_content.setText(content)

if __name__ == "__main__":
    app = QApplication()

    window = MainWindow()
    window.show()

    sys.exit(app.exec())