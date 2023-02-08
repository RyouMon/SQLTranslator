import sys

from fbs_runtime.application_context.PySide6 import ApplicationContext
from PySide6.QtWidgets import QMainWindow
import sqlglot

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('SQLTranslator')

        self.ui.translateButton.clicked.connect(self.translate)

        self.dialects = list(sqlglot.Dialect.classes.keys())
        self.ui.fromComboBox.addItems(self.dialects)
        self.ui.toComboBox.addItems(self.dialects)

    def translate(self):
        text = sqlglot.transpile(
            self.ui.fromEdit.toPlainText(),
            read=self.ui.fromComboBox.currentText(),
            write=self.ui.toComboBox.currentText(),
        )[0]
        self.ui.toEdit.setText(text)


if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    window = MainWindow()
    window.show()
    exit_code = appctxt.app.exec()      # 2. Invoke appctxt.app.exec()
    sys.exit(exit_code)
