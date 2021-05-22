import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from VideoInput_Ui import Ui_form_video_input
from VideoProcessing import VideoProcessing

class VideoInput(QWidget):
    back_signal = pyqtSignal()
    video_path_signal = pyqtSignal(str)
    def __init__(self):
        super(VideoInput, self).__init__()
        self.ui = Ui_form_video_input()
        self.ui.setupUi(self)
        self.ui.btn_back.clicked.connect(self.slot_btn_back_clicked)
        self.ui.btn_next.clicked.connect(self.slot_btn_next_clicked)
        self.ui.btn_browse.clicked.connect(self.slot_btn_browse_clicked)
        self.w = VideoProcessing()
        self.video_path_signal[str].connect(self.w.slot_set_video_path)
        self.w.back_signal.connect(self.slot_back)
    def slot_btn_back_clicked(self):
        self.close()
        self.back_signal.emit()
    def slot_btn_next_clicked(self):
        self.video_path_signal.emit(self.video_path)
        self.close()
        self.w.show()
    def slot_btn_browse_clicked(self):
        self.video_path, _ = QFileDialog.getOpenFileName(self, 'Open Video', '', 'Image Files (*.mp4;*.avi)')
        self.ui.le_video_path.setText(self.video_path)
    def slot_back(self):
        self.show()