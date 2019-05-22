from PyQt4 import QtCore, QtGui
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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setWindowIcon(QtGui.QIcon("FIcon.png"))



    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(838, 283)
        MainWindow.setWindowIcon(QtGui.QIcon("FIcon.png"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pikemen1 = QtGui.QLabel(self.centralwidget)
        self.pikemen1.setObjectName(_fromUtf8("pikemen1"))
        self.gridLayout.addWidget(self.pikemen1, 6, 0, 1, 1)
        self.footmen2 = QtGui.QLabel(self.centralwidget)
        self.footmen2.setObjectName(_fromUtf8("footmen2"))
        self.gridLayout.addWidget(self.footmen2, 3, 3, 1, 1)
        self.calvary1 = QtGui.QLabel(self.centralwidget)
        self.calvary1.setObjectName(_fromUtf8("calvary1"))
        self.gridLayout.addWidget(self.calvary1, 5, 0, 1, 1)
        self.archers1 = QtGui.QLabel(self.centralwidget)
        self.archers1.setObjectName(_fromUtf8("archers1"))
        self.gridLayout.addWidget(self.archers1, 4, 0, 1, 1)
        self.knights1 = QtGui.QLabel(self.centralwidget)
        self.knights1.setObjectName(_fromUtf8("knights1"))
        self.gridLayout.addWidget(self.knights1, 7, 0, 1, 1)
        self.footmen1line = QtGui.QLineEdit(self.centralwidget)
        self.footmen1line.setObjectName(_fromUtf8("footmen1line"))
        self.gridLayout.addWidget(self.footmen1line, 3, 1, 1, 1)
        self.calvary1line = QtGui.QLineEdit(self.centralwidget)
        self.calvary1line.setObjectName(_fromUtf8("calvary1line"))
        self.gridLayout.addWidget(self.calvary1line, 5, 1, 1, 1)
        self.calvary2 = QtGui.QLabel(self.centralwidget)
        self.calvary2.setObjectName(_fromUtf8("calvary2"))
        self.gridLayout.addWidget(self.calvary2, 5, 3, 1, 1)
        self.pikemen2line_2 = QtGui.QLineEdit(self.centralwidget)
        self.pikemen2line_2.setObjectName(_fromUtf8("pikemen2line_2"))
        self.gridLayout.addWidget(self.pikemen2line_2, 7, 4, 1, 1)
        self.pikemen2 = QtGui.QLabel(self.centralwidget)
        self.pikemen2.setObjectName(_fromUtf8("pikemen2"))
        self.gridLayout.addWidget(self.pikemen2, 6, 3, 1, 1)
        self.army1label = QtGui.QLabel(self.centralwidget)
        self.army1label.setObjectName(_fromUtf8("army1label"))
        self.gridLayout.addWidget(self.army1label, 0, 1, 1, 1)
        self.footmen2line = QtGui.QLineEdit(self.centralwidget)
        self.footmen2line.setObjectName(_fromUtf8("footmen2line"))
        self.gridLayout.addWidget(self.footmen2line, 3, 4, 1, 1)
        self.startbattle = QtGui.QPushButton(self.centralwidget)
        self.startbattle.setObjectName(_fromUtf8("startbattle"))
        self.gridLayout.addWidget(self.startbattle, 8, 1, 1, 4)
        self.army2label = QtGui.QLabel(self.centralwidget)
        self.army2label.setObjectName(_fromUtf8("army2label"))
        self.gridLayout.addWidget(self.army2label, 0, 4, 1, 1)
        self.footmen1 = QtGui.QLabel(self.centralwidget)
        self.footmen1.setObjectName(_fromUtf8("footmen1"))
        self.gridLayout.addWidget(self.footmen1, 3, 0, 1, 1)
        self.knights1line = QtGui.QLineEdit(self.centralwidget)
        self.knights1line.setObjectName(_fromUtf8("knights1line"))
        self.gridLayout.addWidget(self.knights1line, 7, 1, 1, 1)
        self.pikemen1line = QtGui.QLineEdit(self.centralwidget)
        self.pikemen1line.setObjectName(_fromUtf8("pikemen1line"))
        self.gridLayout.addWidget(self.pikemen1line, 6, 1, 1, 1)
        self.knights2 = QtGui.QLabel(self.centralwidget)
        self.knights2.setObjectName(_fromUtf8("knights2"))
        self.gridLayout.addWidget(self.knights2, 7, 3, 1, 1)
        self.archers1line = QtGui.QLineEdit(self.centralwidget)
        self.archers1line.setObjectName(_fromUtf8("archers1line"))
        self.gridLayout.addWidget(self.archers1line, 4, 1, 1, 1)
        self.archers2line = QtGui.QLineEdit(self.centralwidget)
        self.archers2line.setObjectName(_fromUtf8("archers2line"))
        self.gridLayout.addWidget(self.archers2line, 4, 4, 1, 1)
        self.archers2 = QtGui.QLabel(self.centralwidget)
        self.archers2.setObjectName(_fromUtf8("archers2"))
        self.gridLayout.addWidget(self.archers2, 4, 3, 1, 1)
        self.calvary2line = QtGui.QLineEdit(self.centralwidget)
        self.calvary2line.setObjectName(_fromUtf8("calvary2line"))
        self.gridLayout.addWidget(self.calvary2line, 5, 4, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 2)
        self.army2name = QtGui.QLabel(self.centralwidget)
        self.army2name.setObjectName(_fromUtf8("army2name"))
        self.gridLayout.addWidget(self.army2name, 1, 3, 1, 1)
        self.army1line = QtGui.QLineEdit(self.centralwidget)
        self.army1line.setObjectName(_fromUtf8("army1line"))
        self.gridLayout.addWidget(self.army1line, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 2, 5, 1)
        self.army2line = QtGui.QLineEdit(self.centralwidget)
        self.army2line.setObjectName(_fromUtf8("army2line"))
        self.gridLayout.addWidget(self.army2line, 1, 4, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        self.army1name = QtGui.QLabel(self.centralwidget)
        self.army1name.setObjectName(_fromUtf8("army1name"))
        self.gridLayout.addWidget(self.army1name, 1, 0, 1, 1)
        self.pikemen2line = QtGui.QLineEdit(self.centralwidget)
        self.pikemen2line.setObjectName(_fromUtf8("pikemen2line"))
        self.gridLayout.addWidget(self.pikemen2line, 6, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 838, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.troopnames_action = QtGui.QAction(MainWindow)
        self.troopnames_action.setObjectName(_fromUtf8("troopnames_action"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.fileMenu.addAction(self.actionQuit)
        self.menuEdit.addAction(self.troopnames_action)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BattleManager 4", None))

        with open ("NameSettings__.txt") as f:
            lines = f.readlines()
            for line in lines:
                names = line.split()

        self.pikemen1.setText(_translate("MainWindow", names[3], None))
        self.footmen2.setText(_translate("MainWindow", names[5], None))
        self.calvary1.setText(_translate("MainWindow", names[2], None))
        self.archers1.setText(_translate("MainWindow", names[1], None))
        self.knights1.setText(_translate("MainWindow", names[4], None))
        self.calvary2.setText(_translate("MainWindow", names[7], None))
        self.pikemen2.setText(_translate("MainWindow", names[8], None))
        self.army1label.setText(_translate("MainWindow", "Army 1", None))
        self.startbattle.setText(_translate("MainWindow", "Start Battle", None))
        self.army2label.setText(_translate("MainWindow", "Army 2", None))
        self.footmen1.setText(_translate("MainWindow", names[0], None))
        self.knights2.setText(_translate("MainWindow", names[9], None))
        self.archers2.setText(_translate("MainWindow", names[6], None))
        self.army2name.setText(_translate("MainWindow", "Army 2 Name", None))
        self.army1name.setText(_translate("MainWindow", "Army1 Name", None))
        self.fileMenu.setTitle(_translate("MainWindow", "File", None))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit", None))
        self.troopnames_action.setText(_translate("MainWindow", "Troop Names", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

        self.startbattle.clicked.connect(self.warning)


        self.troopnames = self.troopnames_action
        self.troopnames.triggered.connect(self.help)
        self.actionQuit.triggered.connect(self.exit)

    def battle(self):
        a1name = str(self.army1line.text())
        if a1name == "":
            a1name = "Army 1"
            
        a2name = str(self.army1line.text())
        if a2name == "":
            a2name = "Army 2"

        f1 = int(self.footmen1line.text())
        a1 = int(self.archers1line.text())
        c1 = int(self.calvary1line.text())
        p1 = int(self.pikemen1line.text())
        k1 = int(self.knights1line.text())

        f2 = int(self.footmen2line.text())
        a2 = int(self.archers2line.text())
        c2 = int(self.calvary2line.text())
        p2 = int(self.pikemen2line.text())
        k2 = int(self.pikemen2line_2.text())
        print("I got here")
        
    def warning(self):
        warningBox = QtGui.QMessageBox.question(self, "Exit", "All Fields except for the army names must be filled out before executing the program. Are all fields filled out?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if warningBox == QtGui.QMessageBox.Yes:
            self.battle()
        else:
            pass

    def help(self):
        helpmenu = QtGui.QMessageBox.question(self, "Exit",
            "To edit the troopnames of the BattleManager you must edit the names in the txt file \"NameSettings__.txt\".\n\nWould you like to quit now to make these changes?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if helpmenu == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def exit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

