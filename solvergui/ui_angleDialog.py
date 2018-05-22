# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'angleeditdialog.ui'
#
# Created: Wed Oct 17 14:06:10 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AngleDialog(object):
    def setupUi(self, AngleDialog):
        AngleDialog.setObjectName("AngleDialog")
        AngleDialog.resize(QtCore.QSize(QtCore.QRect(0,0,221,550).size()).expandedTo(AngleDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(AngleDialog)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_16 = QtWidgets.QLabel(AngleDialog)

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.vboxlayout.addWidget(self.label_16)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_15 = QtWidgets.QLabel(AngleDialog)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.hboxlayout.addWidget(self.label_15)

        spacerItem = QtWidgets.QSpacerItem(13,
                                           15,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.angleName = QtWidgets.QLineEdit(AngleDialog)
        self.angleName.setObjectName("angleName")
        self.hboxlayout.addWidget(self.angleName)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.groupBox_6 = QtWidgets.QGroupBox(AngleDialog)
        self.groupBox_6.setObjectName("groupBox_6")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setObjectName("label_17")
        self.hboxlayout1.addWidget(self.label_17)

        self.optionAngle = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.optionAngle.setDecimals(4)
        self.optionAngle.setMaximum(360.0)
        self.optionAngle.setObjectName("optionAngle")
        self.hboxlayout1.addWidget(self.optionAngle)
        self.vboxlayout1.addLayout(self.hboxlayout1)

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.angleFixed = QtWidgets.QCheckBox(self.groupBox_6)
        self.angleFixed.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.angleFixed.setObjectName("angleFixed")
        self.hboxlayout2.addWidget(self.angleFixed)

        spacerItem1 = QtWidgets.QSpacerItem(40,
                                            20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout2)
        self.vboxlayout.addWidget(self.groupBox_6)

        self.groupBox_5 = QtWidgets.QGroupBox(AngleDialog)
        self.groupBox_5.setObjectName("groupBox_5")

        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setObjectName("label_13")
        self.hboxlayout3.addWidget(self.label_13)

        self.infoAPoint1Name = QtWidgets.QLabel(self.groupBox_5)
        self.infoAPoint1Name.setObjectName("infoAPoint1Name")
        self.hboxlayout3.addWidget(self.infoAPoint1Name)
        self.vboxlayout2.addLayout(self.hboxlayout3)

        self.infoAPoint1Coords = QtWidgets.QLabel(self.groupBox_5)
        self.infoAPoint1Coords.setIndent(10)
        self.infoAPoint1Coords.setObjectName("infoAPoint1Coords")
        self.vboxlayout2.addWidget(self.infoAPoint1Coords)

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.label_14 = QtWidgets.QLabel(self.groupBox_5)
        self.label_14.setObjectName("label_14")
        self.hboxlayout4.addWidget(self.label_14)

        self.infoAPoint2Name = QtWidgets.QLabel(self.groupBox_5)
        self.infoAPoint2Name.setObjectName("infoAPoint2Name")
        self.hboxlayout4.addWidget(self.infoAPoint2Name)
        self.vboxlayout2.addLayout(self.hboxlayout4)

        self.infoAPoint2Coords = QtWidgets.QLabel(self.groupBox_5)
        self.infoAPoint2Coords.setIndent(10)
        self.infoAPoint2Coords.setObjectName("infoAPoint2Coords")
        self.vboxlayout2.addWidget(self.infoAPoint2Coords)

        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setObjectName("label_18")
        self.hboxlayout5.addWidget(self.label_18)

        self.infoAPoint3Name = QtWidgets.QLabel(self.groupBox_5)
        self.infoAPoint3Name.setObjectName("infoAPoint3Name")
        self.hboxlayout5.addWidget(self.infoAPoint3Name)
        self.vboxlayout2.addLayout(self.hboxlayout5)

        self.infoAPoint3Coords = QtWidgets.QLabel(self.groupBox_5)
        self.infoAPoint3Coords.setIndent(10)
        self.infoAPoint3Coords.setObjectName("infoAPoint3Coords")
        self.vboxlayout2.addWidget(self.infoAPoint3Coords)

        self.hboxlayout6 = QtWidgets.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")

        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setObjectName("label_11")
        self.hboxlayout6.addWidget(self.label_11)

        self.getRangesButton = QtWidgets.QPushButton(self.groupBox_5)
        self.getRangesButton.setObjectName("getRangesButton")
        self.hboxlayout6.addWidget(self.getRangesButton)
        self.vboxlayout2.addLayout(self.hboxlayout6)

        self.parRangeList = QtWidgets.QListWidget(self.groupBox_5)
        self.parRangeList.setObjectName("parRangeList")
        self.vboxlayout2.addWidget(self.parRangeList)
        self.vboxlayout.addWidget(self.groupBox_5)

        self.retranslateUi(AngleDialog)
        QtCore.QMetaObject.connectSlotsByName(AngleDialog)

    def retranslateUi(self, AngleDialog):
        AngleDialog.setWindowTitle(QtWidgets.QApplication.translate("AngleDialog", "Form", None))
        self.label_16.setText(QtWidgets.QApplication.translate("AngleDialog", "Angle", None))
        self.label_15.setText(QtWidgets.QApplication.translate("AngleDialog", "Name:", None))
        self.groupBox_6.setTitle(QtWidgets.QApplication.translate("AngleDialog", "Options", None))
        self.label_17.setText(QtWidgets.QApplication.translate("AngleDialog", "Angle:", None))
        self.angleFixed.setText(QtWidgets.QApplication.translate("AngleDialog", "Fixed", None))
        self.groupBox_5.setTitle(QtWidgets.QApplication.translate("AngleDialog", "Info", None))
        self.label_13.setText(QtWidgets.QApplication.translate("AngleDialog", "Point 1:", None))
        self.label_14.setText(QtWidgets.QApplication.translate("AngleDialog", "Point 2:", None))
        self.label_18.setText(QtWidgets.QApplication.translate("AngleDialog", "Point 3:", None))
        self.label_11.setText(QtWidgets.QApplication.translate("AngleDialog", "Range(s):", None))
        self.getRangesButton.setText(QtWidgets.QApplication.translate("AngleDialog", "!", None))

