# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(708, 404)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fromLayout = QHBoxLayout()
        self.fromLayout.setObjectName(u"fromLayout")
        self.fromLabel = QLabel(self.centralwidget)
        self.fromLabel.setObjectName(u"fromLabel")

        self.fromLayout.addWidget(self.fromLabel)

        self.fromComboBox = QComboBox(self.centralwidget)
        self.fromComboBox.setObjectName(u"fromComboBox")

        self.fromLayout.addWidget(self.fromComboBox)


        self.horizontalLayout_4.addLayout(self.fromLayout)

        self.toLayout = QHBoxLayout()
        self.toLayout.setObjectName(u"toLayout")
        self.toLabel = QLabel(self.centralwidget)
        self.toLabel.setObjectName(u"toLabel")

        self.toLayout.addWidget(self.toLabel)

        self.toComboBox = QComboBox(self.centralwidget)
        self.toComboBox.setObjectName(u"toComboBox")

        self.toLayout.addWidget(self.toComboBox)


        self.horizontalLayout_4.addLayout(self.toLayout)


        self.mainLayout.addLayout(self.horizontalLayout_4)

        self.editLayout = QHBoxLayout()
        self.editLayout.setObjectName(u"editLayout")
        self.fromEdit = QTextEdit(self.centralwidget)
        self.fromEdit.setObjectName(u"fromEdit")

        self.editLayout.addWidget(self.fromEdit)

        self.toEdit = QTextEdit(self.centralwidget)
        self.toEdit.setObjectName(u"toEdit")

        self.editLayout.addWidget(self.toEdit)


        self.mainLayout.addLayout(self.editLayout)

        self.translateButton = QPushButton(self.centralwidget)
        self.translateButton.setObjectName(u"translateButton")

        self.mainLayout.addWidget(self.translateButton)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")

        self.mainLayout.addWidget(self.clearButton)


        self.gridLayout.addLayout(self.mainLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 708, 34))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.clearButton.clicked.connect(self.toEdit.clear)
        self.clearButton.clicked.connect(self.fromEdit.clear)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fromLabel.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.toLabel.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.translateButton.setText(QCoreApplication.translate("MainWindow", u"Translate", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
    # retranslateUi
