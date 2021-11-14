import sys
from PyQt4 import QtGui

from mod1 import Ui_MainWindow1
from mod2 import Ui_MainWindow2
class GUI(QtGui.QMainWindow):
	def __init__(self,parent=None):
		super(GUI,self).__init__(parent)
		self.uiWindow1=Ui_MainWindow1()
		self.uiWindow2=Ui_MainWindow2()
		self.uiWindow1.setupUi(self)
		self.uiWindow1.startSniff.triggered.connect(self.startUiWindow2)
		self.show()
	def startUiWindow2(self):
		self.uiWindow2.setupUi(self)
		self.show()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp1 = GUI()
    app.exec_()
    sys.exit()