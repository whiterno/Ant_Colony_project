from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_FPWindow(object):
    def start_FP(self):
        self.fp_data = self.textEdit.toPlainText()
        data = open("ga_data.txt", "w")
        data.write(self.fp_data)
        data.close()
        os.system("python fp_a.py")
        sm = open("ga_data.txt", "r")
        time = open('time.txt', "r")
        self.label_3.setText("Результат: " + sm.read())
        self.label_4.setText("Время работы: " + time.read())
        sm.close()

    def return_to_main(self, FPWindow):
        from mainwindow import Ui_MainWindow
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        FPWindow.hide()

    def setupUi(self, FPWindow):
        FPWindow.setObjectName("FPWindow")
        FPWindow.resize(798, 599)
        self.centralwidget = QtWidgets.QWidget(FPWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 771, 141))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.returnButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.return_to_main(FPWindow))
        self.returnButton.setGeometry(QtCore.QRect(20, 470, 160, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.returnButton.setFont(font)
        self.returnButton.setObjectName("returnButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(430, 210, 201, 241))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 470, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(430, 500, 270, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.start_FP())
        self.pushButton.setGeometry(QtCore.QRect(40, 280, 341, 101))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        FPWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FPWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 22))
        self.menubar.setObjectName("menubar")
        FPWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FPWindow)
        self.statusbar.setObjectName("statusbar")
        FPWindow.setStatusBar(self.statusbar)

        self.retranslateUi(FPWindow)
        QtCore.QMetaObject.connectSlotsByName(FPWindow)

    def retranslateUi(self, FPWindow):
        _translate = QtCore.QCoreApplication.translate
        FPWindow.setWindowTitle(_translate("FPWindow", "MainWindow"))
        self.label.setText(_translate("FPWindow",
                                      "    Полный перебор - метод поиска решения исчерпыванием всех возможных вариантов. Сложность полного перебора зависит от количества всех возможных решений задачи. Если пространство решений очень велико, то полный перебор может не дать результатов в течение нескольких лет или даже столетий."))
        self.label_2.setText(_translate("FPWindow", "Введите координаты вершин:"))
        self.returnButton.setText(_translate("FPWindow", "Вернуться"))
        self.label_3.setText(_translate("FPWindow", "Результат: "))
        self.label_4.setText(_translate("FPWindow", "Время работы: "))
        self.pushButton.setText(_translate("FPWindow", "Запустить алгоритм"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FPWindow = QtWidgets.QMainWindow()
    ui = Ui_FPWindow()
    ui.setupUi(FPWindow)
    FPWindow.show()
    sys.exit(app.exec_())
