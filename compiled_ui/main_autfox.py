# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_autfox.ui'
#
# Created: Sat Jul 02 12:22:51 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(540, 539)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/automationfox32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QWidget{\n"
"    /*background-color: #222222;*/\n"
"    background-color:#3E4649;\n"
"    border-width: 8px;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    font-family: \"Agency FB\", Arial, serif;\n"
"    font: bold 14px;\n"
"}\n"
"\n"
"\n"
"QToolTip { \n"
"    color: #ffffff; \n"
"    background-color: #666666;\n"
"    border: 1px solid #F48024;\n"
"    min-height: 1.5em;\n"
"    \n"
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
"}\n"
"\n"
"QComboBox {\n"
"    background-color:#2E2F31;\n"
"    padding: 1px 5px 1px 20px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #fc994e;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    border: 1px solid #F48024;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 30px;\n"
"    border: 0px;\n"
"/*\'background-color:#1EB98F;*/\n"
"\n"
"    /*#\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    /*border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    /*border-bottom-right-radius: 3px; */\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/images/down-arrow.png);\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down:on{\n"
"    background-color:#bf5b0f;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"border-radius: 2px;\n"
"background-color:#F48024;\n"
"selection-background-color:#bf5b0f;\n"
"padding: 5px 20px\n"
"}\n"
"\n"
" QMenuBar {\n"
"            background-color:#3E4649;\n"
" }\n"
"\n"
" QMenuBar::item {\n"
"\n"
"     padding: 1px 10px;\n"
"    background-color:transparent;\n"
"     border-radius: 4px;\n"
" }\n"
"\n"
" QMenuBar::item:selected { /* when selected using mouse or keyboard */\n"
"    /* background: #a8a8a8;*/\n"
"        background-color:#F48024;\n"
" }\n"
"\n"
" QMenuBar::item:pressed {\n"
"       background-color:#bf5b0f;\n"
" }\n"
"\n"
"QMenu{\n"
"\n"
"selection-background-color:#F48024;\n"
"}\n"
"\n"
"QAction{\n"
"selection-background-color:#F48024;\n"
"}\n"
"")
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 471, 471))
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"border-top: 2px solid #F48024;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"left: 5px; /* move to the right by 5px */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #F48024, stop: 0.4 #FF8024, stop: 0.8 #F4802F, stop: 1.0 #666666);\n"
"border: 2px solid #bf5b0f;\n"
"border-bottom-color: #bf5b0a; /* same as the pane color */\n"
"border-top-left-radius: 4px;\n"
"border-top-right-radius: 4px;\n"
"min-width: 3em;\n"
"padding: 2px;\n"
"color:#999999\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background:#fE994e;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"border-color: #9B9B9B;\n"
"border-bottom-color: #F48024; /* same as pane color */\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 2px; /* make non-selected tabs look smaller */\n"
"}\n"
"\n"
"/* IMPORTANT: 8< Add the code above here 8< */ QTabBar::tab:selected { /* expand/overlap to the left and right by 4px */ margin-left: -4px; margin-right: -4px; } QTabBar::tab:first:selected { margin-left: 0; /* the first selected tab has nothing to overlap with on the left */ } QTabBar::tab:last:selected { margin-right: 0; /* the last selected tab has nothing to overlap with on the right */ } QTabBar::tab:only-one { margin: 0; /* if there is only one tab, we don\'t want overlapping margins */ }\n"
"\n"
"QTabBar::tab:selected { font: bold; color: white; }\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_test = QtGui.QWidget()
        self.tab_test.setObjectName("tab_test")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_test)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(self.tab_test)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_test_case_id = QtGui.QLabel(self.groupBox)
        self.label_test_case_id.setGeometry(QtCore.QRect(170, 10, 68, 18))
        self.label_test_case_id.setStyleSheet("")
        self.label_test_case_id.setObjectName("label_test_case_id")
        self.btn_start = QtGui.QPushButton(self.groupBox)
        self.btn_start.setEnabled(True)
        self.btn_start.setGeometry(QtCore.QRect(10, 320, 411, 39))
        self.btn_start.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB,Arial,serif")
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QtCore.Qt.ArrowCursor)
        self.btn_start.setMouseTracking(False)
        self.btn_start.setToolTip("")
        self.btn_start.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_start.setAutoFillBackground(False)
        self.btn_start.setStyleSheet("QPushButton{\n"
"background-color:#F48024;\n"
"color: white;\n"
"font: bold 32px\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #fc994e;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"\n"
"background-color:#bf5b0f;\n"
"\n"
"}\n"
"\n"
"")
        self.btn_start.setIconSize(QtCore.QSize(24, 24))
        self.btn_start.setCheckable(False)
        self.btn_start.setAutoDefault(False)
        self.btn_start.setDefault(False)
        self.btn_start.setFlat(False)
        self.btn_start.setObjectName("btn_start")
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 70, 411, 131))
        self.widget.setObjectName("widget")
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(-1, 10, -1, 5)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_dmr = QtGui.QLabel(self.widget)
        self.label_dmr.setObjectName("label_dmr")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_dmr)
        self.lineedit_dms = QtGui.QLineEdit(self.widget)
        self.lineedit_dms.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineedit_dms.setText("")
        self.lineedit_dms.setMaxLength(100)
        self.lineedit_dms.setFrame(True)
        self.lineedit_dms.setObjectName("lineedit_dms")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineedit_dms)
        self.label_dmr_2 = QtGui.QLabel(self.widget)
        self.label_dmr_2.setObjectName("label_dmr_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_dmr_2)
        self.lineedit_dmr = QtGui.QLineEdit(self.widget)
        self.lineedit_dmr.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineedit_dmr.setText("")
        self.lineedit_dmr.setMaxLength(100)
        self.lineedit_dmr.setObjectName("lineedit_dmr")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineedit_dmr)
        self.combobox_test_case_id = QtGui.QComboBox(self.groupBox)
        self.combobox_test_case_id.setGeometry(QtCore.QRect(10, 40, 411, 22))
        self.combobox_test_case_id.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.combobox_test_case_id.setToolTip("")
        self.combobox_test_case_id.setMaxVisibleItems(8)
        self.combobox_test_case_id.setMaxCount(1000)
        self.combobox_test_case_id.setInsertPolicy(QtGui.QComboBox.InsertAlphabetically)
        self.combobox_test_case_id.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.combobox_test_case_id.setObjectName("combobox_test_case_id")
        self.label_url = QtGui.QLabel(self.groupBox)
        self.label_url.setGeometry(QtCore.QRect(10, 220, 46, 13))
        self.label_url.setObjectName("label_url")
        self.label_total_testcount = QtGui.QLabel(self.groupBox)
        self.label_total_testcount.setGeometry(QtCore.QRect(10, 250, 91, 16))
        self.label_total_testcount.setObjectName("label_total_testcount")
        self.label_url_value = QtGui.QLabel(self.groupBox)
        self.label_url_value.setEnabled(True)
        self.label_url_value.setGeometry(QtCore.QRect(50, 210, 381, 31))
        self.label_url_value.setText("")
        self.label_url_value.setTextFormat(QtCore.Qt.RichText)
        self.label_url_value.setOpenExternalLinks(True)
        self.label_url_value.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_url_value.setObjectName("label_url_value")
        self.label_total_testcount_value = QtGui.QLabel(self.groupBox)
        self.label_total_testcount_value.setGeometry(QtCore.QRect(100, 250, 321, 16))
        self.label_total_testcount_value.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_total_testcount_value.setObjectName("label_total_testcount_value")
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_test, "")
        self.tab_log = QtGui.QWidget()
        self.tab_log.setObjectName("tab_log")
        self.list_logs = QtGui.QListWidget(self.tab_log)
        self.list_logs.setGeometry(QtCore.QRect(0, 0, 471, 401))
        self.list_logs.setStyleSheet("\n"
"\n"
"QScrollBar:vertical{\n"
"border: 2px solid red;\n"
"background:#F48024;\n"
"}\n"
"\n"
"QListWidget{\n"
"background:#444444;\n"
"alternate-background-color:#666666;\n"
"\n"
"}")
        self.list_logs.setFrameShape(QtGui.QFrame.StyledPanel)
        self.list_logs.setFrameShadow(QtGui.QFrame.Sunken)
        self.list_logs.setAlternatingRowColors(True)
        self.list_logs.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.list_logs.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.list_logs.setTextElideMode(QtCore.Qt.ElideRight)
        self.list_logs.setMovement(QtGui.QListView.Static)
        self.list_logs.setFlow(QtGui.QListView.TopToBottom)
        self.list_logs.setProperty("isWrapping", False)
        self.list_logs.setLayoutMode(QtGui.QListView.SinglePass)
        self.list_logs.setViewMode(QtGui.QListView.ListMode)
        self.list_logs.setUniformItemSizes(False)
        self.list_logs.setBatchSize(1000)
        self.list_logs.setSelectionRectVisible(True)
        self.list_logs.setObjectName("list_logs")
        self.toolbtn_save_logs = QtGui.QToolButton(self.tab_log)
        self.toolbtn_save_logs.setGeometry(QtCore.QRect(0, 410, 41, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/images/Generic Orange.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolbtn_save_logs.setIcon(icon1)
        self.toolbtn_save_logs.setIconSize(QtCore.QSize(30, 32))
        self.toolbtn_save_logs.setObjectName("toolbtn_save_logs")
        self.tabWidget.addTab(self.tab_log, "")
        self.line_seperator = QtGui.QFrame(self.centralwidget)
        self.line_seperator.setGeometry(QtCore.QRect(10, 480, 471, 2))
        self.line_seperator.setStyleSheet("background-color:#F48024;\n"
"")
        self.line_seperator.setFrameShape(QtGui.QFrame.HLine)
        self.line_seperator.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_seperator.setObjectName("line_seperator")
        self.label_softwarename_fox = QtGui.QLabel(self.centralwidget)
        self.label_softwarename_fox.setGeometry(QtCore.QRect(470, 450, 20, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB,Arial,serif")
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_softwarename_fox.setFont(font)
        self.label_softwarename_fox.setStyleSheet("background-color:rgba(255,255,255,0);\n"
"color:#F48024;")
        self.label_softwarename_fox.setObjectName("label_softwarename_fox")
        self.label_softwarename_automation = QtGui.QLabel(self.centralwidget)
        self.label_softwarename_automation.setGeometry(QtCore.QRect(410, 450, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB,Arial,serif")
        font.setPointSize(-1)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(True)
        self.label_softwarename_automation.setFont(font)
        self.label_softwarename_automation.setStyleSheet("QLabel#label_softwarename_automation{\n"
"\n"
"background-color:rgba(255,255,255,0);\n"
"font: bold 16px\n"
"}\n"
"\n"
"QLabel#label_softwarename_automation:hover{\n"
"color:white;\n"
"}")
        self.label_softwarename_automation.setObjectName("label_softwarename_automation")
        self.pixmap_logo = QtGui.QLabel(self.centralwidget)
        self.pixmap_logo.setGeometry(QtCore.QRect(370, 440, 41, 40))
        self.pixmap_logo.setText("")
        self.pixmap_logo.setPixmap(QtGui.QPixmap(":/icons/images/automationfox32.png"))
        self.pixmap_logo.setObjectName("pixmap_logo")
        self.pixmap_splash = QtGui.QLabel(self.centralwidget)
        self.pixmap_splash.setGeometry(QtCore.QRect(0, 0, 581, 491))
        self.pixmap_splash.setText("")
        self.pixmap_splash.setPixmap(QtGui.QPixmap(":/icons/images/splash-screen.png"))
        self.pixmap_splash.setObjectName("pixmap_splash")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/images/questions-circular-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon2)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAdd_New_Test_Case = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/images/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_New_Test_Case.setIcon(icon3)
        self.actionAdd_New_Test_Case.setObjectName("actionAdd_New_Test_Case")
        self.actionEdit_Existing_Test_Case = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/images/edit-pencil-symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Existing_Test_Case.setIcon(icon4)
        self.actionEdit_Existing_Test_Case.setObjectName("actionEdit_Existing_Test_Case")
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu_File.addAction(self.actionAdd_New_Test_Case)
        self.menu_File.addAction(self.actionEdit_Existing_Test_Case)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Automationfox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_test_case_id.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Select test case to be automated </p><p><span style=\" font-style:italic;\">or add a new testcase under File&gt;Add New Test Case</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_test_case_id.setText(QtGui.QApplication.translate("MainWindow", "Test Case ID: ", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setText(QtGui.QApplication.translate("MainWindow", "S T A R T   T E S T", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dmr.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Enter your DMR name here. </p><p>Example: </p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Shield </li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Samsung Android Tablet SM-T550</li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dmr.setText(QtGui.QApplication.translate("MainWindow", "DMR:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineedit_dms.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Homegateway_testset1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dmr_2.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Enter your DMS name here. </p><p>Example: </p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Homegateway_Testset_1</li><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Mac DMS</li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_dmr_2.setText(QtGui.QApplication.translate("MainWindow", "DMS:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineedit_dmr.setPlaceholderText(QtGui.QApplication.translate("MainWindow", "Nvdia Shield", None, QtGui.QApplication.UnicodeUTF8))
        self.label_url.setText(QtGui.QApplication.translate("MainWindow", "URL :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_total_testcount.setText(QtGui.QApplication.translate("MainWindow", "Total Test Count:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_total_testcount_value.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.list_logs.setSortingEnabled(False)
        self.toolbtn_save_logs.setToolTip(QtGui.QApplication.translate("MainWindow", "Save logs", None, QtGui.QApplication.UnicodeUTF8))
        self.toolbtn_save_logs.setText(QtGui.QApplication.translate("MainWindow", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_log), QtGui.QApplication.translate("MainWindow", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_softwarename_fox.setText(QtGui.QApplication.translate("MainWindow", "fox", None, QtGui.QApplication.UnicodeUTF8))
        self.label_softwarename_automation.setText(QtGui.QApplication.translate("MainWindow", "Automation", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About..", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_New_Test_Case.setText(QtGui.QApplication.translate("MainWindow", "Add New Test Case..", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Existing_Test_Case.setText(QtGui.QApplication.translate("MainWindow", "Edit Existing Test Case..", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
