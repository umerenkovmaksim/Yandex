import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.show_circles)
        self.flag = False

    def show_circles(self):
        self.coords = random.randint(50, 400), random.randint(100, 430)
        self.size = random.randint(20, 80)
        self.color = random.choice(['red', 'yellow', 'green', 'black', 'blue', 'pink'])
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            self.draw_circle(painter)
            painter.end()
            self.flag = False

    def draw_circle(self, painter):
        painter.setBrush(QColor(self.color))
        painter.drawEllipse(self.coords[0], self.coords[1], self.size, self.size)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
