from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Grindy_A_Win(object):
    def start_GA(self):
        self.ga_data = self.textEdit.toPlainText()
        data = open("ga_data.txt", "w")
        data.write(self.ga_data)
        data.close()
        os.system("python grindy_a.py")
        sm = open("ga_data.txt", "r")
        self.label_3.setText("Результат: " + sm.read())
        sm.close()

    def return_to_main(self, GAWindow):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        GAWindow.hide()


    def setupUi(self, GAWindow):
        GAWindow.setObjectName("GAWindow")
        GAWindow.resize(798, 599)
        self.centralwidget = QtWidgets.QWidget(GAWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.return_to_main(GAWindow))
        self.returnButton.setGeometry(QtCore.QRect(20, 470, 160, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(40, 10, 721, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setAcceptDrops(False)
        self.label.setToolTipDuration(-1)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 470, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 210, 201, 241))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.start_GA())
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        GAWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(GAWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        GAWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(GAWindow)
        self.statusbar.setObjectName("statusbar")
        GAWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GAWindow)
        QtCore.QMetaObject.connectSlotsByName(GAWindow)

    def retranslateUi(self, GAWindow):
        _translate = QtCore.QCoreApplication.translate
        GAWindow.setWindowTitle(_translate("MainWindow", "Grindy Algorithm"))
        self.returnButton.setText(_translate("MainWindow", "Вернуться"))
        self.label.setText(_translate("MainWindow",
                                      "    Жадный алгоритм – алгоритм нахождения наикратчайшего расстояния путём выбора самого короткого, ещё не выбранного ребра, при условии, что оно не образует цикла с уже выбранными рёбрами."))
        self.label_2.setText(_translate("MainWindow", "Введите координаты вершин:"))
        self.label_3.setText(_translate("MainWindow", "Результат: "))
        self.pushButton.setText(_translate("MainWindow", "Запустить алгоритм"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    GAWindow = QtWidgets.QMainWindow()
    ui = Ui_Grindy_A_Win()
    ui.setupUi(GAWindow)
    GAWindow.show()
    sys.exit(app.exec_())

from mainwindow import Ui_MainWindow