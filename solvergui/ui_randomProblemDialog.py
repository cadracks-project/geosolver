# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/randomproblemdialog.ui'
#
# Created: Fri May 22 11:28:24 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_randomProblemDialog(object):
    def setupUi(self, randomProblemDialog):
        randomProblemDialog.setObjectName("randomProblemDialog")
        randomProblemDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        randomProblemDialog.resize(393, 288)
        self.buttonBox = QtWidgets.QDialogButtonBox(randomProblemDialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.numPointsSpinbox = QtGui.QSpinBox(randomProblemDialog)
        self.numPointsSpinbox.setGeometry(QtCore.QRect(260, 50, 61, 28))
        self.numPointsSpinbox.setProperty("value", QtCore.QVariant(10))
        self.numPointsSpinbox.setObjectName("numPointsSpinbox")
        self.ratioSpinbox = QtWidgets.QDoubleSpinBox(randomProblemDialog)
        self.ratioSpinbox.setGeometry(QtCore.QRect(260, 90, 62, 28))
        self.ratioSpinbox.setObjectName("ratioSpinbox")
        self.label = QtWidgets.QLabel(randomProblemDialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 101, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(randomProblemDialog)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 121, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(randomProblemDialog)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 371, 18))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(50)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.sizeSpinbox = QtWidgets.QDoubleSpinBox(randomProblemDialog)
        self.sizeSpinbox.setGeometry(QtCore.QRect(260, 130, 62, 28))
        self.sizeSpinbox.setMaximum(1000.0)
        self.sizeSpinbox.setProperty("value", QtCore.QVariant(100.0))
        self.sizeSpinbox.setObjectName("sizeSpinbox")
        self.label_4 = QtWidgets.QLabel(randomProblemDialog)
        self.label_4.setGeometry(QtCore.QRect(80, 100, 141, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(randomProblemDialog)
        self.label_5.setGeometry(QtCore.QRect(80, 180, 141, 18))
        self.label_5.setObjectName("label_5")
        self.roundingSpingbox = QtWidgets.QDoubleSpinBox(randomProblemDialog)
        self.roundingSpingbox.setGeometry(QtCore.QRect(260, 170, 62, 28))
        self.roundingSpingbox.setObjectName("roundingSpingbox")

        self.retranslateUi(randomProblemDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), randomProblemDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), randomProblemDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(randomProblemDialog)

    def retranslateUi(self, randomProblemDialog):
        randomProblemDialog.setWindowTitle(QtGui.QApplication.translate("randomProblemDialog", "Generate random problem", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label.setText(QtWidgets.QApplication.translate("randomProblemDialog", "Numer of points", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_2.setText(QtWidgets.QApplication.translate("randomProblemDialog", "Layout box size", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_3.setText(QtWidgets.QApplication.translate("randomProblemDialog", "Create a random, well-constrained probem", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_4.setText(QtWidgets.QApplication.translate("randomProblemDialog", "Distance to angle ratio", None, QtWidgets.QApplication.UnicodeUTF8))
        self.label_5.setText(QtWidgets.QApplication.translate("randomProblemDialog", "Position rounding", None, QtWidgets.QApplication.UnicodeUTF8))

