import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtSql


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)
        self.model.setTable('coffee')
        self.model.select()
        self.tableView.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("coffee.sqlite")
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
