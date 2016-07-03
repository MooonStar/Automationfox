import ctypes
import sys

from PySide.QtCore import *
from PySide.QtGui import *

import fox_tools
import pytest
from compiled_ui.dialog_about import Ui_AboutDialog
from compiled_ui.dialog_addnew import Ui_AddDialog
from compiled_ui.dialog_edit import Ui_EditDialog
from compiled_ui.main_autfox import Ui_MainWindow

# directory = '/Media\ Format\ Support/'
# file_path = '/home/hamza-c/nflc/src/tests/uitest-appium/UITests/Android/JioShare'
# file_name = ''
directory = ''
file_path = 'C:/Users/Hamza/PycharmProjects/AutFox/'
file_name = ''


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
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MainWindow, cls).__new__(cls)
        return cls._instance

    def __init__(self, parent=None):
        if not self._initialized:
            super(MainWindow, self).__init__(parent)
            # loadUi(os.path.join(SCRIPT_DIRECTORY, 'mainwindow.ui'), self)
            self.setup(parent)
            self._initialized = True

    def setup(self, parent):
        # super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon('automationfox32.png'))

        myappid = 'MyOrganization.MyGui.1.0.0'  # arbitrary string
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        self.setupUi(self)

        self.cb_testcases = self.combobox_test_case_id
        self.cb_testcases.addItems(fox_tools.load_json())

        # Variables
        self.data = {}
        self.settings = None
        self.dialog = {}
        self.status = ['Waiting for test begin', 'Running', 'Passed', 'Failed']
        self.state_color = ['yellow', 'cyan', 'green', 'red']
        self.curr_state = 0
        self.read_settings()
        self.add_testcase = AddNewDialog(parent)
        self.edit_testcase = EditDialog(parent)
        self.assign_widgets()

        # Declare graphics effect for splash fade_out
        self.effect = QGraphicsOpacityEffect()
        self.effect_menu = QGraphicsOpacityEffect()
        self.pixmap_splash.setGraphicsEffect(self.effect)
        self.menubar.setGraphicsEffect(self.effect_menu)
        QGraphicsOpacityEffect.setOpacity(self.effect, 1)
        QGraphicsOpacityEffect.setOpacity(self.effect_menu, 0)

        # fade_out after 2 seconds
        self.ag = QSequentialAnimationGroup()
        self.ag.addPause(200)
        self.ag.addAnimation(self.fade_out(self.effect, 200))
        self.ag.addAnimation(self.fade_in(self.effect_menu, 200))
        self.ag.start()
        self.ag.finished.connect(self.pixmap_splash.deleteLater)

        self.timer = QTimer()  # set up your QTimer
        self.timer.timeout.connect(self.update_test_state)  # connect it to your update function
        self.timer.start(1000)  # set it to timeout in 5000 ms

    def assign_widgets(self):
        # Main window bindings
        self.btn_start.clicked.connect(self.execute_test)
        self.actionAdd_New_Test_Case.triggered.connect(self.open_add_testcase_dialog)
        self.actionEdit_Existing_Test_Case.triggered.connect(self.open_edit_testcase_dialog)
        self.actionAbout.triggered.connect(self.open_about_dialog)
        self.lineedit_dmr.textChanged.connect(self.on_changed)
        self.lineedit_dms.textChanged.connect(self.on_changed)
        self.toolbtn_save_logs.clicked.connect(self.save_log_2_file)

        self.label_status_value.setText(self.status[0])
        self.label_status_value.setStyleSheet("QLabel#label_status_value{ color:yellow}")

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

    def update_test_state(self):
        self.label_status_value.setText(self.status[self.curr_state])
        self.label_status_value.setStyleSheet(
            "QLabel#label_status_value{ color:" + self.state_color[self.curr_state] + "}")

        if self.curr_state != 1:
            self.btn_start.setText('S T A R T  T E S T')

        if self.curr_state == 1:
            self.btn_start.setText('S T O P  T E S T')
        self.timer.start(1000)  # set it to timeout in 5000 ms

    def execute_test(self):
        if self.curr_state == 1:
            self.stop_test()
            return
        try:
            self.curr_state = 1
            file_name = self.cb_testcases.currentText()
            full_path = file_path + directory + file_name + '.py'
            print(full_path)
            pytest.main(['-x', full_path])
        except ValueError:
            pass

    def test_results(self):
        self.curr_state = 2
        QMessageBox.information(self, 'Test Run Finished', 'Test execution is finished.', QMessageBox.Ok)
        #self.stop_test()

    def stop_test(self):
        try:
            file_name = self.cb_testcases.currentText()

            full_path = file_path + directory + file_name + '.py'
            print(full_path)

            self.curr_state = 0
            # pytest.main("-c " + full_path)
        except ValueError:
            pass

    def extract_log(self):
        items_text_list = [
            str(self.list_logs.item(i).text())
            for i in range(self.list_logs.count())
            ]
        print items_text_list
        return items_text_list, self.list_logs.count()

    def save_log_2_file(self):
        file_path = QFileDialog.getSaveFileName(self, "Save log", "",
                                                "Fox(*.autfox);;Text(*.txt);;All Files(*)")

        if not file_path[0]:
            return

        filename = file_path[0]

        import unicodedata
        filename = unicodedata.normalize('NFKD', filename).encode('ascii', 'ignore')
        print filename

        ret = True

        if QFile.exists(filename):
            ret = QMessageBox.question(QMessageBox(), 'Overwrite',
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

        li, count = self.extract_log()
        for x in xrange(0, count):
            outfile.write(li[x])
            outfile.write('\n')

        outfile.close

    @staticmethod
    def fade_in(target, duration):
        an = QPropertyAnimation(target, "opacity")
        an.setDuration(duration)
        an.setStartValue(0)
        an.setEndValue(1)
        return an

    @staticmethod
    def fade_out(target, duration):
        an = QPropertyAnimation(target, "opacity")
        an.setDuration(duration)
        an.setStartValue(1)
        an.setEndValue(0)
        return an

    def open_add_testcase_dialog(self):
        result = self.add_testcase.exec_()
        print result == QDialog.Accepted
        if result:
            if not fox_tools.add_new_testcase(self.data['lineedit_id']):
                QMessageBox.information(self, 'Duplicate Entry', 'Please enter a different name.', QMessageBox.Ok)
                self.open_add_testcase_dialog()
                return

            self.cb_testcases.clear()
            self.cb_testcases.addItems(fox_tools.load_json())
        print self.data

    def open_edit_testcase_dialog(self):
        self.edit_testcase.lineedit_id.setText(self.cb_testcases.currentText())
        old = self.edit_testcase.lineedit_id.text()

        self.edit_testcase.btn_delete.clicked.connect(self.delete_entry)

        self.edit_testcase.lineedit_url.setText(self.label_url_value.text())

        result = self.edit_testcase.exec_()

        print result == QDialog.Accepted
        if result:
            fox_tools.update_entry(old, self.edit_testcase.lineedit_id.text())
            self.cb_testcases.clear()
            self.cb_testcases.addItems(fox_tools.load_json())
        print self.data

    def delete_entry(self):
        if not fox_tools.delete_entry(self.edit_testcase.lineedit_id.text()):
            QMessageBox.information(self, 'Could not delete', 'Entry not found.', QMessageBox.Ok)
            self.open_edit_testcase_dialog()
            return

            # self.edit_testcase.close()

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
