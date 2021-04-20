# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Desktop\PCM_XYZ_Converter\Popup1.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Complete(object):
    def setupUi(self, Complete):
        Complete.setObjectName("Complete")
        Complete.resize(159, 70)
        self.OKButton = QtWidgets.QPushButton(Complete)
        self.OKButton.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.OKButton.setAutoDefault(False)
        self.OKButton.setDefault(True)
        self.OKButton.setObjectName("OKButton")
        self.label = QtWidgets.QLabel(Complete)
        self.label.setGeometry(QtCore.QRect(0, 10, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Complete)
        QtCore.QMetaObject.connectSlotsByName(Complete)

    def retranslateUi(self, Complete):
        _translate = QtCore.QCoreApplication.translate
        Complete.setWindowTitle(_translate("Complete", "Complete"))
        self.OKButton.setText(_translate("Complete", "OK"))
        self.label.setText(_translate("Complete", "Conversion Complete"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Complete = QtWidgets.QWidget()
    ui = Ui_Complete()
    ui.setupUi(Complete)
    Complete.show()
    sys.exit(app.exec_())
