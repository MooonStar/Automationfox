import ctypes
import sys

from PySide.QtCore import *
from PySide.QtGui import *

import fox_tools
from compiled_ui.dialog_about import Ui_AboutDialog
from compiled_ui.dialog_addnew import Ui_AddDialog
from compiled_ui.dialog_edit import Ui_EditDialog
from compiled_ui.main_autfox import Ui_MainWindow


class AddNewDialog(QDialog, Ui_AddDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


class EditDialog(QDialog, Ui_EditDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon('automationfox32.png'))

        myappid = 'MyOrganization.MyGui.1.0.0'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setupUi(self)

        self.cb_testcases = self.combobox_test_case_id
        self.cb_testcases.addItems(fox_tools.load_json())

        # Variables
        self.data = {}
        self.settings = None
        self.read_settings()
        self.add_testcase = AddNewDialog(parent)
        self.assign_widgets()

        # Declare graphics effect for splash fadeout
        self.effect = QGraphicsOpacityEffect()
        self.effect_menu = QGraphicsOpacityEffect()
        self.pixmap_splash.setGraphicsEffect(self.effect)
        self.menubar.setGraphicsEffect(self.effect_menu)
        QGraphicsOpacityEffect.setOpacity(self.effect, 1)
        QGraphicsOpacityEffect.setOpacity(self.effect_menu, 0)

        # fadeout after 2 seconds
        self.ag = QSequentialAnimationGroup()
        self.ag.addPause(2000)
        self.ag.addAnimation(self.fadeout(self.effect, 2000))
        self.ag.addAnimation(self.fadein(self.effect_menu, 2000))
        self.ag.start()
        self.ag.finished.connect(self.pixmap_splash.deleteLater)

    def assign_widgets(self):
        # Main window bindings
        self.btn_start.clicked.connect(self.print_log)
        self.actionAdd_New_Test_Case.triggered.connect(self.open_add_testcase_dialog)
        self.actionEdit_Existing_Test_Case.triggered.connect(self.open_edit_testcase_dialog)
        self.actionAbout.triggered.connect(self.open_about_dialog)
        self.lineedit_dmr.textChanged.connect(self.on_changed)
        self.lineedit_dms.textChanged.connect(self.on_changed)
        self.toolbtn_save_logs.clicked.connect(self.save_log_2_file)

        print self.cb_testcases.currentText()

        fox_tests = fox_tools.count_tests(self.cb_testcases.currentText())

        if fox_tests:
            total_tests = len(fox_tests)
            self.label_total_testcount_value.setText(str(total_tests))
        else:
            self.label_total_testcount_value.setText('Null')

        url_index = self.cb_testcases.currentIndex()
        url_list = fox_tools.get_item_url()
        self.label_url_value.setText("<a href=\"%s\">"
                                     "<span style=\" text-decoration: underline; color:#f7433a;\">"
                                     "%s</a></span>"
                                     % (url_list[url_index], url_list[url_index]))

        # Add testcase dialog bindings
        self.add_testcase.lineedit_id.textChanged.connect(self.on_changed)

    def print_log(self):
        import random
        new_log = "lala" + str(random.random())
        self.list_logs.addItem(new_log)
        self.save_log_2_file()

    def extract_log(self):
        itemsTextList = [
            str(self.list_logs.item(i).text())
            for i in range(self.list_logs.count())
            ]
        print itemsTextList
        return itemsTextList, self.list_logs.count()

    def save_log_2_file(self):
        filepath = QFileDialog.getSaveFileName(self, "Save log", "", "Fox (*.autfox);;Text (*.txt);;All Files (*)");

        if not filepath[0]:
            return

        filename = filepath[0]

        import unicodedata
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore')
        print filename

        ret = True

        if QFile.exists(filename):
            ret = QMessageBox.question(self, 'Overwrite',
                                       'There already exists a file called %s in the current directory.' % filename,
                                       QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)

        if ret == QMessageBox.Cancel:
            return

        QFile.remove(filename)

        try:
            outfile = open(str(filename), 'wb')
        except:
            QMessageBox.information(self, 'Unable to open file', "There was an error opening '{0}'".format(filename))
            return

        list, count = self.extract_log()
        for x in xrange(0, count):
            outfile.write(list[x])
            outfile.write('\n')

        outfile.close

    def fadein(self, target, duration):
        an = QPropertyAnimation(target, "opacity")
        an.setDuration(duration)
        an.setStartValue(0)
        an.setEndValue(1)
        return an

    def fadeout(self, target, duration):
        an = QPropertyAnimation(target, "opacity")
        an.setDuration(duration)
        an.setStartValue(1)
        an.setEndValue(0)
        return an

    def open_add_testcase_dialog(self):
        result = self.add_testcase.exec_()
        print result == QDialog.Accepted
        if result:
            sender = self.sender()
            fox_tools.add_new_testcase(self.data['lineedit_id'])
            self.cb_testcases.clear()
            self.cb_testcases.addItems(fox_tools.load_json())
        print self.data

    def open_edit_testcase_dialog(self):
        self.dialog = EditDialog()
        self.dialog.show()

    def open_about_dialog(self):
        self.dialog = AboutDialog()
        self.dialog.show()

    def on_changed(self, text):
        sender = self.sender()
        self.data[sender.objectName()] = text

    def write_settings(self):
        # Store and Load QSettings
        # Company: Access, Product: Automationfox
        self.settings = QSettings('Access', 'Automationfox')
        self.settings.setValue('name/dmr', self.lineedit_dmr.text())
        self.settings.setValue('name/dms', self.lineedit_dms.text())

    def read_settings(self):
        self.settings = QSettings('Access', 'Automationfox')
        self.lineedit_dmr.setText(self.settings.value('name/dmr', ''))
        self.lineedit_dms.setText(self.settings.value('name/dms', ''))

    def closeEvent(self, event):
        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Exit Program?',
                                     quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.write_settings()
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    ret = app.exec_()
    sys.exit(ret)
