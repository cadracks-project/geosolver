# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'constraintdialog.ui'
#
# Created: Wed Oct 17 15:06:50 2007
#      by: PyQt4 UI code generator 4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConstraintDialog(object):
    def setupUi(self, ConstraintDialog):
        ConstraintDialog.setObjectName("ConstraintDialog")
        ConstraintDialog.resize(QtCore.QSize(QtCore.QRect(0,0,238,479).size()).expandedTo(ConstraintDialog.minimumSizeHint()))

        self.vboxlayout = QtWidgets.QVBoxLayout(ConstraintDialog)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtWidgets.QTabWidget(ConstraintDialog)
        self.tabWidget.setObjectName("tabWidget")

        self.selectionTab = QtWidgets.QWidget()
        self.selectionTab.setObjectName("selectionTab")

        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.selectionTab)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.treeWidget = QtWidgets.QTreeWidget(self.selectionTab)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setObjectName("treeWidget")
        self.vboxlayout1.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.selectionTab,"")

        self.editTab = QtWidgets.QWidget()
        self.editTab.setObjectName("editTab")

        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.editTab)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.stackedWidget = QtWidgets.QStackedWidget(self.editTab)
        self.stackedWidget.setObjectName("stackedWidget")

        self.pointEdit = QtWidgets.QWidget()
        self.pointEdit.setObjectName("pointEdit")
        self.stackedWidget.addWidget(self.pointEdit)
        self.vboxlayout2.addWidget(self.stackedWidget)
        self.tabWidget.addTab(self.editTab,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(ConstraintDialog)
        self.tabWidget.setCurrentIndex(1)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ConstraintDialog)

    def retranslateUi(self, ConstraintDialog):
        ConstraintDialog.setWindowTitle(QtWidgets.QApplication.translate("ConstraintDialog", "Form", None))
        self.tabWidget.setWhatsThis(QtWidgets.QApplication.translate("ConstraintDialog", "Edit of the different constraints and other objects", None))
        self.treeWidget.headerItem().setText(0,QtWidgets.QApplication.translate("ConstraintDialog", "column 1", None))
        self.treeWidget.clear()

        item = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item.setText(0,QtWidgets.QApplication.translate("ConstraintDialog", "Points", None))

        item1 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item1.setText(0,QtWidgets.QApplication.translate("ConstraintDialog", "Distances", None))

        item2 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item2.setText(0,QtWidgets.QApplication.translate("ConstraintDialog", "Angles", None))

        item3 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item3.setText(0,QtWidgets.QApplication.translate("ConstraintDialog", "Fixed Points", None))

        item4 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item4.setText(0,QtWidgets.QApplication.translate("ConstraintDialog", "Lines", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.selectionTab), QtWidgets.QApplication.translate("ConstraintDialog", "Se&lection", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.editTab), QtWidgets.QApplication.translate("ConstraintDialog", "E&dit", None))

