import json
from PyQt5 import QtCore, QtGui, QtWidgets
from pylegend_display import Ui_DisplayWindow


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 426)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labeledit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledit1.setGeometry(QtCore.QRect(40, 60, 113, 25))
        self.labeledit1.setObjectName("labeledit1")
        self.labeledit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledit2.setGeometry(QtCore.QRect(40, 100, 113, 25))
        self.labeledit2.setObjectName("labeledit2")
        self.labeledit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledit3.setGeometry(QtCore.QRect(40, 140, 113, 25))
        self.labeledit3.setObjectName("labeledit3")
        self.labeledit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledit4.setGeometry(QtCore.QRect(40, 180, 113, 25))
        self.labeledit4.setObjectName("labeledit4")
        self.coloredit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.coloredit4.setGeometry(QtCore.QRect(170, 180, 111, 25))
        self.coloredit4.setObjectName("coloredit4")
        self.coloredit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.coloredit3.setGeometry(QtCore.QRect(170, 140, 111, 25))
        self.coloredit3.setObjectName("coloredit3")
        self.coloredit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.coloredit1.setGeometry(QtCore.QRect(170, 60, 111, 25))
        self.coloredit1.setObjectName("coloredit1")
        self.coloredit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.coloredit2.setGeometry(QtCore.QRect(170, 100, 111, 25))
        self.coloredit2.setObjectName("coloredit2")
        self.savebutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed_save_button())
        self.savebutton.setGeometry(QtCore.QRect(10, 330, 89, 25))
        self.savebutton.setObjectName("savebutton")
        self.loadbutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed_load_button())
        self.loadbutton.setGeometry(QtCore.QRect(120, 330, 89, 25))
        self.loadbutton.setObjectName("loadbutton")
        self.displaybutton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.pressed_display_button())
        self.displaybutton.setGeometry(QtCore.QRect(230, 330, 89, 25))
        self.displaybutton.setObjectName("displaybutton")
        self.coloredit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.coloredit6.setGeometry(QtCore.QRect(170, 260, 111, 25))
        self.coloredit6.setObjectName("coloredit6")
        self.coloredit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.coloredit5.setGeometry(QtCore.QRect(170, 220, 111, 25))
        self.coloredit5.setObjectName("coloredit5")
        self.labeledit6 = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledit6.setGeometry(QtCore.QRect(40, 260, 113, 25))
        self.labeledit6.setObjectName("labeledit6")
        self.labeledit5 = QtWidgets.QLineEdit(self.centralwidget)
        self.labeledit5.setGeometry(QtCore.QRect(40, 220, 113, 25))
        self.labeledit5.setObjectName("labeledit5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 111, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ QTDesigner created function """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.savebutton.setText(_translate("MainWindow", "Save"))
        self.loadbutton.setText(_translate("MainWindow", "Load"))
        self.displaybutton.setText(_translate("MainWindow", "Display"))
        self.label.setText(_translate("MainWindow", "Label:"))
        self.label_2.setText(_translate("MainWindow", "Color HexCode:"))

    def pressed_save_button(self, ):
        """ save legend configuration on pressed button """
        # read config parameters from text input
        config = {}
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            object_name = str(field.objectName())
            if "label" in object_name:
                config[object_name] = field.text()
            elif "color" in object_name:
                config[object_name] = field.text()

        print(config)

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,"Save Configuration","","json Files (*.json)"
            )
        if filename:
            with open(filename, 'w') as config_file:
                json.dump(config, config_file, indent=4, sort_keys=True)

    def pressed_load_button(self, ):
        """ load legend configuration on pressed button """
        # args: text displayed, dir opened, which files are displayed
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "Load Configuration", "","json Files (*.json)"
            )
        if filename:
            with open(filename) as config_file:
                config = json.load(config_file)

        # write config in legend display
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            object_name = str(field.objectName())
            field.setText(config[object_name])

    def pressed_display_button(self, ):
        """ display legend window on pressed button """
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DisplayWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def pressed_clear_button(self, ):
        """ clear all text in QLineEdits """
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            field.clear()
        #TODO add clear button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
