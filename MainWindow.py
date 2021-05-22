import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from MainWindow_Ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Image Processing")
        self.ui.cbb_option.activated[str].connect(self.slot_option_activated)
        self.ui.btn_open.clicked.connect(self.slot_btn_open_clicked)
        self.ui.btn_start_process.clicked.connect(self.slot_btn_start_process_clicked)
        self.ui.btn_save.clicked.connect(self.slot_btn_save_clicked)
        self.ui.cb_resize.toggled.connect(self.slot_cb_resize_toggled)
        self.ui.cb_filters.toggled.connect(self.slot_cb_filters_toggled)
        self.ui.cb_edges.toggled.connect(self.slot_cb_edges_toggled)
        self.ui.cb_thresholding.toggled.connect(self.slot_cb_thresholding_toggled)
        self.ui.cb_segmentation.toggled.connect(self.slot_cb_segmentation_toggled)
        self.ui.cb_transformation.toggled.connect(self.slot_cb_transformation_toggled)
        self.option = 'Image'
        self.update_actions()
    def update_actions(self):
        if self.ui.le_file_path.text() == '':
            self.ui.cb_cvt_color.setDisabled(True)
            self.ui.cb_resize.setDisabled(True)
            self.ui.cb_filters.setDisabled(True)
            self.ui.cb_edges.setDisabled(True)
            self.ui.cb_thresholding.setDisabled(True)
            self.ui.cb_segmentation.setDisabled(True)
            self.ui.cb_transformation.setDisabled(True)
            self.ui.frame_resize.setDisabled(True)
            self.ui.frame_filters.setDisabled(True)
            self.ui.frame_edges.setDisabled(True)
            self.ui.frame_thresholding.setDisabled(True)
            self.ui.frame_segmentation.setDisabled(True)
            self.ui.frame_transformation.setDisabled(True)
            self.ui.btn_start_process.setDisabled(True)
            self.ui.btn_save.setDisabled(True)
        else:
            self.ui.cb_cvt_color.setEnabled(True)
            self.ui.cb_resize.setEnabled(True)
            self.ui.cb_filters.setEnabled(True)
            self.ui.cb_edges.setEnabled(True)
            self.ui.cb_thresholding.setEnabled(True)
            self.ui.btn_start_process.setEnabled(True)
            self.ui.btn_save.setEnabled(True)
            if self.option == 'Video':
                self.ui.cb_segmentation.setEnabled(True)
                self.ui.cb_transformation.setEnabled(True)
            else:
                self.ui.cb_segmentation.setDisabled(True)
                self.ui.cb_transformation.setDisabled(True)
    def image_process(self):
        if self.ui.cb_cvt_color.checkState() == Qt.Checked:
            self.dest_img = cv2.cvtColor(self.src_img, cv2.COLOR_BGR2GRAY)
        else:
            self.dest_img = self.src_img.copy()
        if self.ui.cb_resize.checkState() == Qt.Checked:
            dsize = (int(self.ui.le_width.text()), int(self.ui.le_height.text()))
            # resize image
            self.dest_img = cv2.resize(self.dest_img, dsize)
        if self.ui.cb_filters.checkState() == Qt.Checked:
            if self.ui.rb_mean.isChecked() == True:
                self.dest_img = cv2.blur(self.dest_img,(9,9))
            if self.ui.rb_gaussian.isChecked() == True:
                self.dest_img = cv2.GaussianBlur(self.dest_img,(5,5), 0)
            if self.ui.rb_median.isChecked() == True:
                self.dest_img = cv2.medianBlur(self.dest_img,5)
            if self.ui.rb_bilateral.isChecked() == True:
                self.dest_img = cv2.bilateralFilter(self.dest_img, 15, 75, 75)
            if self.ui.rb_averaging.isChecked() == True:
                self.dest_img = cv2.blur(self.dest_img,(9,9))
        if self.ui.cb_edges.checkState() == Qt.Checked:
            if self.ui.rb_canny.isChecked() == True:
                self.dest_img = cv2.Canny(self.dest_img, 30, 80)
            if self.ui.rb_sobel.isChecked() == True:
                self.dest_img = cv2.Sobel(self.dest_img,cv2.CV_64F,1,1,ksize=5)
            if self.ui.rb_prewitt.isChecked() == True:
                kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
                kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
                self.dest_img = cv2.filter2D(self.dest_img, -1, kernelx)
                self.dest_img = cv2.filter2D(self.dest_img, -1, kernely)
            if self.ui.rb_laplace.isChecked() == True:
                self.dest_img = cv2.Laplacian(self.dest_img,cv2.CV_64F)
        if self.ui.cb_thresholding.checkState() == Qt.Checked:
            if self.ui.rb_simple.isChecked() == True:
                ret, self.dest_img = cv2.threshold(self.dest_img,10,255,cv2.THRESH_BINARY)
            if self.ui.rb_adaptive.isChecked() == True:
                self.dest_img = cv2.adaptiveThreshold(self.dest_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            if self.ui.rb_otsu.isChecked() == True:
                ret, self.dest_img= cv2.threshold(self.dest_img,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return self.dest_img
    def video_process(self):
        self.fps = int(self.cap.get(5))
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
        fgbg = cv2.createBackgroundSubtractorMOG2()
        while(True):
            ret, self.src_img = self.cap.read()
            if ret == False:
                break
            self.dest_img = self.image_process()
            if self.ui.cb_segmentation.checkState() == Qt.Checked:
                if self.ui.rb_foreground.isChecked() == True:
                    self.dest_img = fgbg.apply(self.dest_img)
                    self.dest_img = cv2.morphologyEx(self.dest_img, cv2.MORPH_OPEN, kernel)
                if self.ui.rb_background.isChecked() == True:
                    self.dest_img = fgbg.apply(self.dest_img)
                    self.dest_img = cv2.morphologyEx(self.dest_img, cv2.MORPH_OPEN, kernel)
            cv2.imshow('video',self.dest_img)
            if cv2.waitKey(self.fps) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()
    def slot_option_activated(self, text):
        self.option = text
        self.ui.le_file_path.setText('')
        self.update_actions()
    def slot_btn_open_clicked(self):
        if self.option == 'Image':
            self.img_path, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.jpg;*.jpeg;*.png)')
            self.ui.le_file_path.setText(self.img_path)
            self.update_actions()
        elif self.option == 'Video':
            self.video_path, _ = QFileDialog.getOpenFileName(self, 'Open Video', '', 'Image Files (*.mp4;*.avi)')
            self.ui.le_file_path.setText(self.video_path)
            self.update_actions()
    def slot_btn_start_process_clicked(self):
        if self.option == 'Image':
            self.src_img = cv2.imread(self.ui.le_file_path.text(), cv2.IMREAD_COLOR)
            self.dest_img = self.image_process()
            cv2.imshow('',self.dest_img)
        if self.option == 'Video':
            self.cap = cv2.VideoCapture(self.video_path)
            self.video_process()
    def slot_btn_save_clicked(self):
        if self.option == 'Image':
            self.save_img_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "output.jpg", "Image Files (*.jpg;*.jpeg;*.png)")
            self.dest_img = self.image_process()
            cv2.imwrite(self.save_img_path, self.dest_img)
        if self.option == 'Video':
            self.save_video_path, _ = QFileDialog.getSaveFileName(self, "Save Video", "output.avi", "Image Files (*.avi;*.mp4)")
            self.cap = cv2.VideoCapture(self.video_path)
            w = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH);
            h = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 
            fps = int(self.cap.get(5))
            fourcc = cv2.VideoWriter_fourcc(*'DIVX')
            out = cv2.VideoWriter(self.save_video_path, fourcc, 10, (int(w),int(h)))
            while(True):
                ret, self.src_img = self.cap.read()
                if ret == False:
                    break
                self.dest_img = self.image_process()
                if self.ui.cb_segmentation.checkState() == Qt.Checked:
                    if self.ui.rb_foreground.isChecked() == True:
                        self.dest_img = fgbg.apply(self.dest_img)
                        self.dest_img = cv2.morphologyEx(self.dest_img, cv2.MORPH_OPEN, kernel)
                    if self.ui.rb_background.isChecked() == True:
                        self.dest_img = fgbg.apply(self.dest_img)
                        self.dest_img = cv2.morphologyEx(self.dest_img, cv2.MORPH_OPEN, kernel)
                cv2.imshow('video',self.dest_img)
                out.write(self.dest_img)
                if cv2.waitKey(fps) & 0xFF == ord('q'):
                    break
            self.cap.release()
            cv2.destroyAllWindows()
    def slot_cb_resize_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_resize.setEnabled(True)
        else:
            self.ui.frame_resize.setDisabled(True)
    def slot_cb_filters_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_filters.setEnabled(True)
        else:
            self.ui.frame_filters.setDisabled(True)
    def slot_cb_edges_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_edges.setEnabled(True)
        else:
            self.ui.frame_edges.setDisabled(True)
    def slot_cb_thresholding_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_thresholding.setEnabled(True)
        else:
            self.ui.frame_thresholding.setDisabled(True)
    def slot_cb_segmentation_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_segmentation.setEnabled(True)
        else:
            self.ui.frame_segmentation.setDisabled(True)
    def slot_cb_transformation_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_transformation.setEnabled(True)
        else:
            self.ui.frame_transformation.setDisabled(True)