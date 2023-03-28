# -*- coding: utf-8 -*-

# Author: harnotcy
# Last Edit Date: 2023-03-13

from UI.About import *


class AboutWindow(QDialog, Ui_about_Dialog):
    def __init__(self, parent=None):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)
