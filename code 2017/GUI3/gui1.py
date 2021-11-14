import sys
from PyQt4 import QtGui

from mod1 import Ui_MainWindow1
from mod2 import Ui_MainWindow2
from share import change_flag


class GUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.uiWindow1 = Ui_MainWindow1()
        self.uiWindow2 = Ui_MainWindow2()
        self.uiWindow1.setupUi(self)
        self.uiWindow1.startSniff.triggered.connect(self.startUiWindow2)
        self.show()

    def makeStat(self):
        background = bool(self.uiWindow1.checkBox.checkState())
        autoblocking = bool(self.uiWindow1.checkBox_2.checkState())
        notification = bool(self.uiWindow1.checkBox_3.checkState())
        change_flag(background=background, autoblocking=autoblocking, notification=notification)

    def startUiWindow2(self):
        self.makeStat()
        self.uiWindow2.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp1 = GUI()
    app.exec_()
    sys.exit()
