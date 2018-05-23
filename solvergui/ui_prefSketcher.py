# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prefsketcher.ui'
#
# Created: Tue May 22 11:24:42 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sketcherForm(object):
    def setupUi(self, sketcherForm):
        sketcherForm.setObjectName("sketcherForm")
        sketcherForm.resize(QtCore.QSize(QtCore.QRect(0, 0, 439, 417).size()).expandedTo(sketcherForm.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(sketcherForm)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_10 = QtWidgets.QLabel(sketcherForm)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))

        font = QtGui.QFont(self.label_10.font())
        font.setPointSize(16)
        font.setWeight(50)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.vboxlayout.addWidget(self.label_10)

        self.colorsizeGroupBox = QtWidgets.QGroupBox(sketcherForm)
        self.colorsizeGroupBox.setObjectName("colorsizeGroupBox")

        self.gridlayout = QtWidgets.QGridLayout(self.colorsizeGroupBox)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label_3.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.fPointClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.fPointClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.fPointClrButton.setFlat(False)
        self.fPointClrButton.setObjectName("fPointClrButton")
        self.gridlayout.addWidget(self.fPointClrButton, 2, 1, 1, 1)

        self.fPointSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.fPointSizeSpin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fPointSizeSpin.setMinimum(1)
        self.fPointSizeSpin.setObjectName("fPointSizeSpin")
        self.gridlayout.addWidget(self.fPointSizeSpin, 2, 2, 1, 1)

        self.dConstraintClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.dConstraintClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.dConstraintClrButton.setFlat(False)
        self.dConstraintClrButton.setObjectName("dConstraintClrButton")
        self.gridlayout.addWidget(self.dConstraintClrButton, 3, 1, 1, 1)

        self.angleClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.angleClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.angleClrButton.setFlat(False)
        self.angleClrButton.setObjectName("angleClrButton")
        self.gridlayout.addWidget(self.angleClrButton, 4, 1, 1, 1)

        self.label_7 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label_7.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label_6.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridlayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.selectClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.selectClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.selectClrButton.setFlat(False)
        self.selectClrButton.setObjectName("selectClrButton")
        self.gridlayout.addWidget(self.selectClrButton, 5, 1, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label_4.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.distanceSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.distanceSizeSpin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.distanceSizeSpin.setMinimum(0)
        self.distanceSizeSpin.setObjectName("distanceSizeSpin")
        self.gridlayout.addWidget(self.distanceSizeSpin, 3, 2, 1, 1)

        self.distanceClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.distanceClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.distanceClrButton.setFlat(False)
        self.distanceClrButton.setObjectName("distanceClrButton")
        self.gridlayout.addWidget(self.distanceClrButton, 1, 1, 1, 1)

        self.label_5 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label_5.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont(self.label_2.font())
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.bgClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.bgClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.bgClrButton.setFlat(False)
        self.bgClrButton.setObjectName("bgClrButton")
        self.gridlayout.addWidget(self.bgClrButton, 6, 1, 1, 1)

        self.pointClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.pointClrButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pointClrButton.setFlat(False)
        self.pointClrButton.setObjectName("pointClrButton")
        self.gridlayout.addWidget(self.pointClrButton, 0, 1, 1, 1)

        self.pointSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.pointSizeSpin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pointSizeSpin.setMinimum(1)
        self.pointSizeSpin.setObjectName("pointSizeSpin")
        self.gridlayout.addWidget(self.pointSizeSpin, 0, 2, 1, 1)

        self.lineSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.lineSizeSpin.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineSizeSpin.setMinimum(0)
        self.lineSizeSpin.setObjectName("lineSizeSpin")
        self.gridlayout.addWidget(self.lineSizeSpin, 1, 2, 1, 1)
        self.vboxlayout.addWidget(self.colorsizeGroupBox)

        self.gridGroupBox = QtWidgets.QGroupBox(sketcherForm)
        self.gridGroupBox.setObjectName("gridGroupBox")

        self.gridlayout1 = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridlayout1.setContentsMargins(9, 9, 9, 9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")

        self.gridHeightSpin = QtWidgets.QSpinBox(self.gridGroupBox)
        self.gridHeightSpin.setEnabled(False)
        self.gridHeightSpin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridHeightSpin.setMaximum(999)
        self.gridHeightSpin.setMinimum(1)
        self.gridHeightSpin.setObjectName("gridHeightSpin")
        self.gridlayout1.addWidget(self.gridHeightSpin, 1, 4, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.gridGroupBox)

        font = QtGui.QFont(self.label_8.font())
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridlayout1.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_11 = QtWidgets.QLabel(self.gridGroupBox)

        font = QtGui.QFont(self.label_11.font())
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridlayout1.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QtWidgets.QLabel(self.gridGroupBox)
        self.label_12.setMinimumSize(QtCore.QSize(100, 0))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 16777215))

        font = QtGui.QFont(self.label_12.font())
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridlayout1.addWidget(self.label_12, 1, 3, 1, 1)

        self.showgridCheckBox = QtWidgets.QCheckBox(self.gridGroupBox)
        self.showgridCheckBox.setChecked(False)
        self.showgridCheckBox.setObjectName("showgridCheckBox")
        self.gridlayout1.addWidget(self.showgridCheckBox, 0, 1, 1, 1)

        self.gridWidthSpin = QtWidgets.QSpinBox(self.gridGroupBox)
        self.gridWidthSpin.setEnabled(False)
        self.gridWidthSpin.setMaximumSize(QtCore.QSize(60, 16777215))
        self.gridWidthSpin.setMaximum(999)
        self.gridWidthSpin.setMinimum(1)
        self.gridWidthSpin.setObjectName("gridWidthSpin")
        self.gridlayout1.addWidget(self.gridWidthSpin, 1, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20,
                                           20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.gridlayout1.addItem(spacerItem, 1, 2, 1, 1)
        self.vboxlayout.addWidget(self.gridGroupBox)

        self.retranslateUi(sketcherForm)
        # QtCore.QObject.connect(self.showgridCheckBox,QtCore.SIGNAL("toggled(bool)"),self.gridWidthSpin.setEnabled)
        # QtCore.QObject.connect(self.showgridCheckBox,QtCore.SIGNAL("toggled(bool)"),self.gridHeightSpin.setEnabled)
        self.showgridCheckBox.toggled.connect(self.gridWidthSpin.setEnabled)
        self.showgridCheckBox.toggled.connect(self.gridHeightSpin.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(sketcherForm)

    def retranslateUi(self, sketcherForm):
        sketcherForm.setWindowTitle(QtWidgets.QApplication.translate("sketcherForm", "Form", None))
        self.label_10.setText(QtWidgets.QApplication.translate("sketcherForm", "Sketcher Options", None))
        self.colorsizeGroupBox.setTitle(QtWidgets.QApplication.translate("sketcherForm", "Color && Size", None))
        self.label.setText(QtWidgets.QApplication.translate("sketcherForm", "Point:", None))
        self.label_3.setText(QtWidgets.QApplication.translate("sketcherForm", "Distance Constraint:", None))
        self.fPointClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Fixed point constraint color", None))
        self.fPointSizeSpin.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Radius of the fixed point constraint", None))
        self.dConstraintClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Distance constraint color", None))
        self.angleClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Angle constraint color", None))
        self.label_7.setText(QtWidgets.QApplication.translate("sketcherForm", "Background:", None))
        self.label_6.setText(QtWidgets.QApplication.translate("sketcherForm", "Selection:", None))
        self.selectClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Selection color", None))
        self.label_4.setText(QtWidgets.QApplication.translate("sketcherForm", "Angle Constraint:", None))
        self.distanceSizeSpin.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Radius of distance constraint", None))
        self.distanceClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Line color", None))
        self.label_5.setText(QtWidgets.QApplication.translate("sketcherForm", "Fixed Point Constraint:", None))
        self.label_2.setText(QtWidgets.QApplication.translate("sketcherForm", "Line:", None))
        self.bgClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Background color", None))
        self.pointClrButton.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Point color", None))
        self.pointSizeSpin.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Radius of the point", None))
        self.lineSizeSpin.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Radius of line", None))
        self.gridGroupBox.setTitle(QtWidgets.QApplication.translate("sketcherForm", "Grid", None))
        self.gridHeightSpin.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Height of one cell", None))
        self.label_8.setText(QtWidgets.QApplication.translate("sketcherForm", "Show Grid:", None))
        self.label_11.setText(QtWidgets.QApplication.translate("sketcherForm", "Width:", None))
        self.label_12.setText(QtWidgets.QApplication.translate("sketcherForm", "Height:", None))
        self.showgridCheckBox.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Grid visibility", None))
        self.gridWidthSpin.setToolTip(QtWidgets.QApplication.translate("sketcherForm", "Width of one cell", None))
