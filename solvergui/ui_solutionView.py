# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'solutionview.ui'
#
# Created: Wed Feb 28 10:52:09 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SolutionView(object):
    def setupUi(self, SolutionView):
        SolutionView.setObjectName("SolutionView")
        SolutionView.resize(QtCore.QSize(QtCore.QRect(0,0,614,527).size()).expandedTo(SolutionView.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(SolutionView)
        self.vboxlayout.setContentsMargins(4, 4, 4, 4)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.moveButton = QtWidgets.QToolButton(SolutionView)
        self.moveButton.setCheckable(True)
        self.moveButton.setAutoExclusive(True)
        self.moveButton.setObjectName("moveButton")
        self.hboxlayout.addWidget(self.moveButton)

        self.zoomButton = QtWidgets.QToolButton(SolutionView)
        self.zoomButton.setCheckable(True)
        self.zoomButton.setAutoExclusive(True)
        self.zoomButton.setObjectName("zoomButton")
        self.hboxlayout.addWidget(self.zoomButton)

        self.rotateButton = QtWidgets.QToolButton(SolutionView)
        self.rotateButton.setCheckable(True)
        self.rotateButton.setAutoExclusive(True)
        self.rotateButton.setObjectName("rotateButton")
        self.hboxlayout.addWidget(self.rotateButton)

        self.syncButton = QtWidgets.QToolButton(SolutionView)
        self.syncButton.setObjectName("syncButton")
        self.hboxlayout.addWidget(self.syncButton)

        spacerItem = QtWidgets.QSpacerItem(40,
                                           20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.actionZoom = QtWidgets.QAction(SolutionView)
        self.actionZoom.setObjectName("actionZoom")

        self.actionMove = QtWidgets.QAction(SolutionView)
        self.actionMove.setObjectName("actionMove")

        self.actionRotate = QtWidgets.QAction(SolutionView)
        self.actionRotate.setObjectName("actionRotate")

        self.actionSync = QtWidgets.QAction(SolutionView)
        self.actionSync.setObjectName("actionSync")

        self.retranslateUi(SolutionView)
        QtCore.QMetaObject.connectSlotsByName(SolutionView)

    def retranslateUi(self, SolutionView):
        SolutionView.setWindowTitle(QtWidgets.QApplication.translate("SolutionView", "Solution View", None))
        self.moveButton.setText(QtWidgets.QApplication.translate("SolutionView", "Move", None))
        self.zoomButton.setText(QtWidgets.QApplication.translate("SolutionView", "Zoom", None))
        self.rotateButton.setText(QtWidgets.QApplication.translate("SolutionView", "Rotate", None))
        self.syncButton.setText(QtWidgets.QApplication.translate("SolutionView", "Sync", None))
        self.actionZoom.setText(QtWidgets.QApplication.translate("SolutionView", "zoom", None))
        self.actionMove.setText(QtWidgets.QApplication.translate("SolutionView", "move", None))
        self.actionRotate.setText(QtWidgets.QApplication.translate("SolutionView", "rotate", None))
        self.actionSync.setText(QtWidgets.QApplication.translate("SolutionView", "sync",None))

