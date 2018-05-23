# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prefviews.ui'
#
# Created: Mon Oct 15 21:18:35 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_viewsForm(object):
    def setupUi(self, viewsForm):
        viewsForm.setObjectName("viewsForm")
        viewsForm.resize(QtCore.QSize(QtCore.QRect(0,0,439,453).size()).expandedTo(viewsForm.minimumSizeHint()))

        self.tabWidget = QtWidgets.QTabWidget(viewsForm)
        self.tabWidget.setGeometry(QtCore.QRect(9,9,421,431))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")

        self.compositionTab = QtWidgets.QWidget()
        self.compositionTab.setObjectName("compositionTab")

        self.treeGroupBox = QtWidgets.QGroupBox(self.compositionTab)
        self.treeGroupBox.setGeometry(QtCore.QRect(10,60,399,150))
        self.treeGroupBox.setMaximumSize(QtCore.QSize(16777215,150))
        self.treeGroupBox.setObjectName("treeGroupBox")

        self.label = QtWidgets.QLabel(self.treeGroupBox)
        self.label.setGeometry(QtCore.QRect(11,48,151,22))

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.alignTreeComboBox = QtWidgets.QComboBox(self.treeGroupBox)
        self.alignTreeComboBox.setGeometry(QtCore.QRect(120,50,93,22))
        self.alignTreeComboBox.setMaximumSize(QtCore.QSize(100,16777215))
        self.alignTreeComboBox.setObjectName("alignTreeComboBox")

        self.radioConnectionButton = QtWidgets.QRadioButton(self.treeGroupBox)
        self.radioConnectionButton.setGeometry(QtCore.QRect(120,90,56,23))
        self.radioConnectionButton.setMinimumSize(QtCore.QSize(0,0))
        self.radioConnectionButton.setObjectName("radioConnectionButton")

        self.label_2 = QtWidgets.QLabel(self.treeGroupBox)
        self.label_2.setGeometry(QtCore.QRect(10,80,85,41))

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.radioCurvedButton = QtWidgets.QRadioButton(self.treeGroupBox)
        self.radioCurvedButton.setGeometry(QtCore.QRect(190,90,67,23))
        self.radioCurvedButton.setMinimumSize(QtCore.QSize(0,0))
        self.radioCurvedButton.setObjectName("radioCurvedButton")

        self.label_10 = QtWidgets.QLabel(self.compositionTab)
        self.label_10.setGeometry(QtCore.QRect(10,10,399,30))
        self.label_10.setMaximumSize(QtCore.QSize(16777215,30))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(50)
        font.setBold(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.compositionTab,"")

        self.solutionTab = QtWidgets.QWidget()
        self.solutionTab.setObjectName("solutionTab")

        self.label_11 = QtWidgets.QLabel(self.solutionTab)
        self.label_11.setGeometry(QtCore.QRect(20,20,371,30))
        self.label_11.setMaximumSize(QtCore.QSize(16777215,30))

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(50)
        font.setBold(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.gridGroupBox = QtWidgets.QGroupBox(self.solutionTab)
        self.gridGroupBox.setGeometry(QtCore.QRect(20,290,371,93))
        self.gridGroupBox.setObjectName("gridGroupBox")

        self.gridlayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridlayout.setContentsMargins(9, 9, 9, 9)
        self.gridlayout.setObjectName("gridlayout")

        self.svGridHeightSpin = QtWidgets.QSpinBox(self.gridGroupBox)
        self.svGridHeightSpin.setEnabled(False)
        self.svGridHeightSpin.setMaximumSize(QtCore.QSize(60,16777215))
        self.svGridHeightSpin.setMinimum(1)
        self.svGridHeightSpin.setMaximum(999)
        self.svGridHeightSpin.setObjectName("svGridHeightSpin")
        self.gridlayout.addWidget(self.svGridHeightSpin,1,4,1,1)

        self.label_8 = QtWidgets.QLabel(self.gridGroupBox)

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,0,0,1,1)

        self.label_12 = QtWidgets.QLabel(self.gridGroupBox)

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridlayout.addWidget(self.label_12,1,0,1,1)

        self.label_13 = QtWidgets.QLabel(self.gridGroupBox)
        self.label_13.setMinimumSize(QtCore.QSize(100,0))
        self.label_13.setMaximumSize(QtCore.QSize(16777215,16777215))

        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridlayout.addWidget(self.label_13,1,3,1,1)

        self.svShowgrid = QtWidgets.QCheckBox(self.gridGroupBox)
        self.svShowgrid.setChecked(False)
        self.svShowgrid.setObjectName("svShowgrid")
        self.gridlayout.addWidget(self.svShowgrid,0,1,1,1)

        self.svGridWidthSpin = QtWidgets.QSpinBox(self.gridGroupBox)
        self.svGridWidthSpin.setEnabled(False)
        self.svGridWidthSpin.setMaximumSize(QtCore.QSize(60,16777215))
        self.svGridWidthSpin.setMinimum(1)
        self.svGridWidthSpin.setMaximum(999)
        self.svGridWidthSpin.setObjectName("svGridWidthSpin")
        self.gridlayout.addWidget(self.svGridWidthSpin,1,1,1,1)

        spacerItem = QtWidgets.QSpacerItem(20,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,1,2,1,1)

        self.colorsizeGroupBox = QtWidgets.QGroupBox(self.solutionTab)
        self.colorsizeGroupBox.setGeometry(QtCore.QRect(20,50,371,231))
        self.colorsizeGroupBox.setObjectName("colorsizeGroupBox")

        self.gridlayout1 = QtWidgets.QGridLayout(self.colorsizeGroupBox)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label_3 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridlayout1.addWidget(self.label_3,0,0,1,1)

        self.svPointClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.svPointClrButton.setMinimumSize(QtCore.QSize(80,0))
        self.svPointClrButton.setMaximumSize(QtCore.QSize(100,16777215))
        self.svPointClrButton.setFlat(False)
        self.svPointClrButton.setObjectName("svPointClrButton")
        self.gridlayout1.addWidget(self.svPointClrButton,0,1,1,1)

        self.svPointSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.svPointSizeSpin.setMaximumSize(QtCore.QSize(50,16777215))
        self.svPointSizeSpin.setMinimum(1)
        self.svPointSizeSpin.setObjectName("svPointSizeSpin")
        self.gridlayout1.addWidget(self.svPointSizeSpin,0,2,1,1)

        self.vPoint = QtWidgets.QCheckBox(self.colorsizeGroupBox)
        self.vPoint.setObjectName("vPoint")
        self.gridlayout1.addWidget(self.vPoint,0,3,1,1)

        self.label_14 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridlayout1.addWidget(self.label_14,1,0,1,1)

        self.svDistanceClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.svDistanceClrButton.setMaximumSize(QtCore.QSize(100,16777215))
        self.svDistanceClrButton.setFlat(False)
        self.svDistanceClrButton.setObjectName("svDistanceClrButton")
        self.gridlayout1.addWidget(self.svDistanceClrButton,1,1,1,1)

        self.svLineSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.svLineSizeSpin.setMaximumSize(QtCore.QSize(50,16777215))
        self.svLineSizeSpin.setMinimum(1)
        self.svLineSizeSpin.setObjectName("svLineSizeSpin")
        self.gridlayout1.addWidget(self.svLineSizeSpin,1,2,1,1)

        self.vLine = QtWidgets.QCheckBox(self.colorsizeGroupBox)
        self.vLine.setObjectName("vLine")
        self.gridlayout1.addWidget(self.vLine,1,3,1,1)

        self.label_9 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridlayout1.addWidget(self.label_9,2,0,1,1)

        self.svfPointClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.svfPointClrButton.setMaximumSize(QtCore.QSize(100,16777215))
        self.svfPointClrButton.setFlat(False)
        self.svfPointClrButton.setObjectName("svfPointClrButton")
        self.gridlayout1.addWidget(self.svfPointClrButton,2,1,1,1)

        self.svfPointSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.svfPointSizeSpin.setMaximumSize(QtCore.QSize(50,16777215))
        self.svfPointSizeSpin.setMinimum(1)
        self.svfPointSizeSpin.setObjectName("svfPointSizeSpin")
        self.gridlayout1.addWidget(self.svfPointSizeSpin,2,2,1,1)

        self.vfPoint = QtWidgets.QCheckBox(self.colorsizeGroupBox)
        self.vfPoint.setObjectName("vfPoint")
        self.gridlayout1.addWidget(self.vfPoint,2,3,1,1)

        self.label_4 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridlayout1.addWidget(self.label_4,3,0,1,1)

        self.svdConstraintClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.svdConstraintClrButton.setMaximumSize(QtCore.QSize(100,16777215))
        self.svdConstraintClrButton.setFlat(False)
        self.svdConstraintClrButton.setObjectName("svdConstraintClrButton")
        self.gridlayout1.addWidget(self.svdConstraintClrButton,3,1,1,1)

        self.svDistanceSizeSpin = QtWidgets.QSpinBox(self.colorsizeGroupBox)
        self.svDistanceSizeSpin.setMaximumSize(QtCore.QSize(50,16777215))
        self.svDistanceSizeSpin.setMinimum(1)
        self.svDistanceSizeSpin.setObjectName("svDistanceSizeSpin")
        self.gridlayout1.addWidget(self.svDistanceSizeSpin,3,2,1,1)

        self.vDistance = QtWidgets.QCheckBox(self.colorsizeGroupBox)
        self.vDistance.setObjectName("vDistance")
        self.gridlayout1.addWidget(self.vDistance,3,3,1,1)

        self.label_5 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridlayout1.addWidget(self.label_5,4,0,1,1)

        self.svAngleClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.svAngleClrButton.setMaximumSize(QtCore.QSize(100,16777215))
        self.svAngleClrButton.setFlat(False)
        self.svAngleClrButton.setObjectName("svAngleClrButton")
        self.gridlayout1.addWidget(self.svAngleClrButton,4,1,1,1)

        self.vAngle = QtWidgets.QCheckBox(self.colorsizeGroupBox)
        self.vAngle.setObjectName("vAngle")
        self.gridlayout1.addWidget(self.vAngle,4,3,1,1)

        self.label_7 = QtWidgets.QLabel(self.colorsizeGroupBox)

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridlayout1.addWidget(self.label_7,5,0,1,1)

        self.svBgClrButton = QtWidgets.QPushButton(self.colorsizeGroupBox)
        self.svBgClrButton.setMaximumSize(QtCore.QSize(100,16777215))
        self.svBgClrButton.setFlat(False)
        self.svBgClrButton.setObjectName("svBgClrButton")
        self.gridlayout1.addWidget(self.svBgClrButton,5,1,1,1)
        self.tabWidget.addTab(self.solutionTab,"")

        self.retranslateUi(viewsForm)
        self.tabWidget.setCurrentIndex(1)
        # QtCore.QObject.connect(self.svShowgrid,QtCore.
        #                        SIGNAL("toggled(bool)"),
        #                        self.svGridHeightSpin.setEnabled)
        self.svShowgrid.toggled.connect(self.svGridHeightSpin.setEnabled)
        # QtCore.QObject.connect(self.svShowgrid,
        #                        QtCore.SIGNAL("toggled(bool)"),
        #                        self.svGridWidthSpin.setEnabled)
        self.svShowgrid.toggled.connect(self.svGridWidthSpin.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(viewsForm)

    def retranslateUi(self, viewsForm):
        viewsForm.setWindowTitle(QtWidgets.QApplication.translate("viewsForm",
                                                                  "Form",
                                                                  None))
        self.treeGroupBox.setTitle(QtWidgets.QApplication.translate("viewsForm",
                                                                    "Tree Visualisation",
                                                                    None))
        self.label.setText(QtWidgets.QApplication.translate("viewsForm", "Alignment:", None))
        self.alignTreeComboBox.addItem(QtWidgets.QApplication.translate("viewsForm", "Top", None))
        self.alignTreeComboBox.addItem(QtWidgets.QApplication.translate("viewsForm", "Bottom", None))
        self.alignTreeComboBox.addItem(QtWidgets.QApplication.translate("viewsForm", "Right", None))
        self.alignTreeComboBox.addItem(QtWidgets.QApplication.translate("viewsForm", "Left", None))
        self.radioConnectionButton.setText(QtWidgets.QApplication.translate("viewsForm", "Lines", None))
        self.label_2.setText(QtWidgets.QApplication.translate("viewsForm", "Connection:", None))
        self.radioCurvedButton.setText(QtWidgets.QApplication.translate("viewsForm", "Curved", None))
        self.label_10.setText(QtWidgets.QApplication.translate("viewsForm", "Decomposition View Options", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.compositionTab), QtWidgets.QApplication.translate("viewsForm", "Decomposition", None))
        self.label_11.setText(QtWidgets.QApplication.translate("viewsForm", "Solution View Options", None))
        self.gridGroupBox.setTitle(QtWidgets.QApplication.translate("viewsForm", "Grid", None))
        self.svGridHeightSpin.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Height of one cell", None))
        self.label_8.setText(QtWidgets.QApplication.translate("viewsForm", "Show Grid:", None))
        self.label_12.setText(QtWidgets.QApplication.translate("viewsForm", "Width:", None))
        self.label_13.setText(QtWidgets.QApplication.translate("viewsForm", "Height:", None))
        self.svShowgrid.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Grid visibility", None))
        self.svGridWidthSpin.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Width of one cell", None))
        self.colorsizeGroupBox.setTitle(QtWidgets.QApplication.translate("viewsForm", "Color && Size && Visibility", None))
        self.label_3.setText(QtWidgets.QApplication.translate("viewsForm", "Point:", None))
        self.svPointClrButton.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Point color", None))
        self.svPointSizeSpin.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Radius of the point", None))
        self.label_14.setText(QtWidgets.QApplication.translate("viewsForm", "Line:", None))
        self.svDistanceClrButton.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Line color", None))
        self.svLineSizeSpin.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Radius of line", None))
        self.label_9.setText(QtWidgets.QApplication.translate("viewsForm", "Fixed Point Constraint:", None))
        self.svfPointClrButton.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Fixed point constraint color", None))
        self.svfPointSizeSpin.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Radius of the fixed point constraint", None))
        self.label_4.setText(QtWidgets.QApplication.translate("viewsForm", "Distance Constraint:", None))
        self.svdConstraintClrButton.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Distance constraint color", None))
        self.svDistanceSizeSpin.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Radius of distance constraint", None))
        self.label_5.setText(QtWidgets.QApplication.translate("viewsForm", "Angle Constraint:", None))
        self.svAngleClrButton.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Angle constraint color", None))
        self.label_7.setText(QtWidgets.QApplication.translate("viewsForm", "Background:", None))
        self.svBgClrButton.setToolTip(QtWidgets.QApplication.translate("viewsForm", "Background color", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.solutionTab), QtWidgets.QApplication.translate("viewsForm", "Solution", None))

