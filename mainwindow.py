from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def openGAWindow(self, MainWindow):
        from grindy_a_win import Ui_Grindy_A_Win
        self.GAwindow = QtWidgets.QMainWindow()
        self.ui = Ui_Grindy_A_Win()
        self.ui.setupUi(self.GAwindow)
        self.GAwindow.show()
        MainWindow.hide()

    def openFPWindow(self, MainWindow):
        from fp_a_win import Ui_FPWindow
        self.FPwindow = QtWidgets.QMainWindow()
        self.ui = Ui_FPWindow()
        self.ui.setupUi(self.FPwindow)
        self.FPwindow.show()
        MainWindow.hide()

    def openACWindow(self, MainWindow):
        from ac_a_win import Ui_ACWindow
        self.ACwindow = QtWidgets.QMainWindow()
        self.ui = Ui_ACWindow()
        self.ui.setupUi(self.ACwindow)
        self.ACwindow.show()
        MainWindow.hide()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 90, 615, 361))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.gridLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.GAPushButton = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.openGAWindow(MainWindow))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GAPushButton.sizePolicy().hasHeightForWidth())
        self.GAPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.GAPushButton.setFont(font)
        self.GAPushButton.setIconSize(QtCore.QSize(16, 16))
        self.GAPushButton.setObjectName("GAPushButton")
        self.verticalLayout.addWidget(self.GAPushButton)
        self.FPPushButton = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.openFPWindow(MainWindow))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FPPushButton.sizePolicy().hasHeightForWidth())
        self.FPPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.FPPushButton.setFont(font)
        self.FPPushButton.setObjectName("FPPushButton")
        self.verticalLayout.addWidget(self.FPPushButton)
        self.ACPushButton = QtWidgets.QPushButton(self.gridLayoutWidget, clicked=lambda: self.openACWindow(MainWindow))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ACPushButton.sizePolicy().hasHeightForWidth())
        self.ACPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.ACPushButton.setFont(font)
        self.ACPushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ACPushButton.setObjectName("ACPushButton")
        self.verticalLayout.addWidget(self.ACPushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
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
        self.GAPushButton.setText(_translate("MainWindow", "Жадный алгоритм"))
        self.FPPushButton.setText(_translate("MainWindow", "Полный перебор"))
        self.ACPushButton.setText(_translate("MainWindow", "Муравьиный алгоритм"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())