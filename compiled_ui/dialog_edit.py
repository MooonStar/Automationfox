# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_edit.ui'
#
# Created: Sat Jul 02 21:44:07 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditDialog(object):
    def setupUi(self, EditDialog):
        EditDialog.setObjectName("EditDialog")
        EditDialog.resize(332, 188)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/automationfox32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EditDialog.setWindowIcon(icon)
        EditDialog.setStyleSheet("QWidget{\n"
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
        self.lineedit_id = QtGui.QLineEdit(EditDialog)
        self.lineedit_id.setGeometry(QtCore.QRect(10, 50, 300, 28))
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
        self.lineedit_id.setPlaceholderText("")
        self.lineedit_id.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineedit_id.setObjectName("lineedit_id")
        self.btn_cancel = QtGui.QPushButton(EditDialog)
        self.btn_cancel.setGeometry(QtCore.QRect(200, 150, 51, 34))
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
        self.label_info = QtGui.QLabel(EditDialog)
        self.label_info.setGeometry(QtCore.QRect(100, 20, 115, 22))
        self.label_info.setObjectName("label_info")
        self.btn_apply = QtGui.QPushButton(EditDialog)
        self.btn_apply.setGeometry(QtCore.QRect(260, 150, 48, 32))
        self.btn_apply.setStyleSheet("QPushButton#btn_apply{\n"
"background-color:#F48024;\n"
"color: white;\n"
"font: bold 18px;\n"
"padding: 5px 5px\n"
"}\n"
"\n"
"QPushButton#btn_apply:hover{\n"
"background-color: #fc994e;\n"
"\n"
"}\n"
"\n"
"QPushButton#btn_apply:pressed{\n"
"\n"
"background-color:#bf5b0f;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.btn_apply.setObjectName("btn_apply")
        self.btn_delete = QtGui.QPushButton(EditDialog)
        self.btn_delete.setGeometry(QtCore.QRect(10, 150, 61, 32))
        self.btn_delete.setStyleSheet("QPushButton#btn_delete{\n"
"background-color:red;\n"
"color: white;\n"
"font: bold 18px;\n"
"padding: 5px 5px\n"
"}\n"
"\n"
"QPushButton#btn_delete:hover{\n"
"background-color:#FF2222;\n"
"\n"
"}\n"
"\n"
"QPushButton#btn_delete:pressed{\n"
"\n"
"background-color: darkred;\n"
"\n"
"}")
        self.btn_delete.setObjectName("btn_delete")
        self.label_url = QtGui.QLabel(EditDialog)
        self.label_url.setGeometry(QtCore.QRect(130, 80, 115, 22))
        self.label_url.setObjectName("label_url")
        self.lineedit_url = QtGui.QLineEdit(EditDialog)
        self.lineedit_url.setGeometry(QtCore.QRect(10, 110, 300, 28))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.lineedit_url.sizePolicy().hasHeightForWidth())
        self.lineedit_url.setSizePolicy(sizePolicy)
        self.lineedit_url.setMaximumSize(QtCore.QSize(300, 28))
        self.lineedit_url.setSizeIncrement(QtCore.QSize(1, 1))
        self.lineedit_url.setAutoFillBackground(False)
        self.lineedit_url.setText("")
        self.lineedit_url.setMaxLength(100)
        self.lineedit_url.setFrame(False)
        self.lineedit_url.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineedit_url.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineedit_url.setPlaceholderText("")
        self.lineedit_url.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineedit_url.setObjectName("lineedit_url")

        self.retranslateUi(EditDialog)
        QtCore.QObject.connect(self.btn_cancel, QtCore.SIGNAL("clicked()"), EditDialog.close)
        QtCore.QObject.connect(self.btn_apply, QtCore.SIGNAL("clicked()"), EditDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(EditDialog)



    def retranslateUi(self, EditDialog):
        EditDialog.setWindowTitle(QtGui.QApplication.translate("EditDialog", "Edit Test Case", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setText(QtGui.QApplication.translate("EditDialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_info.setText(QtGui.QApplication.translate("EditDialog", "Edit test case name:", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_apply.setToolTip(QtGui.QApplication.translate("EditDialog", "<html><head/><body><p>Apply changes to the testcase.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_apply.setText(QtGui.QApplication.translate("EditDialog", "Apply", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setToolTip(QtGui.QApplication.translate("EditDialog", "<html><head/><body><p>Permanently delete testcase.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("EditDialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_url.setText(QtGui.QApplication.translate("EditDialog", "Edit url:", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
