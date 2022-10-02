import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisplayWindow(QtWidgets.QMainWindow):
    def setupUi(self, DisplayWindow):
        DisplayWindow.setObjectName("DisplayWindow")
        DisplayWindow.resize(222, 349)
        self.centralwidget = QtWidgets.QWidget(DisplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 131, 17))
        self.label.setObjectName("labeledit1")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 21, 21))
        self.lineEdit.setObjectName("coloredit1")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 21, 21))
        self.lineEdit_2.setObjectName("coloredit2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 131, 17))
        self.label_2.setObjectName("labeledit2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 21, 21))
        self.lineEdit_3.setObjectName("coloredit3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 17))
        self.label_3.setObjectName("labeledit3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 160, 21, 21))
        self.lineEdit_4.setObjectName("coloredit4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 131, 17))
        self.label_4.setObjectName("labeledit4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 131, 17))
        self.label_5.setObjectName("labeledit5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 190, 21, 21))
        self.lineEdit_5.setObjectName("coloredit5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 131, 17))
        self.label_6.setObjectName("labeledit6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 220, 21, 21))
        self.lineEdit_6.setObjectName("coloredit6")
        DisplayWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DisplayWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 222, 22))
        self.menubar.setObjectName("menubar")
        DisplayWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DisplayWindow)
        self.statusbar.setObjectName("statusbar")
        DisplayWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DisplayWindow)
        QtCore.QMetaObject.connectSlotsByName(DisplayWindow)

    def retranslateUi(self, DisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "Legend"))
        self.label.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_2.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_3.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_4.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_5.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_6.setText(_translate("DisplayWindow", "LegendDisplay"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     DisplayWindow = QtWidgets.QMainWindow()
#     ui = Ui_DisplayWindow()
#     ui.setupUi(DisplayWindow)
#     DisplayWindow.show()
#     sys.exit(app.exec_())
