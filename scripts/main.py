import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

import legend_display


class LegendUI(QtWidgets.QMainWindow, legend_display.Ui_MainWindow):
    """ Class setting up and displaying the UI """
    def __init__(self, parent=None):
        super(LegendUI, self).__init__(parent)
        self.setupUi(self)


class LegendCtrl:
    """ Controller class handling the logic behind UI """
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.connect_signals()

    def connect_signals(self, ):
        """ """
        print('INIT')
        self.view.pushButton.clicked.connect(self.button_event)
        self.view.lineEdit.returnPressed.connect(self.button_event)

    def set_label(self, ):
        self.view.label.setText("TEXT")

    def button_event(self, ):
        self.view.lineEdit.setText("")
        self.view.lineEdit.setFocus()
        print("Button Clicked")


def ui_model():
    """ Logic behind UI """
    pass

def main():
    """ Main function """
    app = QApplication(sys.argv)
    # create and display UI
    ui = LegendUI()
    ui.show()
    # create instance for controller
    model = ui_model
    LegendCtrl(view=ui, model=model)
    # execute main interaction loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()