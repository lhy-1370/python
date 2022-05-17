# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_greeting.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btn_hi = QPushButton(self.centralwidget)
        self.btn_hi.setObjectName(u"btn_hi")
        self.btn_hi.setGeometry(QRect(370, 280, 93, 28))
        self.radio_1 = QRadioButton(self.centralwidget)
        self.radio_1.setObjectName(u"radio_1")
        self.radio_1.setGeometry(QRect(250, 210, 108, 19))
        self.radio_2 = QRadioButton(self.centralwidget)
        self.radio_2.setObjectName(u"radio_2")
        self.radio_2.setGeometry(QRect(440, 210, 108, 19))
        self.chk_1 = QCheckBox(self.centralwidget)
        self.chk_1.setObjectName(u"chk_1")
        self.chk_1.setGeometry(QRect(200, 350, 96, 19))
        self.chk_2 = QCheckBox(self.centralwidget)
        self.chk_2.setObjectName(u"chk_2")
        self.chk_2.setGeometry(QRect(370, 350, 96, 19))
        self.chk_3 = QCheckBox(self.centralwidget)
        self.chk_3.setObjectName(u"chk_3")
        self.chk_3.setGeometry(QRect(520, 350, 96, 19))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_hi.setText(QCoreApplication.translate("MainWindow", u"\uc778\uc0ac\ud558\uae30", None))
        self.radio_1.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.radio_2.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.chk_1.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.chk_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.chk_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

