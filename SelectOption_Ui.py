# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectOption_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_start(object):
    def setupUi(self, form_start):
        form_start.setObjectName("form_start")
        form_start.resize(379, 252)
        form_start.setStyleSheet("QWidget{\n"
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
        self.gridLayout = QtWidgets.QGridLayout(form_start)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(103, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(form_start)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.cbb_option = QtWidgets.QComboBox(form_start)
        self.cbb_option.setObjectName("cbb_option")
        self.cbb_option.addItem("")
        self.cbb_option.addItem("")
        self.verticalLayout.addWidget(self.cbb_option)
        self.btn_submit = QtWidgets.QPushButton(form_start)
        self.btn_submit.setObjectName("btn_submit")
        self.verticalLayout.addWidget(self.btn_submit)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 74, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 73, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)

        self.retranslateUi(form_start)
        QtCore.QMetaObject.connectSlotsByName(form_start)

    def retranslateUi(self, form_start):
        _translate = QtCore.QCoreApplication.translate
        form_start.setWindowTitle(_translate("form_start", "Select Ooption"))
        self.label.setText(_translate("form_start", "Select Options"))
        self.cbb_option.setItemText(0, _translate("form_start", "Image"))
        self.cbb_option.setItemText(1, _translate("form_start", "Video"))
        self.btn_submit.setText(_translate("form_start", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form_start = QtWidgets.QWidget()
    ui = Ui_form_start()
    ui.setupUi(form_start)
    form_start.show()
    sys.exit(app.exec_())
