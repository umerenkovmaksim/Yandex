import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem
from PyQt5 import uic, QtSql


class Writer(QDialog):
    def __init__(self, parent):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        inputs = [self.name, self.greed, self.type, self.description, self.cost, self.volume]
        self.parent = parent
        self.pushButton.clicked.connect(self.add)

    def add(self):
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        try:
            cur.execute(f'''INSERT INTO Coffee(ID, coffee_grade, degree_of_roasting, ground_or_grains, description, cost,
             volume) VALUES ({self.parent.model.rowCount() + 1}, '{self.name.text()}', '{self.greed.text()}', '{self.type.text()}', 
             '{self.description.toPlainText()}', {float(self.cost.text())}, {int(self.volume.text())})''')
            con.commit()
        except ValueError:
            self.parent.statusbar.showMessage('Ошибка ввода данных', 5000)
        self.parent.update_table()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.model = QtSql.QSqlTableModel()
        self.tableView.setModel(self.model)
        self.update_table()
        self.pushButton.clicked.connect(self.write_data)

    def update_table(self):
        self.model.setTable('coffee')
        self.model.select()
        self.tableView.resizeColumnsToContents()

    def write_data(self):
        write = Writer(self)
        write.exec()


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
