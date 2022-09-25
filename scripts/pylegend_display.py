import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DisplayWindow(QtWidgets.QMainWindow):
    def setupUi(self, DisplayWindow, legend_config):
        DisplayWindow.setObjectName("DisplayWindow")
        DisplayWindow.resize(222, 349)
        self.centralwidget = QtWidgets.QWidget(DisplayWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 131, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 70, 21, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 100, 21, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 131, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 130, 21, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 131, 17))
        self.label_3.setObjectName("label_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 160, 21, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 131, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 131, 17))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 190, 21, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 131, 17))
        self.label_6.setObjectName("label_6")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(160, 220, 21, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
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

        # not QtDesinger created
        self.legend_config = legend_config

    def retranslateUi(self, DisplayWindow):
        _translate = QtCore.QCoreApplication.translate
        DisplayWindow.setWindowTitle(_translate("DisplayWindow", "MainWindow"))
        self.label.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_2.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_3.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_4.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_5.setText(_translate("DisplayWindow", "LegendDisplay"))
        self.label_6.setText(_translate("DisplayWindow", "LegendDisplay"))

    #@qtc.pyqtSlot(list, list)
    # def update_legend(self, label_list, color_list)
    def update_legend(self, ):
        """ set labels, textboxes, etc of ui """
        print(self.legend_config)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DisplayWindow = QtWidgets.QMainWindow()
    ui = Ui_DisplayWindow()
    ui.setupUi(DisplayWindow)
    DisplayWindow.show()
    sys.exit(app.exec_())
