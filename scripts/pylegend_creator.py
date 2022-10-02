import json
import pathlib
from PyQt5 import QtCore, QtGui, QtWidgets
from pylegend_display import Ui_DisplayWindow

#TODO Add close button
#TODO add loading default parameters/ config/ last config used
#TODO add setting style properties (darkmode, font, ..)
#TODO add opening default path to created config folder

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

        # Signals added not by QT-Designer
        self.displaybutton.clicked.connect(self.pressed_display_button)

        self.legend_config = {}
        self.background_color = "grey"
        self.background_color_str = "background-color: " + self.background_color + ";"
        self.setStyleSheet(self.background_color_str)

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
        self.read_legend_config()
        config_path = str(pathlib.Path.cwd().parents[0] / "config")
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(
            self,"save config to json file", config_path,"json Files (*.json)"
            )
        if filename:
            with open(filename, 'w') as config_file:
                json.dump(self.legend_config, config_file, indent=4, sort_keys=True)

    def pressed_load_button(self, ):
        """ load legend configuration on pressed button """
        config_path = str(pathlib.Path.cwd().parents[0] / "config")
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self, "load config file", config_path,"json Files (*.json)"
            )
        if filename:
            with open(filename) as config_file:
                self.legend_config = json.load(config_file)

        # write config in legend display
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            object_name = str(field.objectName())
            field.setText(self.legend_config[object_name])

    def pressed_display_button(self, ):
        """ display legend window on pressed button """
        self.read_legend_config()
        self.open_display_window()
        self.set_display_properties()


    def pressed_clear_button(self, ):
        """ clear all text in QLineEdits """
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            field.clear()
        #TODO add clear button

    def pressed_config_button(self, ):
        """ set style parameters for legend display """
        #TODO add functionality
        pass

    def open_display_window(self, ):
        """ """
        self.window = QtWidgets.QMainWindow()
        self.display = Ui_DisplayWindow()
        self.display.setupUi(self.window)
        self.window.show()

    def set_display_properties(self, ):
        """ """
        for label in self.display.centralwidget.findChildren(QtWidgets.QLabel):
            object_name = str(label.objectName())
            label.setText(self.legend_config[object_name])

        for field in self.display.centralwidget.findChildren(QtWidgets.QLineEdit):
            # set color of LineEdit field
            object_name = str(field.objectName())
            color_str = "background-color: " + str(self.legend_config[object_name])
            field.setStyleSheet(color_str)
            field.setEnabled(False)

    def read_legend_config(self, ):
        """ """
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            object_name = str(field.objectName())
            if "label" in object_name:
                self.legend_config[object_name] = field.text()
            elif "color" in object_name:
                self.legend_config[object_name] = field.text()
                if not field.text():
                    # set color to background color if not further specified
                    self.legend_config[object_name] = self.background_color


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
