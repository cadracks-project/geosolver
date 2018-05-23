# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preferencesdialog.ui'
#
# Created: Tue May 22 16:27:12 2007
#      by: PyQt4 UI code generator 4.1.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_preferencesDialog(object):
    def setupUi(self, preferencesDialog):
        preferencesDialog.setObjectName("preferencesDialog")
        preferencesDialog.resize(QtCore.QSize(QtCore.QRect(0,
                                                           0,
                                                           593,
                                                           472).size()).expandedTo(preferencesDialog.minimumSizeHint()))

        self.hboxlayout = QtWidgets.QHBoxLayout(preferencesDialog)
        self.hboxlayout.setContentsMargins(9, 9, 9, 9)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setObjectName("hboxlayout")

        self.contentsWidget = QtWidgets.QListWidget(preferencesDialog)
        self.contentsWidget.setMaximumSize(QtCore.QSize(128, 16777215))
        self.contentsWidget.setObjectName("contentsWidget")
        self.hboxlayout.addWidget(self.contentsWidget)

        self.vboxlayout = QtWidgets.QVBoxLayout()
        self.vboxlayout.setContentsMargins(0, 0, 0, 0)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.pagesWidget = QtWidgets.QStackedWidget(preferencesDialog)
        self.pagesWidget.setObjectName("pagesWidget")

        self.vboxlayout.addWidget(self.pagesWidget)

        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setContentsMargins(0, 0, 0, 0)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setObjectName("hboxlayout1")

        spacerItem = QtWidgets.QSpacerItem(40,
                                           20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)

        self.closeButton = QtWidgets.QPushButton(preferencesDialog)
        self.closeButton.setObjectName("closeButton")
        self.hboxlayout1.addWidget(self.closeButton)

        spacerItem1 = QtWidgets.QSpacerItem(40,20,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(preferencesDialog)
        self.pagesWidget.setCurrentIndex(0)
        # QtCore.QObject.connect(self.closeButton,
        #                        QtCore.SIGNAL("clicked()"),
        #                        preferencesDialog.close)
        self.closeButton.clicked.connect(preferencesDialog.close)
        QtCore.QMetaObject.connectSlotsByName(preferencesDialog)

    def retranslateUi(self, preferencesDialog):
        preferencesDialog.setWindowTitle(QtWidgets.QApplication.translate("preferencesDialog",
                                                                          "Dialog",
                                                                          None))
        self.closeButton.setText(QtWidgets.QApplication.translate("preferencesDialog",
                                                                  "&Close",
                                                                  None))
