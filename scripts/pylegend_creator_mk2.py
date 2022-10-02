# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pylegend_creator_mk2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreatorWindow(object):
    def setupUi(self, CreatorWindow):
        CreatorWindow.setObjectName("CreatorWindow")
        CreatorWindow.resize(373, 427)
        self.centralwidget = QtWidgets.QWidget(CreatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLineEdit(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(30, 60, 131, 25))
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLineEdit(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 100, 131, 25))
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLineEdit(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(30, 140, 131, 25))
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLineEdit(self.centralwidget)
        self.label4.setGeometry(QtCore.QRect(30, 180, 131, 25))
        self.label4.setObjectName("label4")
        self.color4 = QtWidgets.QLineEdit(self.centralwidget)
        self.color4.setGeometry(QtCore.QRect(190, 180, 151, 25))
        self.color4.setObjectName("color4")
        self.color3 = QtWidgets.QLineEdit(self.centralwidget)
        self.color3.setGeometry(QtCore.QRect(190, 140, 151, 25))
        self.color3.setObjectName("color3")
        self.color1 = QtWidgets.QLineEdit(self.centralwidget)
        self.color1.setGeometry(QtCore.QRect(190, 60, 151, 25))
        self.color1.setObjectName("color1")
        self.color2 = QtWidgets.QLineEdit(self.centralwidget)
        self.color2.setGeometry(QtCore.QRect(190, 100, 151, 25))
        self.color2.setObjectName("color2")
        self.displaybutton = QtWidgets.QPushButton(self.centralwidget)
        self.displaybutton.setGeometry(QtCore.QRect(250, 330, 89, 25))
        self.displaybutton.setObjectName("displaybutton")
        self.color6 = QtWidgets.QLineEdit(self.centralwidget)
        self.color6.setGeometry(QtCore.QRect(190, 260, 151, 25))
        self.color6.setObjectName("color6")
        self.color5 = QtWidgets.QLineEdit(self.centralwidget)
        self.color5.setGeometry(QtCore.QRect(190, 220, 151, 25))
        self.color5.setObjectName("color5")
        self.label6 = QtWidgets.QLineEdit(self.centralwidget)
        self.label6.setGeometry(QtCore.QRect(30, 260, 131, 25))
        self.label6.setObjectName("label6")
        self.label5 = QtWidgets.QLineEdit(self.centralwidget)
        self.label5.setGeometry(QtCore.QRect(30, 220, 131, 25))
        self.label5.setObjectName("label5")
        self.labeltitle = QtWidgets.QLabel(self.centralwidget)
        self.labeltitle.setGeometry(QtCore.QRect(30, 30, 67, 17))
        self.labeltitle.setObjectName("labeltitle")
        self.colortitle = QtWidgets.QLabel(self.centralwidget)
        self.colortitle.setGeometry(QtCore.QRect(190, 30, 111, 17))
        self.colortitle.setObjectName("colortitle")
        self.clearbutton = QtWidgets.QPushButton(self.centralwidget)
        self.clearbutton.setGeometry(QtCore.QRect(30, 330, 89, 25))
        self.clearbutton.setObjectName("clearbutton")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(140, 330, 89, 25))
        self.closebutton.setObjectName("closebutton")
        CreatorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CreatorWindow)
        self.statusbar.setObjectName("statusbar")
        CreatorWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(CreatorWindow)
        self.toolBar.setObjectName("toolBar")
        CreatorWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(CreatorWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(CreatorWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSettings = QtWidgets.QAction(CreatorWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionLoad)
        self.toolBar.addAction(self.actionSettings)

        self.retranslateUi(CreatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CreatorWindow)

    def retranslateUi(self, CreatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CreatorWindow.setWindowTitle(_translate("CreatorWindow", "PyLegend Creator"))
        self.displaybutton.setText(_translate("CreatorWindow", "Display"))
        self.labeltitle.setText(_translate("CreatorWindow", "Label:"))
        self.colortitle.setText(_translate("CreatorWindow", "Color-Coding:"))
        self.clearbutton.setText(_translate("CreatorWindow", "Clear"))
        self.closebutton.setText(_translate("CreatorWindow", "Close"))
        self.toolBar.setWindowTitle(_translate("CreatorWindow", "toolBar"))
        self.actionSave.setText(_translate("CreatorWindow", "Save"))
        self.actionLoad.setText(_translate("CreatorWindow", "Load"))
        self.actionSettings.setText(_translate("CreatorWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreatorWindow = QtWidgets.QMainWindow()
    ui = Ui_CreatorWindow()
    ui.setupUi(CreatorWindow)
    CreatorWindow.show()
    sys.exit(app.exec_())
