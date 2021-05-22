import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
import operator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from ImageProcessing_Ui import Ui_form_image_processing

class ImageProcessing(QWidget):
    back_signal = pyqtSignal()
    def __init__(self):
        super(ImageProcessing, self).__init__()
        self.ui = Ui_form_image_processing()
        self.ui.setupUi(self)
        self.ui.btn_back.clicked.connect(self.slot_btn_back_clicked)
        self.ui.btn_preview.clicked.connect(self.slot_btn_preview_clicked)
        self.ui.btn_save.clicked.connect(self.slot_btn_save_clicked)
        self.ui.btn_browse.clicked.connect(self.slot_btn_browse_clicked)
        self.ui.cb_cvt_color.toggled.connect(self.slot_cb_cvt_color_toggled)
        self.ui.cb_resize.toggled.connect(self.slot_cb_resize_toggled)
        self.ui.cb_filters.toggled.connect(self.slot_cb_filters_toggled)
        self.ui.cb_edges.toggled.connect(self.slot_cb_edges_toggled)
        self.ui.cb_thresholding.toggled.connect(self.slot_cb_thresholding_toggled)
        self.ui.cb_transformation.toggled.connect(self.slot_cb_transformation_toggled)
        self.ui.cb_translation.toggled.connect(self.slot_cb_translation_toggled)
        self.ui.cb_rotation.toggled.connect(self.slot_cb_rotation_toggled)
        self.ui.cb_perspective.toggled.connect(self.slot_cb_perspective_toggled)
        self.update_actions()
    def slot_btn_back_clicked(self):
        self.close()
        self.back_signal.emit()
    def update_actions(self):
        if self.ui.le_file_path.text() == '':
            self.ui.cb_cvt_color.setDisabled(True)
            self.ui.cb_resize.setDisabled(True)
            self.ui.cb_filters.setDisabled(True)
            self.ui.cb_edges.setDisabled(True)
            self.ui.cb_thresholding.setDisabled(True)
            self.ui.cb_transformation.setDisabled(True)
            self.ui.frame_cvt_color.setDisabled(True)
            self.ui.frame_resize.setDisabled(True)
            self.ui.frame_filters.setDisabled(True)
            self.ui.frame_edges.setDisabled(True)
            self.ui.frame_thresholding.setDisabled(True)
            self.ui.frame_transformation.setDisabled(True)
            self.ui.btn_preview.setDisabled(True)
            self.ui.btn_save.setDisabled(True)
            self.ui.cb_transformation.setDisabled(True)
        else:
            self.ui.cb_cvt_color.setEnabled(True)
            self.ui.cb_resize.setEnabled(True)
            self.ui.cb_filters.setEnabled(True)
            self.ui.cb_edges.setEnabled(True)
            self.ui.cb_thresholding.setEnabled(True)
            self.ui.btn_save.setEnabled(True)
            self.ui.btn_preview.setEnabled(True)
            self.ui.cb_transformation.setEnabled(True)
    def image_process(self):
        if self.ui.cb_cvt_color.checkState() == Qt.Checked:
            if self.ui.rb_gray.isChecked() == True:
                self.dest_img = cv2.cvtColor(self.src_img, cv2.COLOR_BGR2GRAY)
            if self.ui.rb_color.isChecked() == True:
                self.dest_img = self.src_img.copy()
        else:
            self.dest_img = self.src_img.copy()
        if self.ui.cb_resize.checkState() == Qt.Checked:
            dsize = (int(self.ui.le_width.text()), int(self.ui.le_height.text()))
            # resize image
            self.dest_img = cv2.resize(self.dest_img, dsize)
        if self.ui.cb_filters.checkState() == Qt.Checked:
            if self.ui.cb_mean.checkState() == Qt.Checked:
                self.dest_img = cv2.blur(self.dest_img,(9,9))
            if self.ui.cb_gaussian.checkState() == Qt.Checked:
                self.dest_img = cv2.GaussianBlur(self.dest_img,(5,5), 0)
            if self.ui.cb_median.checkState() == Qt.Checked:
                self.dest_img = cv2.medianBlur(self.dest_img,5)
            if self.ui.cb_bilateral.checkState() == Qt.Checked:
                self.dest_img = cv2.bilateralFilter(self.dest_img, 15, 75, 75)
            if self.ui.cb_averaging.checkState() == Qt.Checked:
                self.dest_img = cv2.blur(self.dest_img,(9,9))
        if self.ui.cb_edges.checkState() == Qt.Checked:
            if self.ui.rb_canny.isChecked() == True:
                self.dest_img = cv2.Canny(self.dest_img, 30, 80)
            if self.ui.rb_sobel.isChecked() == True:
                self.dest_img = cv2.Sobel(self.dest_img,cv2.CV_64F,1,1,ksize=5)
                self.dest_img = np.absolute(self.dest_img)
                self.dest_img = np.uint8(255 * self.dest_img / np.max(self.dest_img))
            if self.ui.rb_prewitt.isChecked() == True:
                kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
                kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
                self.dest_img = cv2.filter2D(self.dest_img, -1, kernelx)
                self.dest_img = cv2.filter2D(self.dest_img, -1, kernely)
                
            if self.ui.rb_laplace.isChecked() == True:
                self.dest_img = cv2.Laplacian(self.dest_img,cv2.CV_64F)
                
                self.dest_img = np.absolute(self.dest_img)
                self.dest_img = np.uint8(255 * self.dest_img / np.max(self.dest_img))

        if self.ui.cb_thresholding.checkState() == Qt.Checked:
            if len(self.dest_img.shape) == 3:
                self.dest_img = cv2.cvtColor(self.dest_img, cv2.COLOR_BGR2GRAY)
            if self.ui.rb_simple.isChecked() == True:
                ret, self.dest_img = cv2.threshold(self.dest_img,125,255,cv2.THRESH_BINARY)
            if self.ui.rb_adaptive.isChecked() == True:
                self.dest_img = cv2.adaptiveThreshold(self.dest_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            if self.ui.rb_otsu.isChecked() == True:
                ret, self.dest_img= cv2.threshold(self.dest_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        if self.ui.cb_transformation.checkState() == Qt.Checked:
            if self.ui.cb_translation.checkState() == Qt.Checked:
                height, width = self.dest_img.shape[:2]
                T = np.float32([[1, 0, int(self.ui.le_translation_posX.text())],\
                                [0, 1, int(self.ui.le_translation_posY.text())]])
                self.dest_img = cv2.warpAffine(self.dest_img, T, (width, height)) 
            if self.ui.cb_rotation.checkState() == Qt.Checked:
                height, width = self.dest_img.shape[:2]
                M = cv2.getRotationMatrix2D((width/2, height/2), int(self.ui.le_rotation_angle.text()), 1)
                self.dest_img = cv2.warpAffine(self.dest_img,M,(width, height))
            if self.ui.cb_perspective.checkState() == Qt.Checked:
                pts1 = np.float32([[int(self.ui.le_tlpx.text()),int(self.ui.le_tlpy.text())],\
                                   [int(self.ui.le_trpx.text()),int(self.ui.le_trpy.text())],\
                                   [int(self.ui.le_blpx.text()),int(self.ui.le_blpy.text())],\
                                   [int(self.ui.le_brpx.text()),int(self.ui.le_brpy.text())]])
                pts2 = np.float32([[0,0],[int(self.ui.le_perspective_width.text()),0],\
                                   [0,int(self.ui.le_perspective_height.text())],\
                                   [int(self.ui.le_perspective_width.text()),int(self.ui.le_perspective_height.text())]])
                M = cv2.getPerspectiveTransform(pts1,pts2)
                self.dest_img = cv2.warpPerspective(self.dest_img,M,(int(self.ui.le_perspective_width.text()),\
                                                                     int(self.ui.le_perspective_height.text())))
        return self.dest_img
    def slot_btn_preview_clicked(self):
        self.src_img = cv2.imread(self.ui.le_file_path.text(), cv2.IMREAD_COLOR)
        self.dest_img = self.image_process()
        img_t = cv2.resize(self.dest_img, (self.src_img.shape[1], self.src_img.shape[0]))
        if len(self.dest_img.shape) == 2:
            img_t = cv2.cvtColor(img_t, cv2.COLOR_GRAY2BGR)

        img_preview = cv2.hconcat([self.src_img, img_t]);
        
        
        if img_preview.shape[1] > 1000:
            w = int(1000)
            h = int(img_preview.shape[0] * 1000 / img_preview.shape[1])
            img_preview = cv2.resize(img_preview, (w, h))
        cv2.destroyAllWindows()
        cv2.imshow('preview', img_preview)
        cv2.moveWindow('preview', 300,300)
        
    def slot_btn_save_clicked(self):      
        self.save_img_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "output.jpg", "Image Files (*.jpg;*.jpeg;*.png)")
        self.dest_img = self.image_process()
        cv2.imwrite(self.save_img_path, self.dest_img)
    def slot_btn_browse_clicked(self):
        self.img_path, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Image Files (*.jpg;*.jpeg;*.png)')
        self.ui.le_file_path.setText(self.img_path)
        self.update_actions()
    def slot_cb_cvt_color_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_cvt_color.setEnabled(True)
        else:
            self.ui.frame_cvt_color.setDisabled(True)
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
    def slot_cb_transformation_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_transformation.setEnabled(True)
        else:
            self.ui.frame_transformation.setDisabled(True)
    def slot_cb_translation_toggled(self, checkState):
        if checkState == True:
            self.ui.lbl_posX.setEnabled(True)
            self.ui.lbl_posY.setEnabled(True)
            self.ui.le_translation_posX.setEnabled(True)
            self.ui.le_translation_posY.setEnabled(True)
        else:
            self.ui.lbl_posX.setDisabled(True)
            self.ui.lbl_posY.setDisabled(True)
            self.ui.le_translation_posX.setDisabled(True)
            self.ui.le_translation_posY.setDisabled(True)
    def slot_cb_rotation_toggled(self, checkState):
        if checkState == True:
            self.ui.lbl_angle.setEnabled(True)
            self.ui.le_rotation_angle.setEnabled(True)
        else:
            self.ui.lbl_angle.setDisabled(True)
            self.ui.le_angle.setDisabled(True)
    def slot_cb_perspective_toggled(self, checkState):
        if checkState == True:
            self.ui.frame_perspective.setEnabled(True)
        else:
            self.ui.frame_perspective.setDisabled(True)