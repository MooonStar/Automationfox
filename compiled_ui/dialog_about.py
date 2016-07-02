# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_about.ui'
#
# Created: Fri Jul 01 21:44:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(304, 289)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutDialog.sizePolicy().hasHeightForWidth())
        AboutDialog.setSizePolicy(sizePolicy)
        AboutDialog.setMaximumSize(QtCore.QSize(16777215, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/automationfox32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        AboutDialog.setStyleSheet("QWidget{\n"
"    /*background-color: #222222;*/\n"
"    background-color:#3E4649;\n"
"    border-width: 8px;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-family: \"Agency FB\", Arial, serif;\n"
"    font: bold 14px;\n"
"}\n"
"\n"
"QToolTip { \n"
"    color: #ffffff; \n"
"    background-color: #666666;\n"
"    border: 1px solid #F48024;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-width: 4px;\n"
"    border-radius: 4px;\n"
"    background-color:#2E2F31;\n"
"    padding: 4px 20px\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"     border: 1px solid #F48024;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"     color:#F48024;\n"
"     border: 1px solid #fc994e;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:#CEDDE5\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:#F48024;\n"
"}")
        self.verticalLayoutWidget = QtGui.QWidget(AboutDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 282, 275))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_image = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_image.setStyleSheet("QWidget{\n"
"    /*background-color: #222222;*/\n"
"    background-color:#3E4649;\n"
"    border-width: 8px;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-family: \"Agency FB\", Arial, serif;\n"
"    font: bold 14px;\n"
"}\n"
"\n"
"QToolTip { \n"
"    color: #ffffff; \n"
"    background-color: #666666;\n"
"    border: 1px solid #F48024;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border-width: 4px;\n"
"    border-radius: 4px;\n"
"    background-color:#2E2F31;\n"
"    padding: 4px 20px\n"
"\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"     border: 1px solid #F48024;\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"     color:#F48024;\n"
"     border: 1px solid #fc994e;\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"color:#CEDDE5\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color:#F48024;\n"
"}")
        self.btn_image.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/automationfox-logo-big.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_image.setIcon(icon1)
        self.btn_image.setIconSize(QtCore.QSize(128, 128))
        self.btn_image.setObjectName("btn_image")
        self.verticalLayout.addWidget(self.btn_image)
        self.label_version = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_version.setStyleSheet("font: bold 16px")
        self.label_version.setOpenExternalLinks(True)
        self.label_version.setObjectName("label_version")
        self.verticalLayout.addWidget(self.label_version)
        self.label_author = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_author.setStyleSheet("font: bold 16px")
        self.label_author.setOpenExternalLinks(True)
        self.label_author.setObjectName("label_author")
        self.verticalLayout.addWidget(self.label_author)
        self.label_author_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_author_2.setStyleSheet("font: bold 16px")
        self.label_author_2.setOpenExternalLinks(True)
        self.label_author_2.setObjectName("label_author_2")
        self.verticalLayout.addWidget(self.label_author_2)
        self.label_email = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_email.setStyleSheet("font: bold 16px")
        self.label_email.setOpenExternalLinks(True)
        self.label_email.setObjectName("label_email")
        self.verticalLayout.addWidget(self.label_email)
        self.btn_close = QtGui.QPushButton(self.verticalLayoutWidget)
        self.btn_close.setStyleSheet("QPushButton{\n"
"background-color:#444444;\n"
"color: white;\n"
"font: bold 18px;\n"
"padding: 5px 5px;\n"
"border: 1px solid #F48024;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border: 2px solid #fc994e;\n"
"background-color:#666666\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"border: 2px solid #bf5b0f;;\n"
"background-color:#222222\n"
"\n"
"}\n"
"\n"
"")
        self.btn_close.setObjectName("btn_close")
        self.verticalLayout.addWidget(self.btn_close)

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.btn_close, QtCore.SIGNAL("clicked()"), AboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "About Automationfox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_version.setText(QtGui.QApplication.translate("AboutDialog", "Version: 0.2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_author.setText(QtGui.QApplication.translate("AboutDialog", "Programmed & Designed by Hamza Cavus.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_author_2.setText(QtGui.QApplication.translate("AboutDialog", "31.07.2016", None, QtGui.QApplication.UnicodeUTF8))
        self.label_email.setText(QtGui.QApplication.translate("AboutDialog", "<html><head/><body><p><a href=\"mailto:hamza.cavus90@gmail.com\"><span style=\" text-decoration: underline; color:#f7433a;\">hamza.cavus90@gmail.com</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_close.setText(QtGui.QApplication.translate("AboutDialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
