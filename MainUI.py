# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\Desktop\Codes\PCM_XYZ_Converter\GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GUI(object):
    def setupUi(self, GUI):
        GUI.setObjectName("GUI")
        GUI.resize(552, 206)
        self.layoutWidget = QtWidgets.QWidget(GUI)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 491, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.PCMLocation = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.PCMLocation.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.PCMLocation.setContentsMargins(0, 2, 0, 2)
        self.PCMLocation.setObjectName("PCMLocation")
        self.PCMLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCMLabel.sizePolicy().hasHeightForWidth())
        self.PCMLabel.setSizePolicy(sizePolicy)
        self.PCMLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PCMLabel.setObjectName("PCMLabel")
        self.PCMLocation.addWidget(self.PCMLabel)
        self.PCMBox = QtWidgets.QPlainTextEdit(self.layoutWidget)
        self.PCMBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PCMBox.sizePolicy().hasHeightForWidth())
        self.PCMBox.setSizePolicy(sizePolicy)
        self.PCMBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PCMBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PCMBox.setPlainText("")
        self.PCMBox.setObjectName("PCMBox")
        self.PCMLocation.addWidget(self.PCMBox)
        self.Choosefile = QtWidgets.QPushButton(self.layoutWidget)
        self.Choosefile.setObjectName("Choosefile")
        self.PCMLocation.addWidget(self.Choosefile)
        self.PCMLocation.setStretch(0, 1)
        self.PCMLocation.setStretch(1, 4)
        self.layoutWidget1 = QtWidgets.QWidget(GUI)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 70, 491, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Output = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Output.setContentsMargins(0, 2, 0, 2)
        self.Output.setObjectName("Output")
        self.OutputLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.OutputLabel.setEnabled(True)
        self.OutputLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OutputLabel.setObjectName("OutputLabel")
        self.Output.addWidget(self.OutputLabel)
        self.OutputBox = QtWidgets.QPlainTextEdit(self.layoutWidget1)
        self.OutputBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OutputBox.sizePolicy().hasHeightForWidth())
        self.OutputBox.setSizePolicy(sizePolicy)
        self.OutputBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.OutputBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.OutputBox.setObjectName("OutputBox")
        self.Output.addWidget(self.OutputBox)
        self.OutputB = QtWidgets.QPushButton(self.layoutWidget1)
        self.OutputB.setObjectName("OutputB")
        self.Output.addWidget(self.OutputB)
        self.Output.setStretch(1, 4)
        self.layoutWidget2 = QtWidgets.QWidget(GUI)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 120, 491, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.Prefix = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.Prefix.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.Prefix.setContentsMargins(0, 2, 0, 2)
        self.Prefix.setObjectName("Prefix")
        self.PrefixLabel = QtWidgets.QLabel(self.layoutWidget2)
        self.PrefixLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PrefixLabel.setObjectName("PrefixLabel")
        self.Prefix.addWidget(self.PrefixLabel)
        self.PrefixBox = QtWidgets.QPlainTextEdit(self.layoutWidget2)
        self.PrefixBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PrefixBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.PrefixBox.setObjectName("PrefixBox")
        self.Prefix.addWidget(self.PrefixBox)
        self.Prefix.setStretch(0, 1)
        self.Prefix.setStretch(1, 4)
        self.layoutWidget3 = QtWidgets.QWidget(GUI)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 150, 493, 51))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(150, 0, 150, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SaveButton = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setDefault(False)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout.addWidget(self.SaveButton)
        self.ExitButton = QtWidgets.QPushButton(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ExitButton.sizePolicy().hasHeightForWidth())
        self.ExitButton.setSizePolicy(sizePolicy)
        self.ExitButton.setObjectName("ExitButton")
        self.horizontalLayout.addWidget(self.ExitButton)

        self.retranslateUi(GUI)
        QtCore.QMetaObject.connectSlotsByName(GUI)

    def retranslateUi(self, GUI):
        _translate = QtCore.QCoreApplication.translate
        GUI.setWindowTitle(_translate("GUI", "PCMtoXYZ"))
        self.PCMLabel.setText(_translate("GUI", "PCM Location"))
        self.PCMBox.setToolTip(_translate("GUI", "ex)C:\\Users\\USER\\Desktop\\TEST2.pcm"))
        self.Choosefile.setText(_translate("GUI", "Open"))
        self.OutputLabel.setText(_translate("GUI", "Output Destination"))
        self.OutputBox.setToolTip(_translate("GUI", "ex) E:\\Data\\TPY9"))
        self.OutputB.setText(_translate("GUI", "Open"))
        self.PrefixLabel.setText(_translate("GUI", "File Prefix"))
        self.PrefixBox.setToolTip(_translate("GUI", "ex) MS_TPY9_A1_"))
        self.SaveButton.setText(_translate("GUI", "Save"))
        self.ExitButton.setText(_translate("GUI", "Exit"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GUI = QtWidgets.QDialog()
    ui = Ui_GUI()
    ui.setupUi(GUI)
    GUI.show()
    sys.exit(app.exec_())