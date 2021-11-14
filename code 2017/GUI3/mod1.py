# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod1.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from mod2 import Ui_MainWindow2
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class MyDialog2(QtGui.QMainWindow, Ui_MainWindow2):
    def __init__(self, options,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(840, 482)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("7(1).jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setAutoRepeat(False)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout.addWidget(self.checkBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 840, 24))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuSniff = QtGui.QMenu(self.menubar)
        self.menuSniff.setObjectName(_fromUtf8("menuSniff"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.startSniff = QtGui.QAction(MainWindow)
        self.startSniff.setObjectName(_fromUtf8("startSniff"))
        self.actionExit_2 = QtGui.QAction(MainWindow)
        self.actionExit_2.setObjectName(_fromUtf8("actionExit_2"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuSniff.addAction(self.startSniff)
        self.menuInfo.addAction(self.actionHelp)
        self.menuInfo.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSniff.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.retranslateUi(MainWindow)
        self.makeTrigger(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sniffing Tool 1.0", None))
        MainWindow.setWindowIcon(QtGui.QIcon('png.png'))
        self.checkBox.setText(_translate("MainWindow", "Run in background", None))
        self.checkBox_2.setText(_translate("MainWindow", "Autoblock blacklisted IPs", None))
        self.checkBox_3.setText(_translate("MainWindow", "Allow notification", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuSniff.setTitle(_translate("MainWindow", "Sniff", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Save", None))
        self.startSniff.setText(_translate("MainWindow", "Start Sniffing", None))
        self.actionExit_2.setText(_translate("MainWindow", "Exit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
    def makeTrigger(self,MainWindow):
        #self.startSniff.triggered.connect(self.startSniffing)
        self.actionExit_2.triggered.connect(QtGui.qApp.quit)
        self.actionHelp.triggered.connect(self.help)
        self.actionAbout.triggered.connect(self.about)
        MainWindow.close()
    #Other Function
    def help(self):
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("7(2).jpg")))
    def about(self):
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("7(3).jpg")))
import src1_rc
