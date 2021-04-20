# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Desktop\PCM_XYZ_Converter\Popup2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Err(object):
    def setupUi(self, Err):
        Err.setObjectName("Err")
        Err.resize(173, 77)
        self.label = QtWidgets.QLabel(Err)
        self.label.setGeometry(QtCore.QRect(10, 10, 161, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.OKButton_2 = QtWidgets.QPushButton(Err)
        self.OKButton_2.setGeometry(QtCore.QRect(50, 40, 75, 23))
        self.OKButton_2.setAutoDefault(False)
        self.OKButton_2.setDefault(True)
        self.OKButton_2.setObjectName("OKButton_2")

        self.retranslateUi(Err)
        QtCore.QMetaObject.connectSlotsByName(Err)

    def retranslateUi(self, Err):
        _translate = QtCore.QCoreApplication.translate
        Err.setWindowTitle(_translate("Err", "Error"))
        self.label.setText(_translate("Err", "ERROR : Input is empty"))
        self.OKButton_2.setText(_translate("Err", "OK"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Err = QtWidgets.QWidget()
    ui = Ui_Err()
    ui.setupUi(Err)
    Err.show()
    sys.exit(app.exec_())
