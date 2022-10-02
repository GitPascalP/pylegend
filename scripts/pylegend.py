import json
import pathlib
from PyQt5 import QtCore, QtGui, QtWidgets
from pylegend_creator_mk2 import Ui_CreatorWindow
from pylegend_display_mk2 import Ui_DisplayWindow
from pylegend_configuration import Ui_ConfigWindow


class PyLegendCreator(QtWidgets.QMainWindow, Ui_CreatorWindow):
    """

    """
    def setupUi(self, CreatorWindow):
        super().setupUi(CreatorWindow)
        self.actionSave.triggered.connect(lambda: self.pressed_save_button())
        self.actionLoad.triggered.connect(lambda: self.pressed_load_button())
        self.actionSettings.triggered.connect(lambda: self.pressed_config_button())

        self.displaybutton.clicked.connect(self.pressed_display_button)
        self.clearbutton.clicked.connect(self.pressed_clear_button)
        self.closebutton.clicked.connect(self.pressed_close_button)

        self.config_window = None
        self.display_window = None
        self.update_stylesheet()
        self.legend_config = {}


    def pressed_save_button(self, ):
            """ save legend configuration on pressed button """
            self.read_configuration()
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
        self.read_configuration()
        self.open_display_window()
        self.set_display_properties()

    def pressed_clear_button(self, ):
        """ clear all text in QLineEdits """
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            field.clear()

    def pressed_config_button(self, ):
        """ set style parameters for legend display """
        self.config_window = QtWidgets.QMainWindow()
        self.configuration = Ui_ConfigWindow()
        self.configuration.setupUi(self.config_window)
        self.config_window.show()

    def pressed_close_button(self, ):
        """ clear all text in QLineEdits """
        if self.display_window is not None:
            self.display_window.close()
        if self.config_window is not None:
            self.config_window.close()
        self.close()
        #TODO fix close function / main window does not close

    def open_display_window(self, ):
        """ """
        self.display_window = QtWidgets.QMainWindow()
        self.display = Ui_DisplayWindow()
        self.display.setupUi(self.display_window)
        self.display_window.show()

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

    def read_configuration(self, ):
        """ """
        for field in self.centralwidget.findChildren(QtWidgets.QLineEdit):
            object_name = str(field.objectName())
            if "label" in object_name:
                self.legend_config[object_name] = field.text()
            elif "color" in object_name:
                self.legend_config[object_name] = field.text()
                if not field.text():
                    # set color to background color if not further specified
                    self.legend_config[object_name] = "rgba(255, 255, 255, 0)"


    def update_stylesheet(self, ):
        """ """

class PyLegendConfig(QtWidgets.QMainWindow, Ui_CreatorWindow):
    """

    """
    def setupUi(self, ConfigWindow):
        super().setupUi(ConfigWindow)

    def pressed_apply_button(self, ):
        pass

    def read_configuration(self, ):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreatorWindow = QtWidgets.QMainWindow()
    ui = PyLegendCreator()
    ui.setupUi(CreatorWindow)
    CreatorWindow.show()
    sys.exit(app.exec_())
