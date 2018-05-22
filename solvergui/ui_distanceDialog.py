# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'distanceeditdialog.ui'
#
# Created: Sun Jul  8 17:49:57 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DistanceDialog(object):
    def setupUi(self, DistanceDialog):
        DistanceDialog.setObjectName("DistanceDialog")
        DistanceDialog.resize(QtCore.QSize(QtCore.QRect(0,0,220,473).size()).expandedTo(DistanceDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(DistanceDialog)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_6 = QtWidgets.QLabel(DistanceDialog)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))

        font = QtGui.QFont()
        font.setFamily("Sans Serif")
        font.setPointSize(13)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.vboxlayout.addWidget(self.label_6)

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_7 = QtWidgets.QLabel(DistanceDialog)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.hboxlayout.addWidget(self.label_7)

        spacerItem = QtWidgets.QSpacerItem(13,
                                           15,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.distanceName = QtWidgets.QLineEdit(DistanceDialog)
        self.distanceName.setObjectName("distanceName")
        self.hboxlayout.addWidget(self.distanceName)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.groupBox_3 = QtWidgets.QGroupBox(DistanceDialog)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setObjectName("groupBox_3")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtWidgets.QGridLayout()
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setSpacing(20)
        self.gridlayout.setObjectName("gridlayout")

        self.optionDistance = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.optionDistance.setDecimals(4)
        self.optionDistance.setMaximum(40000.0)
        self.optionDistance.setObjectName("optionDistance")
        self.gridlayout.addWidget(self.optionDistance,0,1,1,1)

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,0,0,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.DistanceFixed = QtWidgets.QCheckBox(self.groupBox_3)
        self.DistanceFixed.setMaximumSize(QtCore.QSize(250,16777215))
        self.DistanceFixed.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.DistanceFixed.setObjectName("DistanceFixed")
        self.hboxlayout1.addWidget(self.DistanceFixed)

        spacerItem1 = QtWidgets.QSpacerItem(40,
                                            20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout1.addLayout(self.hboxlayout1)
        self.vboxlayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QtWidgets.QGroupBox(DistanceDialog)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215,16777215))
        self.groupBox_4.setObjectName("groupBox_4")

        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.hboxlayout2.addWidget(self.label_10)

        self.infoDPoint1Name = QtWidgets.QLabel(self.groupBox_4)
        self.infoDPoint1Name.setObjectName("infoDPoint1Name")
        self.hboxlayout2.addWidget(self.infoDPoint1Name)
        self.vboxlayout2.addLayout(self.hboxlayout2)

        self.infoDPoint1Coords = QtWidgets.QLabel(self.groupBox_4)
        self.infoDPoint1Coords.setIndent(10)
        self.infoDPoint1Coords.setObjectName("infoDPoint1Coords")
        self.vboxlayout2.addWidget(self.infoDPoint1Coords)

        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.hboxlayout3.addWidget(self.label_12)

        self.infoDPoint2Name = QtWidgets.QLabel(self.groupBox_4)
        self.infoDPoint2Name.setObjectName("infoDPoint2Name")
        self.hboxlayout3.addWidget(self.infoDPoint2Name)
        self.vboxlayout2.addLayout(self.hboxlayout3)

        self.infoDPoint2Coords = QtWidgets.QLabel(self.groupBox_4)
        self.infoDPoint2Coords.setIndent(10)
        self.infoDPoint2Coords.setObjectName("infoDPoint2Coords")
        self.vboxlayout2.addWidget(self.infoDPoint2Coords)

        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setObjectName("label_9")
        self.hboxlayout4.addWidget(self.label_9)

        self.getRanges = QtWidgets.QPushButton(self.groupBox_4)
        self.getRanges.setObjectName("getRanges")
        self.hboxlayout4.addWidget(self.getRanges)
        self.vboxlayout2.addLayout(self.hboxlayout4)

        self.parRangeList = QtWidgets.QListWidget(self.groupBox_4)
        self.parRangeList.setObjectName("parRangeList")
        self.vboxlayout2.addWidget(self.parRangeList)
        self.vboxlayout.addWidget(self.groupBox_4)

        self.retranslateUi(DistanceDialog)
        QtCore.QMetaObject.connectSlotsByName(DistanceDialog)

    def retranslateUi(self, DistanceDialog):
        DistanceDialog.setWindowTitle(QtWidgets.QApplication.translate("DistanceDialog", "Form", None))
        self.label_6.setText(QtWidgets.QApplication.translate("DistanceDialog", "Distance", None))
        self.label_7.setText(QtWidgets.QApplication.translate("DistanceDialog", "Name:", None))
        self.groupBox_3.setTitle(QtWidgets.QApplication.translate("DistanceDialog", "Options", None))
        self.label_8.setText(QtWidgets.QApplication.translate("DistanceDialog", "Distance:", None))
        self.DistanceFixed.setText(QtWidgets.QApplication.translate("DistanceDialog", "Fixed", None))
        self.groupBox_4.setTitle(QtWidgets.QApplication.translate("DistanceDialog", "Info", None))
        self.label_10.setText(QtWidgets.QApplication.translate("DistanceDialog", "Point 1:", None))
        self.label_12.setText(QtWidgets.QApplication.translate("DistanceDialog", "Point 2:", None))
        self.label_9.setText(QtWidgets.QApplication.translate("DistanceDialog", "Range(s):", None))
        self.getRanges.setText(QtWidgets.QApplication.translate("DistanceDialog", "!", None))

