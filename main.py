# -*- coding: utf-8 -*-

# Author: harnotcy
# Last Edit Date: 2023-03-13

import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import calc

# main函数入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("D:\Code\Qt\VentilationDuctResistanceCalculator\icon.ico"))  # 设置应用 window icon, 为了pyinstaller打包时正常，此处设定为绝对路径
    Win = calc.MainWindow()
    Win.show()
    sys.exit(app.exec())
