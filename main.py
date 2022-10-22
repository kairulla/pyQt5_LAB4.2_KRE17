#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.uic import loadUi


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('g.ui', self)

        self.setWindowTitle('Лабораторная 4 _ part 2 _ pyQt5')
        self.setWindowIcon(QtGui.QIcon('_MY_PICTURES/logo.png'))

        self.qPushButtonSolver.clicked.connect(self.qPushButtonSolverOnClick)
        self.qPushButtonClear.clicked.connect(self.qPushButtonClearOnClick)


    def qPushButtonSolverOnClick(self):
        self.qTextEditOutputText.clear()
        text = self.qTextEditSourceText.toPlainText()  # получаем наш текст

        array = re.split(" |\n", text)
        array = sorted(array)
        # array.sort()
        array = set(array)

        sub_array = []
        for i in array:
            if len(i) >= 2:
                if (i[0].lower() == i[-1].lower()):
                    self.qTextEditOutputText.insertPlainText(i)
                self.qTextEditOutputText.insertPlainText("\n")


    def qPushButtonClearOnClick(self):
        self.qTextEditSourceText.clear()
        self.qTextEditOutputText.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
