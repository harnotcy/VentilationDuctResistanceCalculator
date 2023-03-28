# -*- coding: utf-8 -*-

# Author: harnotcy
# Last Edit Date: 2023-03-13

from UI.Help import *


class HelpWindow(QDialog, Ui_help_Dialog):
    def __init__(self, parent=None):
        super(HelpWindow, self).__init__(parent)
        self.setupUi(self)
