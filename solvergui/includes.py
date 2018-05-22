# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from constants import *
from commands import *

# check for the installation of PyOpenGL
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
except ImportError:
    app = QApplication(sys.argv)
    QMessageBox.critical(None,
                         "OpenGL grabber",
                         "PyOpenGL must be installed to run this example.",
                         QMessageBox.Ok | QMessageBox.Default,
                         QMessageBox.NoButton)
    sys.exit(1)
