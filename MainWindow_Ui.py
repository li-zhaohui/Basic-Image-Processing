# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 575)
        MainWindow.setStyleSheet("QWidget{\n"
"background-color: rgb(75, 75, 75);\n"
"}\n"
"QComboBox{\n"
"background-color:rgb(50,50,50);\n"
"color:rgb(200,200,200)\n"
"}\n"
"QTreeView{\n"
"background-color:rgb(50,50,50);\n"
"border:1px solid rgb(25,25,25);\n"
"color:rgb(200,200,200)\n"
"}\n"
"QListView{\n"
"background-color:rgb(50,50,50);\n"
"border:1px solid rgb(25,25,25);\n"
"color:rgb(200,200,200)\n"
"}\n"
"QLineEdit{\n"
"color:rgb(200,200,200);\n"
"border:1px solid rgb(120,120,120);\n"
"background:rgb(50,50,50);\n"
"}\n"
"QPushButton {\n"
"  padding: 0px 8px;\n"
"  font-size: 16px;\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"  outline: none;\n"
"  color: rgb(86,86,86);\n"
"  background-color: rgb(14,215,185);\n"
"  border: none;\n"
"  border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {background-color:  rgb(0,172,142);}\n"
"\n"
"QPushButton:hover:pressed {\n"
"  background-color: rgb(30,152,122);\n"
"}\n"
"QScrollBar:vertical {\n"
"    border:0px solid;\n"
"    background: rgb(50,50,50);\n"
"    width: 30px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border:0px solid;\n"
"    background: rgb(50,50,50);\n"
"    height: 30px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background: rgb(80,80,80);\n"
"    width:10px;\n"
"    margin:10px;\n"
"    border-radius:5px;\n"
"    min-height:30px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(80,80,80);\n"
"    height:10px;\n"
"    margin:10px;\n"
"    border-radius:5px;\n"
"    min-width:30px;\n"
"}\n"
"QScrollBar::add-page, QScrollBar::sub-page{\n"
"background:none;\n"
"}\n"
"QScrollBar::add-page:vertical{\n"
"width:0px;\n"
"}\n"
"QScrollBar::sub-page:vertical{\n"
"width:0px;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"width: 0px;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"width: 0px;\n"
"}\n"
"QScrollBar::add-page:horizontal{\n"
"height:0px;\n"
"}\n"
"QScrollBar::sub-page:horizontal{\n"
"height:0px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"height: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"height: 0px;\n"
"}\n"
"QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"
"    width:0px;\n"
" }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical{\n"
"    height:0px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cbb_option = QtWidgets.QComboBox(self.frame_5)
        self.cbb_option.setObjectName("cbb_option")
        self.cbb_option.addItem("")
        self.cbb_option.addItem("")
        self.horizontalLayout.addWidget(self.cbb_option)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_img_path = QtWidgets.QLabel(self.frame_5)
        self.lbl_img_path.setMinimumSize(QtCore.QSize(0, 18))
        self.lbl_img_path.setMaximumSize(QtCore.QSize(50, 18))
        self.lbl_img_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_img_path.setObjectName("lbl_img_path")
        self.horizontalLayout_3.addWidget(self.lbl_img_path)
        self.le_file_path = QtWidgets.QLineEdit(self.frame_5)
        self.le_file_path.setObjectName("le_file_path")
        self.horizontalLayout_3.addWidget(self.le_file_path)
        self.btn_open = QtWidgets.QPushButton(self.frame_5)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout_3.addWidget(self.btn_open)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_7.addWidget(self.frame_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cb_cvt_color = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_cvt_color.setObjectName("cb_cvt_color")
        self.verticalLayout_5.addWidget(self.cb_cvt_color)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_resize = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_resize.setObjectName("cb_resize")
        self.verticalLayout_2.addWidget(self.cb_resize)
        self.frame_resize = QtWidgets.QFrame(self.centralwidget)
        self.frame_resize.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_resize.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_resize.setObjectName("frame_resize")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_resize)
        self.gridLayout.setObjectName("gridLayout")
        self.le_height = QtWidgets.QLineEdit(self.frame_resize)
        self.le_height.setMaximumSize(QtCore.QSize(50, 16777215))
        self.le_height.setObjectName("le_height")
        self.gridLayout.addWidget(self.le_height, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_resize)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_resize)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.le_width = QtWidgets.QLineEdit(self.frame_resize)
        self.le_width.setMaximumSize(QtCore.QSize(50, 16777215))
        self.le_width.setObjectName("le_width")
        self.gridLayout.addWidget(self.le_width, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_resize)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.cb_filters = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_filters.setObjectName("cb_filters")
        self.verticalLayout_6.addWidget(self.cb_filters)
        self.frame_filters = QtWidgets.QFrame(self.centralwidget)
        self.frame_filters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_filters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_filters.setObjectName("frame_filters")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_filters)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_mean = QtWidgets.QRadioButton(self.frame_filters)
        self.rb_mean.setChecked(True)
        self.rb_mean.setObjectName("rb_mean")
        self.verticalLayout.addWidget(self.rb_mean)
        self.rb_gaussian = QtWidgets.QRadioButton(self.frame_filters)
        self.rb_gaussian.setObjectName("rb_gaussian")
        self.verticalLayout.addWidget(self.rb_gaussian)
        self.rb_median = QtWidgets.QRadioButton(self.frame_filters)
        self.rb_median.setObjectName("rb_median")
        self.verticalLayout.addWidget(self.rb_median)
        self.rb_bilateral = QtWidgets.QRadioButton(self.frame_filters)
        self.rb_bilateral.setObjectName("rb_bilateral")
        self.verticalLayout.addWidget(self.rb_bilateral)
        self.rb_averaging = QtWidgets.QRadioButton(self.frame_filters)
        self.rb_averaging.setObjectName("rb_averaging")
        self.verticalLayout.addWidget(self.rb_averaging)
        self.verticalLayout_6.addWidget(self.frame_filters)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.cb_edges = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_edges.setEnabled(True)
        self.cb_edges.setObjectName("cb_edges")
        self.verticalLayout_10.addWidget(self.cb_edges)
        self.frame_edges = QtWidgets.QFrame(self.centralwidget)
        self.frame_edges.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_edges.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_edges.setObjectName("frame_edges")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_edges)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.rb_canny = QtWidgets.QRadioButton(self.frame_edges)
        self.rb_canny.setChecked(True)
        self.rb_canny.setObjectName("rb_canny")
        self.verticalLayout_9.addWidget(self.rb_canny)
        self.rb_sobel = QtWidgets.QRadioButton(self.frame_edges)
        self.rb_sobel.setObjectName("rb_sobel")
        self.verticalLayout_9.addWidget(self.rb_sobel)
        self.rb_prewitt = QtWidgets.QRadioButton(self.frame_edges)
        self.rb_prewitt.setObjectName("rb_prewitt")
        self.verticalLayout_9.addWidget(self.rb_prewitt)
        self.rb_laplace = QtWidgets.QRadioButton(self.frame_edges)
        self.rb_laplace.setObjectName("rb_laplace")
        self.verticalLayout_9.addWidget(self.rb_laplace)
        self.verticalLayout_10.addWidget(self.frame_edges)
        self.verticalLayout_5.addLayout(self.verticalLayout_10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.cb_thresholding = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_thresholding.setEnabled(True)
        self.cb_thresholding.setObjectName("cb_thresholding")
        self.verticalLayout_14.addWidget(self.cb_thresholding)
        self.frame_thresholding = QtWidgets.QFrame(self.centralwidget)
        self.frame_thresholding.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_thresholding.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_thresholding.setObjectName("frame_thresholding")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_thresholding)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.rb_simple = QtWidgets.QRadioButton(self.frame_thresholding)
        self.rb_simple.setChecked(True)
        self.rb_simple.setObjectName("rb_simple")
        self.verticalLayout_13.addWidget(self.rb_simple)
        self.rb_adaptive = QtWidgets.QRadioButton(self.frame_thresholding)
        self.rb_adaptive.setObjectName("rb_adaptive")
        self.verticalLayout_13.addWidget(self.rb_adaptive)
        self.rb_otsu = QtWidgets.QRadioButton(self.frame_thresholding)
        self.rb_otsu.setObjectName("rb_otsu")
        self.verticalLayout_13.addWidget(self.rb_otsu)
        self.verticalLayout_14.addWidget(self.frame_thresholding)
        self.verticalLayout_4.addLayout(self.verticalLayout_14)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.cb_segmentation = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_segmentation.setObjectName("cb_segmentation")
        self.verticalLayout_15.addWidget(self.cb_segmentation)
        self.frame_segmentation = QtWidgets.QFrame(self.centralwidget)
        self.frame_segmentation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_segmentation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_segmentation.setObjectName("frame_segmentation")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_segmentation)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.rb_foreground = QtWidgets.QRadioButton(self.frame_segmentation)
        self.rb_foreground.setChecked(True)
        self.rb_foreground.setObjectName("rb_foreground")
        self.verticalLayout_12.addWidget(self.rb_foreground)
        self.rb_background = QtWidgets.QRadioButton(self.frame_segmentation)
        self.rb_background.setObjectName("rb_background")
        self.verticalLayout_12.addWidget(self.rb_background)
        self.verticalLayout_15.addWidget(self.frame_segmentation)
        self.verticalLayout_4.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.cb_transformation = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_transformation.setObjectName("cb_transformation")
        self.verticalLayout_16.addWidget(self.cb_transformation)
        self.frame_transformation = QtWidgets.QFrame(self.centralwidget)
        self.frame_transformation.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_transformation.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_transformation.setObjectName("frame_transformation")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_transformation)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.rb_scaling = QtWidgets.QRadioButton(self.frame_transformation)
        self.rb_scaling.setChecked(True)
        self.rb_scaling.setObjectName("rb_scaling")
        self.verticalLayout_11.addWidget(self.rb_scaling)
        self.rb_transaction = QtWidgets.QRadioButton(self.frame_transformation)
        self.rb_transaction.setChecked(False)
        self.rb_transaction.setObjectName("rb_transaction")
        self.verticalLayout_11.addWidget(self.rb_transaction)
        self.rb_rotation = QtWidgets.QRadioButton(self.frame_transformation)
        self.rb_rotation.setObjectName("rb_rotation")
        self.verticalLayout_11.addWidget(self.rb_rotation)
        self.rb_perspective = QtWidgets.QRadioButton(self.frame_transformation)
        self.rb_perspective.setObjectName("rb_perspective")
        self.verticalLayout_11.addWidget(self.rb_perspective)
        self.verticalLayout_16.addWidget(self.frame_transformation)
        self.verticalLayout_4.addLayout(self.verticalLayout_16)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_start_process = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start_process.setEnabled(False)
        self.btn_start_process.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_start_process.setObjectName("btn_start_process")
        self.horizontalLayout_2.addWidget(self.btn_start_process)
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setEnabled(False)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Options:"))
        self.cbb_option.setItemText(0, _translate("MainWindow", "Image"))
        self.cbb_option.setItemText(1, _translate("MainWindow", "Video"))
        self.lbl_img_path.setText(_translate("MainWindow", "File Path:"))
        self.btn_open.setText(_translate("MainWindow", "open"))
        self.cb_cvt_color.setText(_translate("MainWindow", "Convert Color"))
        self.cb_resize.setText(_translate("MainWindow", "Resize"))
        self.label_3.setText(_translate("MainWindow", "Height"))
        self.label_2.setText(_translate("MainWindow", "Width:"))
        self.cb_filters.setText(_translate("MainWindow", "Filters"))
        self.rb_mean.setText(_translate("MainWindow", "Mean"))
        self.rb_gaussian.setText(_translate("MainWindow", "Gaussian"))
        self.rb_median.setText(_translate("MainWindow", "Median"))
        self.rb_bilateral.setText(_translate("MainWindow", "Bilateral"))
        self.rb_averaging.setText(_translate("MainWindow", "Averaging"))
        self.cb_edges.setText(_translate("MainWindow", "Edges"))
        self.rb_canny.setText(_translate("MainWindow", "Canny"))
        self.rb_sobel.setText(_translate("MainWindow", "Sobel"))
        self.rb_prewitt.setText(_translate("MainWindow", "Prewitt"))
        self.rb_laplace.setText(_translate("MainWindow", "Laplace"))
        self.cb_thresholding.setText(_translate("MainWindow", "Thresholding"))
        self.rb_simple.setText(_translate("MainWindow", "Simple"))
        self.rb_adaptive.setText(_translate("MainWindow", "Adaptive"))
        self.rb_otsu.setText(_translate("MainWindow", "OTSU"))
        self.cb_segmentation.setText(_translate("MainWindow", "Segmentation"))
        self.rb_foreground.setText(_translate("MainWindow", "Foreground"))
        self.rb_background.setText(_translate("MainWindow", "Background"))
        self.cb_transformation.setText(_translate("MainWindow", "Transformation"))
        self.rb_scaling.setText(_translate("MainWindow", "Scaling"))
        self.rb_transaction.setText(_translate("MainWindow", "Translation"))
        self.rb_rotation.setText(_translate("MainWindow", "Rotation"))
        self.rb_perspective.setText(_translate("MainWindow", "Perspective"))
        self.btn_start_process.setText(_translate("MainWindow", "start process"))
        self.btn_save.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

