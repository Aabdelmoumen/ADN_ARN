# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1061, 691)
        MainWindow.setMinimumSize(QtCore.QSize(1061, 691))
        MainWindow.setMaximumSize(QtCore.QSize(1061, 691))
        MainWindow.setStyleSheet("background-color: #434544;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget{background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #343434;\n"
"}\n"
" QTabBar::tab:selected {\n"
"  background: #656563;\n"
"border-left: 1px solid #343434;\n"
" border-right: 1px solid #343434;\n"
"border-top:1px solid #343434;\n"
"\n"
" }\n"
" QTabBar::tab {\n"
" border-left: 1px solid #343434;\n"
" border-right: 1px solid #343434;\n"
"border-top:1px solid #343434;\n"
"padding-left:6px;\n"
"padding-right:6px;\n"
"padding-bottom:6px;\n"
"padding-top:6px;\n"
"background: #434544;\n"
"color:#c2c2c2;\n"
" \n"
" \n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.ADN = QtWidgets.QWidget()
        self.ADN.setObjectName("ADN")
        self.frame = QtWidgets.QFrame(self.ADN)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 1061, 691))
        self.frame.setStyleSheet("background-color: #636363;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 20, 220, 171))
        self.groupBox_6.setStyleSheet("QGroupBox \n"
"{\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} \n"
"")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.groupBox_6.setFlat(False)
        self.groupBox_6.setObjectName("groupBox_6")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton.setGeometry(QtCore.QRect(20, 30, 160, 17))
        self.radioButton.setStyleSheet("color:#c2c2c2")
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setGeometry(QtCore.QRect(40, 60, 40, 20))
        self.lineEdit.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 60, 40, 20))
        self.lineEdit_2.setStyleSheet("background-color: #292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.ValiderNbrAdn = QtWidgets.QPushButton(self.groupBox_6)
        self.ValiderNbrAdn.setGeometry(QtCore.QRect(150, 60, 50, 23))
        self.ValiderNbrAdn.setStyleSheet("color:\"white\";\n"
"background-color:#d50000;")
        self.ValiderNbrAdn.setObjectName("ValiderNbrAdn")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 90, 100, 17))
        self.radioButton_2.setStyleSheet("color:#c2c2c2;")
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 120, 120, 23))
        self.pushButton_7.setStyleSheet("color:\"white\";\n"
"background-color:#d50000;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setGeometry(QtCore.QRect(20, 210, 220, 71))
        self.groupBox_7.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} \n"
"")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_4.setGeometry(QtCore.QRect(40, 20, 131, 17))
        self.radioButton_4.setStyleSheet("font: 75 10pt \"Tw Cen MT\";\n"
"color:#c2c2c2")
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_7)
        self.radioButton_3.setGeometry(QtCore.QRect(40, 40, 121, 17))
        self.radioButton_3.setStyleSheet("color:#c2c2c2;\n"
"font: 75 10pt \"Tw Cen MT\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 290, 220, 281))
        self.groupBox.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius:8px 8px 8px 8px;\n"
"} \n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 70, 171, 23))
        self.pushButton_2.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 100, 171, 23))
        self.pushButton_3.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 130, 171, 23))
        self.pushButton_4.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 160, 171, 23))
        self.pushButton_5.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 190, 171, 23))
        self.pushButton_6.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(20, 220, 171, 23))
        self.pushButton_8.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 40, 171, 23))
        self.pushButton_13.setStyleSheet("background-color:#d50000;\n"
"color:\"white\"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.frame)
        self.tabWidget_3.setGeometry(QtCore.QRect(260, 20, 471, 401))
        self.tabWidget_3.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid #c2c2c2;\n"
"}\n"
" QTabBar::tab:selected {\n"
"color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";\n"
"\n"
"  background: #656563;\n"
"border-left: 1px solid #c2c2c2;\n"
" border-right: 1px solid #c2c2c2;\n"
"border-top:1px solid #c2c2c2;\n"
"\n"
" }\n"
" QTabBar::tab {\n"
" border-left: 1px solid #343434;\n"
" border-right: 1px solid #343434;\n"
"border-top:1px solid #343434;\n"
"padding-left:6px;\n"
"padding-right:6px;\n"
"padding-bottom:6px;\n"
"padding-top:6px;\n"
"background: #434544;\n"
"color:#c2c2c2;\n"
" \n"
" \n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.fADN = QtWidgets.QWidget()
        self.fADN.setObjectName("fADN")
        self.listWidget = QtWidgets.QListWidget(self.fADN)
        self.listWidget.setGeometry(QtCore.QRect(20, 20, 431, 341))
        self.listWidget.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.textEdit = QtWidgets.QTextEdit(self.fADN)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 431, 341))
        self.textEdit.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.listWidget_2 = QtWidgets.QListWidget(self.fADN)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 20, 431, 341))
        self.listWidget_2.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.listWidget_2.setObjectName("listWidget_2")
        icon = QtGui.QIcon.fromTheme("col")
        self.tabWidget_3.addTab(self.fADN, icon, "")
        self.rADN = QtWidgets.QWidget()
        self.rADN.setObjectName("rADN")
        self.textEdit_4 = QtWidgets.QTextEdit(self.rADN)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 20, 431, 341))
        self.textEdit_4.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.textEdit_4.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.tabWidget_3.addTab(self.rADN, "")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(260, 450, 776, 100))
        self.groupBox_4.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} ")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_3.setGeometry(QtCore.QRect(20, 30, 740, 40))
        self.textBrowser_3.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame)
        self.pushButton_9.setGeometry(QtCore.QRect(810, 350, 141, 23))
        self.pushButton_9.setStyleSheet("background-color:#d50000;\n"
"color:\"white\";\n"
"font: 75 8pt \"Tw Cen MT\";")
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(740, 90, 291, 241))
        self.groupBox_2.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} ")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(125, 140, 40, 22))
        self.textBrowser.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(125, 190, 40, 22))
        self.textBrowser_2.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(130, 120, 31, 16))
        self.label.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(65, 170, 161, 16))
        self.label_6.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label_6.setObjectName("label_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 30, 151, 81))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(30, 20, 40, 22))
        self.textBrowser_4.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_5.setGeometry(QtCore.QRect(100, 20, 40, 22))
        self.textBrowser_5.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_6.setGeometry(QtCore.QRect(100, 50, 40, 22))
        self.textBrowser_6.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox_3)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 50, 40, 22))
        self.textBrowser_7.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 21, 16))
        self.label_5.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(80, 20, 16, 16))
        self.label_4.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 16, 16))
        self.label_3.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(80, 50, 16, 16))
        self.label_2.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.label_7.setStyleSheet("font: 75 10pt \"Tw Cen MT\";;\n"
"color:#c2c2c2;")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 200, 71, 16))
        self.label_8.setStyleSheet("font: 75 10pt \"Tw Cen MT\";\n"
"color:#c2c2c2;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 282, 71, 16))
        self.label_9.setStyleSheet("color:#c2c2c2;")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(270, 440, 151, 16))
        self.label_10.setStyleSheet("color:#c2c2c2;\n"
"font: 75 10pt \"Tw Cen MT\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(750, 80, 47, 16))
        self.label_11.setStyleSheet("color:#c2c2c2;")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(820, 110, 41, 20))
        self.label_12.setStyleSheet("color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";")
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QLabel(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(230, 560, 23, 23))
        self.pushButton.setStyleSheet("color:#d50000;\n"
"font: 12pt ;\n"
"background-color:#c2c2c2;;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_14 = QtWidgets.QLabel(self.frame)
        self.pushButton_14.setGeometry(QtCore.QRect(230, 180, 23, 23))
        self.pushButton_14.setStyleSheet("color:#d50000;\n"
"font: 12pt ;\n"
"\n"
"background-color:#c2c2c2;;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame)
        self.pushButton_16.setGeometry(QtCore.QRect(660, 560, 141, 23))
        self.pushButton_16.setStyleSheet("background-color:#d50000;\n"
"color:\"white\";\n"
"font: 75 8pt \"Tw Cen MT\";")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.frame)
        self.pushButton_17.setGeometry(QtCore.QRect(492, 560, 141, 23))
        self.pushButton_17.setStyleSheet("background-color:#d50000;\n"
"color:\"white\";\n"
"font: 75 8pt \"Tw Cen MT\";")
        self.pushButton_17.setObjectName("pushButton_17")
        self.tabWidget.addTab(self.ADN, "")
        self.ARN = QtWidgets.QWidget()
        self.ARN.setObjectName("ARN")
        self.frame_2 = QtWidgets.QFrame(self.ARN)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1043, 632))
        self.frame_2.setStyleSheet("background-color: #636363;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_8.setGeometry(QtCore.QRect(412, 30, 220, 147))
        self.groupBox_8.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} ")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_10.setGeometry(QtCore.QRect(20, 30, 171, 23))
        self.pushButton_10.setStyleSheet("color:\"white\";\n"
"background-color:#d50000;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_11.setGeometry(QtCore.QRect(20, 60, 171, 23))
        self.pushButton_11.setStyleSheet("color:\"white\";\n"
"background-color:#d50000;")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_12.setGeometry(QtCore.QRect(20, 90, 171, 23))
        self.pushButton_12.setStyleSheet("color:\"white\";\n"
"background-color:#d50000;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget_2.setGeometry(QtCore.QRect(40, 310, 963, 121))
        self.tabWidget_2.setStyleSheet("QTabWidget::pane {\n"
"    border: 1px solid #c2c2c2;\n"
"}\n"
" QTabBar::tab:selected {\n"
"color:#c2c2c2;\n"
"font: 75 9pt \"Tw Cen MT\";\n"
"\n"
"  background: #656563;\n"
"border-left: 1px solid #c2c2c2;\n"
" border-right: 1px solid #c2c2c2;\n"
"border-top:1px solid #c2c2c2;\n"
"\n"
" }\n"
" QTabBar::tab {\n"
" border-left: 1px solid #343434;\n"
" border-right: 1px solid #343434;\n"
"border-top:1px solid #343434;\n"
"padding-left:6px;\n"
"padding-right:6px;\n"
"padding-bottom:6px;\n"
"padding-top:6px;\n"
"background: #434544;\n"
"color:#c2c2c2;\n"
" \n"
" \n"
" }\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.sARN = QtWidgets.QWidget()
        self.sARN.setObjectName("sARN")
        self.textEdit_3 = QtWidgets.QTextEdit(self.sARN)
        self.textEdit_3.setEnabled(True)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 30, 923, 40))
        self.textEdit_3.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.textEdit_3.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.tabWidget_2.addTab(self.sARN, "")
        self.eARN = QtWidgets.QWidget()
        self.eARN.setObjectName("eARN")
        self.textEdit_2 = QtWidgets.QTextEdit(self.eARN)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 30, 923, 40))
        self.textEdit_2.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.textEdit_2.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget_2.addTab(self.eARN, "")
        self.sProtein = QtWidgets.QGroupBox(self.frame_2)
        self.sProtein.setGeometry(QtCore.QRect(40, 450, 963, 100))
        self.sProtein.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} ")
        self.sProtein.setTitle("")
        self.sProtein.setObjectName("sProtein")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.sProtein)
        self.textBrowser_9.setGeometry(QtCore.QRect(20, 30, 923, 40))
        self.textBrowser_9.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;\n"
"font: 75 12pt \"Tw Cen MT\";")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(430, 20, 76, 16))
        self.label_14.setStyleSheet("font: 75 10pt \"Tw Cen MT\";\n"
"color:#c2c2c2;")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        self.label_15.setGeometry(QtCore.QRect(50, 440, 111, 16))
        self.label_15.setStyleSheet("font: 75 10pt \"Tw Cen MT\";\n"
"color:#c2c2c2;")
        self.label_15.setObjectName("label_15")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_5.setGeometry(QtCore.QRect(447, 200, 150, 50))
        self.groupBox_5.setStyleSheet("QGroupBox \n"
"{\n"
"\n"
"color:#c2c2c2;\n"
"margin: 0em;\n"
"  border: 1px solid #c2c2c2; \n"
"  border-radius: 8px;\n"
"} ")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_8.setGeometry(QtCore.QRect(45, 14, 61, 22))
        self.textBrowser_8.setStyleSheet("background-color:#292929;\n"
" border: 1px solid #292929;\n"
"color:#c2c2c2;")
        self.textBrowser_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setGeometry(QtCore.QRect(470, 190, 107, 16))
        self.label_16.setStyleSheet("font: 75 10pt \"Tw Cen MT\";\n"
"color:#c2c2c2;")
        self.label_16.setObjectName("label_16")
        self.pushButton_15 = QtWidgets.QLabel   (self.frame_2)
        self.pushButton_15.setGeometry(QtCore.QRect(620, 170, 23, 23))
        self.pushButton_15.setStyleSheet("color:#d50000;\n"
"font: 12pt ;\n"
"\n"
"background-color:#c2c2c2;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.tabWidget.addTab(self.ARN, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Generer Sequence Aleatoire"))
        self.ValiderNbrAdn.setText(_translate("MainWindow", "Valider"))
        self.radioButton_2.setText(_translate("MainWindow", "Charger Fichier"))
        self.pushButton_7.setText(_translate("MainWindow", "Chemin Vers Fichier"))
        self.radioButton_4.setText(_translate("MainWindow", "Toutes les sequences"))
        self.radioButton_3.setText(_translate("MainWindow", "Une seul sequences"))
        self.pushButton_2.setText(_translate("MainWindow", "Frequence Bn ADN"))
        self.pushButton_3.setText(_translate("MainWindow", "Generer ARN"))
        self.pushButton_4.setText(_translate("MainWindow", "Reverse ADN"))
        self.pushButton_5.setText(_translate("MainWindow", "%GC"))
        self.pushButton_6.setText(_translate("MainWindow", " Fréquences de codons dans ADN"))
        self.pushButton_8.setText(_translate("MainWindow", "L\'assemblage des fragments ADN"))
        self.pushButton_13.setText(_translate("MainWindow", "Verifier Validite ADN"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.fADN), _translate("MainWindow", "Fragments ADNs"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.rADN), _translate("MainWindow", "ADNs Reverse"))
        self.pushButton_9.setText(_translate("MainWindow", "Sauvegarder les Resultat"))
        self.label.setText(_translate("MainWindow", "%GC"))
        self.label_6.setText(_translate("MainWindow", " Fréquences de codons dans ADN"))
        self.label_5.setText(_translate("MainWindow", "G:"))
        self.label_4.setText(_translate("MainWindow", "C:"))
        self.label_3.setText(_translate("MainWindow", "A:"))
        self.label_2.setText(_translate("MainWindow", "T:"))
        self.label_7.setText(_translate("MainWindow", "Chargements des données:"))
        self.label_8.setText(_translate("MainWindow", "Travailler sur:"))
        self.label_9.setText(_translate("MainWindow", "Fonction ADN:"))
        self.label_10.setText(_translate("MainWindow", " Fragments ADNs assemblés:"))
        self.label_11.setText(_translate("MainWindow", "Resultat:"))
        self.label_12.setText(_translate("MainWindow", "Bn ADN:"))
        self.pushButton.setText(_translate("MainWindow", "?"))
        self.pushButton_14.setText(_translate("MainWindow", "?"))
        self.pushButton_16.setText(_translate("MainWindow", "Dissimuler les graphe"))
        self.pushButton_17.setText(_translate("MainWindow", "Afficher les Graphe"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ADN), _translate("MainWindow", "ADN"))
        self.pushButton_10.setText(_translate("MainWindow", "Transcription ARN en protéines"))
        self.pushButton_11.setText(_translate("MainWindow", "Calculer la masse protéique"))
        self.pushButton_12.setText(_translate("MainWindow", "Effectuer l\'épissage d\'ARN"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.sARN), _translate("MainWindow", "Sequence ARN"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.eARN), _translate("MainWindow", "ARN apres epissage"))
        self.label_14.setText(_translate("MainWindow", "Fonction ARN:"))
        self.label_15.setText(_translate("MainWindow", "Sequence proteique:"))
        self.label_16.setText(_translate("MainWindow", "La masse protéique:"))
        self.pushButton_15.setText(_translate("MainWindow", "?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ARN), _translate("MainWindow", "ARN"))
