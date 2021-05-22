import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from MainWindow_Ui import Ui_MainWindow
from SelectOption import SelectOption
import numpy as np

if __name__ ==   '__main__':
    app = QApplication(sys.argv)
    w = SelectOption()
    w.show()
    app.exec()