# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_addnew.ui'
#
# Created: Fri Jul 01 21:44:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(339, 147)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/automationfox32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddDialog.setWindowIcon(icon)
        AddDialog.setStyleSheet("QWidget{\n"
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
        self.btn_create = QtGui.QPushButton(AddDialog)
        self.btn_create.setGeometry(QtCore.QRect(270, 100, 48, 32))
        self.btn_create.setStyleSheet("QPushButton#btn_create{\n"
"background-color:#F48024;\n"
"color: white;\n"
"font: bold 18px;\n"
"padding: 5px 5px\n"
"}\n"
"\n"
"QPushButton#btn_create:hover{\n"
"background-color: #fc994e;\n"
"\n"
"}\n"
"\n"
"QPushButton#btn_create:pressed{\n"
"\n"
"background-color:#bf5b0f;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.btn_create.setObjectName("btn_create")
        self.btn_cancel = QtGui.QPushButton(AddDialog)
        self.btn_cancel.setGeometry(QtCore.QRect(210, 100, 51, 34))
        self.btn_cancel.setStyleSheet("QPushButton#btn_cancel{\n"
"background-color:#444444;\n"
"color: white;\n"
"font: bold 18px;\n"
"padding: 5px 5px;\n"
"border: 1px solid #F48024;\n"
"}\n"
"\n"
"QPushButton#btn_cancel:hover{\n"
"border: 2px solid #fc994e;\n"
"background-color:#666666\n"
"\n"
"}\n"
"\n"
"QPushButton#btn_cancel:pressed{\n"
"\n"
"border: 2px solid #bf5b0f;;\n"
"background-color:#222222\n"
"\n"
"}\n"
"\n"
"")
        self.btn_cancel.setObjectName("btn_cancel")
        self.label_info = QtGui.QLabel(AddDialog)
        self.label_info.setGeometry(QtCore.QRect(90, 20, 165, 22))
        self.label_info.setObjectName("label_info")
        self.lineedit_id = QtGui.QLineEdit(AddDialog)
        self.lineedit_id.setGeometry(QtCore.QRect(20, 60, 300, 28))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineedit_id.sizePolicy().hasHeightForWidth())
        self.lineedit_id.setSizePolicy(sizePolicy)
        self.lineedit_id.setMaximumSize(QtCore.QSize(300, 28))
        self.lineedit_id.setSizeIncrement(QtCore.QSize(1, 1))
        self.lineedit_id.setAutoFillBackground(False)
        self.lineedit_id.setText("")
        self.lineedit_id.setMaxLength(100)
        self.lineedit_id.setFrame(False)
        self.lineedit_id.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineedit_id.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineedit_id.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineedit_id.setObjectName("lineedit_id")

        self.retranslateUi(AddDialog)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL("clicked()"), AddDialog.close)
        QtCore.QObject.connect(self.btn_create, QtCore.SIGNAL("clicked()"), AddDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        AddDialog.setWindowTitle(QtGui.QApplication.translate("AddDialog", "New Test Case", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create.setToolTip(QtGui.QApplication.translate("AddDialog", "<html><head/><body><p>Create this new testcase.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_create.setText(QtGui.QApplication.translate("AddDialog", "Create", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("AddDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_info.setText(QtGui.QApplication.translate("AddDialog", "Enter a new test case name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineedit_id.setPlaceholderText(QtGui.QApplication.translate("AddDialog", "01-TC-1800-VerifyVersion", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
