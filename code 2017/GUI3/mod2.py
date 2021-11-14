# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mod2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sqlite3
from arpd import Sniffer
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import QThread
from PyQt4.QtSql import QSqlDatabase,QSqlTableModel,QSqlQuery
import _thread
import share
import time
from notification import notification
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


class NewThread(QThread):
    def __init__(self, parent=None):
        super(NewThread, self).__init__()
        self.parent = parent
        self.signal_verbose_text=QtCore.SIGNAL('signal')
    def __del__(self):
        self.wait()
    def run(self):
        time.sleep(5)
        while True:
            self.emit(self.signal_verbose_text,"hi there")
            time.sleep(5)

class Ui_MainWindow2(object):
    def __init__(self):
        self.logfile=open('logfile')
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName('sfile.db')
        self.db.open()
        self.projectModel_blocked = QSqlTableModel()
        self.projectModel_blacklist = QSqlTableModel()
        self.projectModel_mac = QSqlTableModel()
        self.sniff=Sniffer()
        self.sniff.start_gui()
        self.fnotification=share.get_flags()['notification']
    def __ref__(self):
        self.db.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(841, 574)
        MainWindow.setMaximumSize(QtCore.QSize(3000, 2000))
        MainWindow.setMenuBar(None)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab_1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.tab_1)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/7(1).jpg")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.scrollArea_2 = QtGui.QScrollArea(self.tab_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 799, 328))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tableView_mac = QtGui.QTableView(self.scrollAreaWidgetContents) #mactable

        #self.tableView_mac.verticalScrollBar().setValue(self.tableView_mac.verticalScrollBar().maximum())

        self.tableView_mac.setObjectName(_fromUtf8("tableView_mac"))
        self.tableView_mac.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.verticalLayout_3.addWidget(self.tableView_mac)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea_3 = QtGui.QScrollArea(self.tab_3)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName(_fromUtf8("scrollArea_3"))
        self.scrollAreaWidgetContents_4 = QtGui.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 799, 239))
        self.scrollAreaWidgetContents_4.setObjectName(_fromUtf8("scrollAreaWidgetContents_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.tableView_blocked = QtGui.QTableView(self.scrollAreaWidgetContents_4)  #blocked
        self.tableView_blocked.setObjectName(_fromUtf8("tableView_blocked"))
        self.tableView_blocked.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.verticalLayout_7.addWidget(self.tableView_blocked)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_4.addWidget(self.scrollArea_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setMargin(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 3, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.tab_3)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 0, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(5, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tableView_blacklist = QtGui.QTableView(self.tab_4)    #blacklist
        self.tableView_blacklist.setObjectName(_fromUtf8("tableView_blacklist"))
        self.tableView_blacklist.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.verticalLayout_6.addWidget(self.tableView_blacklist)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.textBrowser_verbose = QtGui.QTextBrowser(self.tab_5)

        #self.textBrowser_verbose.verticalScrollBar().setValue(self.textBrowser_verbose.verticalScrollBar().maximum())

        self.textBrowser_verbose.setObjectName(_fromUtf8("textBrowser_verbose")) #verbose
        self.verticalLayout_5.addWidget(self.textBrowser_verbose)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setMargin(5)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.checkBox_3 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.checkBox_4 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.checkBox_2 = QtGui.QCheckBox(self.tab_5)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.checkBox = QtGui.QCheckBox(self.tab_5)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.horizontalLayout_2.addWidget(self.checkBox)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        vbar = self.scrollArea.verticalScrollBar()
        vbar.setValue(vbar.maximum())
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 130))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 821, 166))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))

        self.textBrowser = QtGui.QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_8.addWidget(self.textBrowser)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)

        self.addBottomText('Detecting Spoofing on network ...')
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sniffing Tool 1.0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "MacTable", None))
        self.pushButton.setText(_translate("MainWindow", "Unblock", None))
        self.pushButton_2.setText(_translate("MainWindow", "Block", None))
        self.label_2.setText(_translate("MainWindow", "IP", None))
        self.label_3.setText(_translate("MainWindow", "PORT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Blocked", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "BlackList", None))
        self.checkBox_3.setText(_translate("MainWindow", "ICMP", None))
        self.checkBox_4.setText(_translate("MainWindow", "DHCP", None))
        self.checkBox_2.setText(_translate("MainWindow", "ARP", None))
        self.checkBox.setText(_translate("MainWindow", "TCP", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Verbose", None))
        self.threads(MainWindow)
        self.makeTrigger()

        #commit
        if self.fnotification:
            self.addBottomText('Notification : ON')
        else:
            self.addBottomText('Notification : OFF')
        if share.get_flags()['background']:
            self.addBottomText('Background Run : ON')
        else:
            self.addBottomText('Background Run : OFF')
        if share.get_flags()['autoblocking']:
            self.addBottomText('Autoblock IP : ON')
        else:
            self.addBottomText('Autoblock IP : OFF')

    def makeTrigger(self):
        self.checkBox.stateChanged.connect(self.checkboxsignal_tcp)
        self.checkBox_2.stateChanged.connect(self.checkboxsignal_arp)
        self.checkBox_3.stateChanged.connect(self.checkboxsignal_icmp)
        self.checkBox_4.stateChanged.connect(self.checkboxsignal_udp)
        self.pushButton_2.clicked.connect(self.manual_block_ip)
        self.pushButton.clicked.connect(self.manual_unblock_ip)
    def checkboxsignal_tcp(self):
        fg=bool(self.checkBox.isChecked())
        share.change_flag(tcp=fg)
        if fg and self.fnotification:
            notification(['Event Trigger','TCP Verbose Start'])
            self.addBottomText('Event Trigger : ' + 'TCP Verbose Start')
        if not fg:
            self.addBottomText('Event Trigger : ' + 'TCP Verbose Stop')
        self.sniff.verbose_tcp=fg
    def checkboxsignal_icmp(self):
        fg=bool(self.checkBox_2.isChecked())
        share.change_flag(icmp=fg)
        if fg and self.fnotification:
            notification(['Event Trigger','ICMP Verbose Start'])
            self.addBottomText('Event Trigger : ' + 'ICMP Verbose Start')
        if not fg:
            self.addBottomText('Event Trigger : ' + 'ICMP Verbose Stop')
        self.sniff.verbose_icmp = fg
    def checkboxsignal_arp(self):
        fg=bool(self.checkBox_2.isChecked())
        share.change_flag(arp=fg)
        if fg and self.fnotification:
            notification(['Event Trigger','ARP Verbose Start'])
            self.addBottomText('Event Trigger : ' + 'ARP Verbose Start')
        if not fg:
            self.addBottomText('Event Trigger : ' + 'ARP Verbose Stop')
        self.sniff.verbose_arp = fg
    def checkboxsignal_udp(self):
        fg=bool(self.checkBox_2.isChecked())
        share.change_flag(udp=fg)
        if fg and self.fnotification:
            notification(['Event Trigger','UDP Verbose Start'])
            self.addBottomText('Event Trigger : '+'UDP Verbose Start')
        if not fg:
            self.addBottomText('Event Trigger : ' + 'UDP Verbose Stop')
        self.sniff.verbose_udp=fg
    def manual_block_ip(self):
        ip=''
        port=''
        if(self.sniff.block_ip(ip=ip,port=port,autoblocking=True)):
            self.addBottomText('IP : '+str(ip)+' PORT : '+str(port)+' is blocked.')
        else:
            self.addBottomText('Invalid IP,PORT')
    def manual_unblock_ip(self):
        ip=''
        port=''
        if self.sniff.unblock_ip(ip=ip,port=port):
            self.addBottomText('IP : ' + str(ip) + ' PORT : ' + str(port) + ' is unblock.')
        else:
            self.addBottomText('Invalid IP,PORT')
    def threads(self,mainwindow):
        self.manageTables1()
        _thread.start_new_thread(self.SniffTraffic,())
        self.tableThreads=NewThread(self)
        mainwindow.connect(self.tableThreads,self.tableThreads.signal_verbose_text,self.manageTables)
        self.tableThreads.start()

    def SniffTraffic(self):
        print(share.get_flags())
        background=False
        if background:
            os.system('python tool.py &')
        else:
            while True:
                self.sniff.sniff_packet()

    def manageTables1(self):
        self.tableView_blocked.show()
        self.tableView_blocked.setModel(self.projectModel_blocked)
        self.tableView_blacklist.show()
        self.tableView_blacklist.setModel(self.projectModel_blacklist)
        self.tableView_mac.show()
        self.tableView_mac.setModel(self.projectModel_mac)

    def manageTables(self,text):
        try:
            self.projectModel_blocked.setQuery(QSqlQuery('select * from blocked',self.db))
            self.projectModel_blacklist.setQuery(QSqlQuery('select * from blacklist',self.db))
            self.projectModel_mac.setQuery(QSqlQuery('select * from macip',self.db))
            self.addVerboseText(self.logfile)
        except:
            print 'database lock error'

    def addVerboseText(self,logfile):
        text=logfile.read().strip()
        if text:
            self.textBrowser_verbose.append(text)

    def addBottomText(self,text):
        self.textBrowser.append(text)
import src2_rc