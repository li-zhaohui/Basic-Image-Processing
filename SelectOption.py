import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from SelectOption_Ui import Ui_form_start
from ImageProcessing import ImageProcessing
from VideoInput import VideoInput
class SelectOption(QWidget):
    def __init__(self):
        super(SelectOption, self).__init__()
        self.ui = Ui_form_start()
        self.ui.setupUi(self)
        self.ui.cbb_option.activated[str].connect(self.slot_option_activated)
        self.ui.btn_submit.clicked.connect(self.slot_submit)
        self.option = 'Image'
        self.w_image = ImageProcessing()
        self.w_image.back_signal.connect(self.slot_back)
        self.w_video_input = VideoInput()
        self.w_video_input.back_signal.connect(self.slot_back)
    def slot_option_activated(self, option):
        self.option = option
    def slot_submit(self):
        if self.option == 'Image':
            self.hide()
            self.w_image.show()
        if self.option == 'Video':
            self.hide()
            self.w_video_input.show()
    def slot_back(self):
        self.show()
    def resizeEvent(self, event):
        QWidget.resizeEvent(self,event)
        h = event.size().height()
        width = 0;
        font = self.ui.btn_submit.font()
        if h > 500:
            font.setPointSize(30)
            width = 250;
        else:
            font.setPointSize(15)
            width = 150
        
        
        self.ui.cbb_option.setFixedWidth(width)
        self.ui.btn_submit.setFixedWidth(width)
        
        self.ui.cbb_option.setFont(font)
        self.ui.btn_submit.setFont(font)
        self.ui.label.setFont(font)