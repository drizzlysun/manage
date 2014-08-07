import sys
from PyQt4 import QtGui,QtCore
class test_slot(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.Qwidget.__init__(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('test_SLOT')
        quit = QtGui.QPushButton('Close', self)
        quit.setGeometry(10, 10, 60, 35)
        self.connect(quit, QtCore.SIGNAL('clicked()'), QtGui.qApp,QtCore.SLOT('messageout()'))
    def messageout(self):
        reply=QtGui





