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
        array1 = []
        for i in array:
            sub_array = []
            if i:
                for j in i:
                    sub_array.append(j.lower())
                array1.append(sub_array)

        # print(array1)

        same_letters = []
        for i in array1:
            if(i[0] == i[-1]):
                same_letters.append(i)
                for j in i:
                    self.qTextEditOutputText.insertPlainText(j)
                self.qTextEditOutputText.insertPlainText(" ")
        # print(same_letters)


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
