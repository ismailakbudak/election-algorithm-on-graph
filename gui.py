# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Nov 28 01:22:09 2014
#      by: PyQt4 UI code generator 4.10.4
# 
# Developer
# Ismail AKBUDAK
# ismailakbudak.com
# Election algorithm on graph
  
from PyQt4 import QtCore, QtGui
 
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

# Application UI
class Ui_MainWindow( ):
     
    def __init__(self):
        pass

    def setupUi(self, MainWindow): 
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 400)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Election algorithm on graph - Ismail AKBUDAK", None))
        font = QtGui.QFont()
        font.setStrikeOut(False)
        font.setPointSize(13)
        MainWindow.setFont(font) 

        # Tabs initialized
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))        
        # Tab main initialized
        self.tabMain = QtGui.QWidget()
        self.tabMain.setObjectName(_fromUtf8("tabMain")) 

        # Main - Nodes count label title
        self.labelNodesCount = QtGui.QLabel(self.tabMain)
        self.labelNodesCount.setGeometry(QtCore.QRect(85, 10, 350, 30)) 
        self.labelNodesCount.setObjectName(_fromUtf8("labelNodesCount"))
        self.labelNodesCount.setText(_translate("MainWindow", "Number of Nodes : ", None))
        # Main - Start Growing button
        self.pushButtonGrow = QtGui.QPushButton(self.tabMain)
        self.pushButtonGrow.setGeometry(QtCore.QRect(85, 50, 200, 30)) 
        self.pushButtonGrow.setObjectName(_fromUtf8("pushButtonGrow"))
        self.pushButtonGrow.setText(_translate("MainWindow", "Start Growing", None))
        #self.pushButtonDraw.clicked.connect(self.grow)
        # Main - Stop Growing button
        self.pushButtonStop = QtGui.QPushButton(self.tabMain)
        self.pushButtonStop.setGeometry(QtCore.QRect(85, 90, 200, 30)) 
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.pushButtonStop.setText(_translate("MainWindow", "Stop Growing", None))
        #self.pushButtonDraw.clicked.connect(self.grow)

        # Main - Draw Graph  button
        self.pushButtonDraw = QtGui.QPushButton(self.tabMain)
        self.pushButtonDraw.setGeometry(QtCore.QRect(85, 130, 200, 30)) 
        self.pushButtonDraw.setObjectName(_fromUtf8("pushButtonDraw"))
        self.pushButtonDraw.setText(_translate("MainWindow", "Draw Graph", None))
        #self.pushButtonDraw.clicked.connect(self.grow)

        # Main - Nodes count label title
        self.labelNodesCount = QtGui.QLabel(self.tabMain)
        self.labelNodesCount.setGeometry(QtCore.QRect(30, 200, 150, 30)) 
        self.labelNodesCount.setObjectName(_fromUtf8("labelNodesCount"))
        self.labelNodesCount.setText(_translate("MainWindow", "Starting Node : ", None))
        # Main - nodes combobax
        self.comboBoxNodes = QtGui.QComboBox(self.tabMain)
        self.comboBoxNodes.setGeometry(QtCore.QRect(150, 200, 200, 30)) 
        self.comboBoxNodes.setObjectName(_fromUtf8("comboBoxNodes"))
        for x in xrange(1,1000):
            self.comboBoxNodes.addItem("Deneme %s" % str(x) ) 
              
        # Main - Start election algorithm button
        self.pushButtonStartElection = QtGui.QPushButton(self.tabMain)
        self.pushButtonStartElection.setGeometry(QtCore.QRect(150, 240, 200, 30)) 
        self.pushButtonStartElection.setObjectName(_fromUtf8("pushButtonStartElection"))
        self.pushButtonStartElection.setText(_translate("MainWindow", "Start Election Algorithm", None))
        #self.pushButtonStartElection.clicked.connect(self.grow)

        # Tab settings initialized
        self.tabSettings = QtGui.QWidget()
        self.tabSettings.setObjectName(_fromUtf8("tabSettings"))   
        
        # settings - Grow limit label title
        self.labelNodesGrowLimit = QtGui.QLabel(self.tabSettings)
        self.labelNodesGrowLimit.setGeometry(QtCore.QRect(30, 10, 100, 30)) 
        self.labelNodesGrowLimit.setObjectName(_fromUtf8("labelNodesGrowLimit"))
        self.labelNodesGrowLimit.setText(_translate("MainWindow", "Grow Limit : ", None))
        # settings - Nodes count label title
        self.textEditGrowLimit = QtGui.QLineEdit(self.tabSettings)
        self.textEditGrowLimit.setGeometry(QtCore.QRect(130, 10, 200, 30))
        self.textEditGrowLimit.setObjectName(_fromUtf8("textEditGrowLimit")) 
        # settings - Grow limit label title
        self.labelNodesGrowthRate = QtGui.QLabel(self.tabSettings)
        self.labelNodesGrowthRate.setGeometry(QtCore.QRect(30, 50, 100, 30)) 
        self.labelNodesGrowthRate.setObjectName(_fromUtf8("labelNodesGrowthRate"))
        self.labelNodesGrowthRate.setText(_translate("MainWindow", "Growth Rate : ", None))
        # settings - Nodes count label title
        self.textEditGrowthRate = QtGui.QLineEdit(self.tabSettings)
        self.textEditGrowthRate.setGeometry(QtCore.QRect(130, 50, 200, 30))
        self.textEditGrowthRate.setObjectName(_fromUtf8("textEditGrowthRate")) 

        # Tab main initialized
        self.tabNode = QtGui.QWidget()
        self.tabNode.setObjectName(_fromUtf8("tabNode"))

        # Main window
        # Because of dialog exception 
        # MainWindow.setCentralWidget(self.centralwidget)  
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.addTab(self.tabMain, _fromUtf8(""))
        self.tabWidget.addTab(self.tabSettings, _fromUtf8("")) 
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain), _translate("MainWindow", "Main Menu", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), _translate("MainWindow", "Settings ", None)) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Fill with data
        # self.fill_fields()
    
    def fill_fields(self):
        self.fill_combobox()
        self.set_edit_line()
        self.talkWith(self.managerNymphData)
        if self.error!=None:
            self.tabWidget.setCurrentIndex(1)
            self.labelStatusSettings.setText( "Error : " + self.error + " -- Your manager is not working now.. Try connect manager.." )
        else:
            self.labelStatusSettings.setText( "You have been connected your manager.." ) 
   
    def fill_combobox(self):
        #self.comboBoxNodesUpload.insertItem (self, int index, QString text, QVariant userData = QVariant())
        #self.comboBoxNodesUpload.currentIndex()
        #self.comboBoxNodesUpload.currentText()
        #index = comobox.findData(lineedit.text())
        #combobox.setCurrentIndex(index)
        for key in nodes:
            self.comboBoxNodes.addItem( nodes[key].NAME, key )
            self.comboBoxNodesUpload.addItem( nodes[key].NAME, key ) 
    
    def add_new_message(self, nyphdata, content , type='message'  ):
        if type=='message':
            info =  "%s : %s " % ( nyphdata.NAME, content )
        else:
            info =  "%s : %s " % ( nyphdata.NAME, content )
        item = QtGui.QListWidgetItem()
        item.setText( info )
        self.listViewMessages.addItem(item)  
 
class Win(QtGui.QDialog,Ui_MainWindow):
    def __init__(self):
        Ui_MainWindow.__init__(self)
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

# Main application
if __name__ == "__main__":
    import sys 
    app = QtGui.QApplication(sys.argv) 
    MWindow = Win()
    MWindow.show()
    sys.exit(app.exec_())
