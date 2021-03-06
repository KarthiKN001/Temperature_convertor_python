# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temp_convertor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 355)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 497, 266))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.splitter_4 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.input_field = QtWidgets.QLineEdit(self.splitter_4)
        self.input_field.setObjectName("input_field")
        self.result_field = QtWidgets.QLineEdit(self.splitter_4)
        self.result_field.setObjectName("result_field")
        self.verticalLayout.addWidget(self.splitter_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_6 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.ktoc_btn = QtWidgets.QPushButton(self.splitter_6)
        self.ktoc_btn.setObjectName("ktoc_btn")
        self.ctof_btn = QtWidgets.QPushButton(self.splitter_6)
        self.ctof_btn.setObjectName("ctof_btn")
        self.ftok_btn = QtWidgets.QPushButton(self.splitter_6)
        self.ftok_btn.setObjectName("ftok_btn")
        self.horizontalLayout_2.addWidget(self.splitter_6)
        self.splitter_5 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.ktof_btn = QtWidgets.QPushButton(self.splitter_5)
        self.ktof_btn.setObjectName("ktof_btn")
        self.ctok_btn = QtWidgets.QPushButton(self.splitter_5)
        self.ctok_btn.setObjectName("ctok_btn")
        self.ftoc_btn = QtWidgets.QPushButton(self.splitter_5)
        self.ftoc_btn.setObjectName("ftoc_btn")
        self.horizontalLayout_2.addWidget(self.splitter_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.clear_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout_2.addWidget(self.clear_btn)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.one_btn = QtWidgets.QPushButton(self.splitter)
        self.one_btn.setObjectName("one_btn")
        self.four_btn = QtWidgets.QPushButton(self.splitter)
        self.four_btn.setObjectName("four_btn")
        self.seven_btn = QtWidgets.QPushButton(self.splitter)
        self.seven_btn.setObjectName("seven_btn")
        self.minus_btn = QtWidgets.QPushButton(self.splitter)
        self.minus_btn.setObjectName("minus_btn")
        self.horizontalLayout.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.two_btn = QtWidgets.QPushButton(self.splitter_2)
        self.two_btn.setObjectName("two_btn")
        self.five_btn = QtWidgets.QPushButton(self.splitter_2)
        self.five_btn.setObjectName("five_btn")
        self.eight_btn = QtWidgets.QPushButton(self.splitter_2)
        self.eight_btn.setObjectName("eight_btn")
        self.dot_btn = QtWidgets.QPushButton(self.splitter_2)
        self.dot_btn.setObjectName("dot_btn")
        self.horizontalLayout.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.three_btn = QtWidgets.QPushButton(self.splitter_3)
        self.three_btn.setObjectName("three_btn")
        self.six_btn = QtWidgets.QPushButton(self.splitter_3)
        self.six_btn.setObjectName("six_btn")
        self.nine_btn = QtWidgets.QPushButton(self.splitter_3)
        self.nine_btn.setObjectName("nine_btn")
        self.zero_btn = QtWidgets.QPushButton(self.splitter_3)
        self.zero_btn.setObjectName("zero_btn")
        self.horizontalLayout.addWidget(self.splitter_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_7 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.label_2 = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.splitter_7)
        self.splitter_8 = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_5 = QtWidgets.QLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.splitter_8)
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.splitter_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 26))
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
        self.label.setText(_translate("MainWindow", "TEMPERATURE  CONVERTOR"))
        self.ktoc_btn.setText(_translate("MainWindow", "K to C"))
        self.ctof_btn.setText(_translate("MainWindow", "C to F"))
        self.ftok_btn.setText(_translate("MainWindow", "F to K"))
        self.ktof_btn.setText(_translate("MainWindow", "K to F"))
        self.ctok_btn.setText(_translate("MainWindow", "C to K"))
        self.ftoc_btn.setText(_translate("MainWindow", "F to C"))
        self.clear_btn.setText(_translate("MainWindow", "CLEAR"))
        self.one_btn.setText(_translate("MainWindow", "1"))
        self.four_btn.setText(_translate("MainWindow", "4"))
        self.seven_btn.setText(_translate("MainWindow", "7"))
        self.minus_btn.setText(_translate("MainWindow", "-"))
        self.two_btn.setText(_translate("MainWindow", "2"))
        self.five_btn.setText(_translate("MainWindow", "5"))
        self.eight_btn.setText(_translate("MainWindow", "8"))
        self.dot_btn.setText(_translate("MainWindow", "."))
        self.three_btn.setText(_translate("MainWindow", "3"))
        self.six_btn.setText(_translate("MainWindow", "6"))
        self.nine_btn.setText(_translate("MainWindow", "9"))
        self.zero_btn.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "K - Kelvin"))
        self.label_3.setText(_translate("MainWindow", "C - Celsius"))
        self.label_4.setText(_translate("MainWindow", "F - Fahrenheit"))
        self.label_5.setText(_translate("MainWindow", "Joker\"s"))
        self.label_6.setText(_translate("MainWindow", "           Brand"))
