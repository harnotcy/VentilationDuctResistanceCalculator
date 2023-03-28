# -*- coding: utf-8 -*-

# Author: harnotcy
# Last Edit Date: 2023-03-14

import math
from UI.MainWindow import *
from aboutpage import AboutWindow
from helppage import HelpWindow


# 计算器主窗口
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 设置输入输出的全部 QLineEdit 默认为不可用状态
        self.roundTubeDiameter_inPut_lineEdit.setEnabled(False)
        self.squareTubeLength_inPut_lineEdit.setEnabled(False)
        self.squareTubeWidth_inPut_lineEdit.setEnabled(False)
        self.airVolume_inPut_lineEdit.setEnabled(False)
        self.pipeLength_inPut_lineEdit.setEnabled(False)
        self.flowRate_outPut_lineEdit.setEnabled(False)
        self.airVolume_outPut_lineEdit.setEnabled(False)
        self.roundTubeDiameter_outPut_lineEdit.setEnabled(False)
        self.squareTubeLength_outPut_lineEdit.setEnabled(False)
        self.squareTubeWidth_outPut_lineEdit.setEnabled(False)
        self.bimodalResistance_pa_outPut_lineEdit.setEnabled(False)
        self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(False)
        self.totalRistance_pa_outPut_lineEdit.setEnabled(False)
        self.totalRistance_h2o_outPut_lineEdit.setEnabled(False)

        # 设置输出区的 QLineEdit 为只读
        self.flowRate_outPut_lineEdit.setReadOnly(True)
        self.airVolume_outPut_lineEdit.setReadOnly(True)
        self.roundTubeDiameter_outPut_lineEdit.setReadOnly(True)
        self.squareTubeLength_outPut_lineEdit.setReadOnly(True)
        self.squareTubeWidth_outPut_lineEdit.setReadOnly(True)
        self.bimodalResistance_pa_outPut_lineEdit.setReadOnly(True)
        self.bimodalResistance_h2o_outPut_lineEdit.setReadOnly(True)
        self.totalRistance_pa_outPut_lineEdit.setReadOnly(True)
        self.totalRistance_h2o_outPut_lineEdit.setReadOnly(True)

        # 设置选择圆形管的 QRadioBottom 时，输入直径和风量的 QLineEdit 可用，使用自定义槽函数roundchoose()
        self.connect_roundchoose = self.roundTube_radioButton.toggled.connect(
            self.roundchoose
        )

        # 设置选择矩形管的 QRadioBottom 时，输入长宽和风量的 QLineEdit 可用，使用自定义槽函数squarechoose()
        self.connect_squarechoose = self.squareTube_radioButton.toggled.connect(
            self.squarechoose
        )

        # 设置选择管段长度的 QCheckBox 时，输入管段长度的 QLineEdit 可用
        self.pipeLength_checkBox.toggled.connect(
            self.pipeLength_inPut_lineEdit.setEnabled
        )

        # 设置清除键功能，使用自定义的槽函数clearlineedit()
        self.connect_resultremove = self.resultClear_pushButton.clicked.connect(
            self.clearlineedit
        )

        # 设置计算键功能,，使用自定义的槽函数choosecalc()
        self.connect1_calculate = self.calculate_pushButton.clicked.connect(
            self.choosecalc
        )

        # 设置退出键功能
        self.exec_pushButton.clicked.connect(self.close)

        # 设置帮助键功能
        connect_help = self.help_pushButton.clicked.connect(self.showhelp)

        # 设置关于键功能
        connect_about = self.about_pushButton.clicked.connect(self.showabout)


    # 计算键接收函数，实现计算功能
    def choosecalc(self):
        print("choosecalc函数调用")
        # 圆形管阻力计算
        if self.roundTube_radioButton.isChecked():
            # 圆形管有长度
            if self.pipeLength_checkBox.isChecked():
                # print("圆管有长度")
                # 设置相关输出的 QLineEdit 可用
                self.flowRate_outPut_lineEdit.setEnabled(True)
                self.airVolume_outPut_lineEdit.setEnabled(True)
                self.roundTubeDiameter_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_pa_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(True)
                self.totalRistance_pa_outPut_lineEdit.setEnabled(True)
                self.totalRistance_h2o_outPut_lineEdit.setEnabled(True)
                # 获取输入数据
                diameter = self.roundTubeDiameter_inPut_lineEdit.text()
                airvolume = self.airVolume_inPut_lineEdit.text()
                pipelength = self.pipeLength_inPut_lineEdit.text()
                # 计算
                radius = float(diameter) * 0.001 * 0.5  # 将输入的毫米为单位的直径换算成米并获取半径
                airflowrate = float(airvolume) / (math.pi * pow(radius, 2))  # 计算流速
                renolds = (airflowrate * radius * 2) / 0.0000150  # 计算雷诺数
                f = 64 / renolds  # 摩擦系数
                pressurelose = (f * pow(airflowrate, 2) * 1.2) / (4 * radius)  # 阻力损失
                bimodalresistancepa = pressurelose  # 比摩阻
                totalristancepa = pressurelose * float(pipelength) * 0.001  # 总阻力
                bimodalresistanceh2o = bimodalresistancepa * 0.101972  # 比摩阻毫米水柱
                totalristanceh2o = totalristancepa * 0.101972  # 总阻力毫米水柱
                # 输出计算结果
                self.flowRate_outPut_lineEdit.setText(str(airflowrate))
                self.airVolume_outPut_lineEdit.setText(str(airvolume))
                self.roundTubeDiameter_outPut_lineEdit.setText(str(diameter))
                self.bimodalResistance_pa_outPut_lineEdit.setText(
                    str(bimodalresistancepa)
                )
                self.bimodalResistance_h2o_outPut_lineEdit.setText(
                    str(bimodalresistanceh2o)
                )
                self.totalRistance_pa_outPut_lineEdit.setText(str(totalristancepa))
                self.totalRistance_h2o_outPut_lineEdit.setText(str(totalristanceh2o))
            # 圆形管无长度
            else:
                # print("圆管无长度")
                # 设置相关输出的 QLineEdit 可用
                self.flowRate_outPut_lineEdit.setEnabled(True)
                self.airVolume_outPut_lineEdit.setEnabled(True)
                self.roundTubeDiameter_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_pa_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(True)
                # 获取输入数据
                diameter = self.roundTubeDiameter_inPut_lineEdit.text()
                airvolume = self.airVolume_inPut_lineEdit.text()
                # 计算
                radius = float(diameter) * 0.001 * 0.5  # 将输入的毫米为单位的直径换算成米并获取半径
                airflowrate = float(airvolume) / (math.pi * pow(radius, 2))  # 计算流速
                renolds = (airflowrate * radius * 2) / 0.0000150  # 计算雷诺数
                f = 64 / renolds  # 摩擦系数
                pressurelose = (f * pow(airflowrate, 2) * 1.2) / (4 * radius)  # 阻力损失
                bimodalresistancepa = pressurelose  # 比摩阻
                bimodalresistanceh2o = bimodalresistancepa * 0.101972  # 比摩阻毫米水柱
                # 输出计算结果
                self.flowRate_outPut_lineEdit.setText(str(airflowrate))
                self.airVolume_outPut_lineEdit.setText(str(airvolume))
                self.roundTubeDiameter_outPut_lineEdit.setText(str(diameter))
                self.bimodalResistance_pa_outPut_lineEdit.setText(
                    str(bimodalresistancepa)
                )
                self.bimodalResistance_h2o_outPut_lineEdit.setText(
                    str(bimodalresistanceh2o)
                )
        # 方形管阻力计算
        else:
            # 方形管有长度
            if self.pipeLength_checkBox.isChecked():
                # print("方管有长度")
                # 设置相关输出的 QLineEdit 可用
                self.flowRate_outPut_lineEdit.setEnabled(True)
                self.airVolume_outPut_lineEdit.setEnabled(True)
                self.squareTubeLength_outPut_lineEdit.setEnabled(True)
                self.squareTubeWidth_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_pa_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(True)
                self.totalRistance_pa_outPut_lineEdit.setEnabled(True)
                self.totalRistance_h2o_outPut_lineEdit.setEnabled(True)
                # 获取输入数据
                lengthc = self.squareTubeLength_inPut_lineEdit.text()
                widthc = self.squareTubeWidth_inPut_lineEdit.text()
                airvolume = self.airVolume_inPut_lineEdit.text()
                pipelength = self.pipeLength_inPut_lineEdit.text()
                # 计算
                a = math.pow((float(lengthc) * float(widthc)), 0.625)
                b = math.pow((float(lengthc) + float(widthc)), 0.625)
                diameter = 1.3 * (a / b)  # 计算等效直径
                radius = diameter * 0.5  # 将输入的毫米为单位的直径换算成米并获取半径
                airflowrate = float(airvolume) / (math.pi * pow(radius, 2))  # 计算流速
                renolds = (airflowrate * radius * 2) / 0.0000150  # 计算雷诺数
                f = 64 / renolds  # 摩擦系数
                pressurelose = (f * pow(airflowrate, 2) * 1.2) / (4 * radius)  # 阻力损失
                bimodalresistancepa = pressurelose  # 比摩阻
                totalristancepa = pressurelose * float(pipelength) * 0.001  # 总阻力
                bimodalresistanceh2o = bimodalresistancepa * 0.101972  # 比摩阻毫米水柱
                totalristanceh2o = totalristancepa * 0.101972  # 总阻力毫米水柱
                # 输出计算结果
                self.flowRate_outPut_lineEdit.setText(str(airflowrate))
                self.airVolume_outPut_lineEdit.setText(str(airvolume))
                self.squareTubeLength_outPut_lineEdit.setText(str(lengthc))
                self.squareTubeWidth_outPut_lineEdit.setText(str(widthc))
                self.bimodalResistance_pa_outPut_lineEdit.setText(
                    str(bimodalresistancepa)
                )
                self.bimodalResistance_h2o_outPut_lineEdit.setText(
                    str(bimodalresistanceh2o)
                )
                self.totalRistance_pa_outPut_lineEdit.setText(str(totalristancepa))
                self.totalRistance_h2o_outPut_lineEdit.setText(str(totalristanceh2o))
            # 方形管无长度
            else:
                # print("方管无长度")
                # 设置相关输出的 QLineEdit 可用
                self.flowRate_outPut_lineEdit.setEnabled(True)
                self.airVolume_outPut_lineEdit.setEnabled(True)
                self.squareTubeLength_outPut_lineEdit.setEnabled(True)
                self.squareTubeWidth_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_pa_outPut_lineEdit.setEnabled(True)
                self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(True)
                # 获取输入数据
                lengthc = self.squareTubeLength_inPut_lineEdit.text()
                widthc = self.squareTubeWidth_inPut_lineEdit.text()
                airvolume = self.airVolume_inPut_lineEdit.text()
                # pipelength = self.pipeLength_inPut_lineEdit.text()
                # 计算
                a = math.pow((float(lengthc) * float(widthc)), 0.625)
                b = math.pow((float(lengthc) + float(widthc)), 0.625)
                diameter = 1.3 * (a / b)  # 计算等效直径
                radius = diameter * 0.5  # 将输入的毫米为单位的直径换算成米并获取半径
                airflowrate = float(airvolume) / (math.pi * pow(radius, 2))  # 计算流速
                renolds = (airflowrate * radius * 2) / 0.0000150  # 计算雷诺数
                f = 64 / renolds  # 摩擦系数
                pressurelose = (f * pow(airflowrate, 2) * 1.2) / (4 * radius)  # 阻力损失
                bimodalresistancepa = pressurelose  # 比摩阻
                bimodalresistanceh2o = bimodalresistancepa * 0.101972  # 比摩阻毫米水柱
                # 输出计算结果
                self.flowRate_outPut_lineEdit.setText(str(airflowrate))
                self.airVolume_outPut_lineEdit.setText(str(airvolume))
                self.squareTubeLength_outPut_lineEdit.setText(str(lengthc))
                self.squareTubeWidth_outPut_lineEdit.setText(str(widthc))
                self.bimodalResistance_pa_outPut_lineEdit.setText(
                    str(bimodalresistancepa)
                )
                self.bimodalResistance_h2o_outPut_lineEdit.setText(
                    str(bimodalresistanceh2o)
                )

    # 清除键信号槽接收函数，实现清除功能
    def clearlineedit(self):
        # 清除输入输出数据
        self.roundTubeDiameter_inPut_lineEdit.clear()
        self.squareTubeLength_inPut_lineEdit.clear()
        self.squareTubeWidth_inPut_lineEdit.clear()
        self.airVolume_inPut_lineEdit.clear()
        self.pipeLength_inPut_lineEdit.clear()
        self.flowRate_outPut_lineEdit.clear()
        self.airVolume_outPut_lineEdit.clear()
        self.roundTubeDiameter_outPut_lineEdit.clear()
        self.squareTubeLength_outPut_lineEdit.clear()
        self.squareTubeWidth_outPut_lineEdit.clear()
        self.bimodalResistance_pa_outPut_lineEdit.clear()
        self.bimodalResistance_h2o_outPut_lineEdit.clear()
        self.totalRistance_pa_outPut_lineEdit.clear()
        self.totalRistance_h2o_outPut_lineEdit.clear()
        # 设置输出区为不可用
        self.flowRate_outPut_lineEdit.setEnabled(False)
        self.airVolume_outPut_lineEdit.setEnabled(False)
        self.roundTubeDiameter_outPut_lineEdit.setEnabled(False)
        self.squareTubeLength_outPut_lineEdit.setEnabled(False)
        self.squareTubeWidth_outPut_lineEdit.setEnabled(False)
        self.bimodalResistance_pa_outPut_lineEdit.setEnabled(False)
        self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(False)
        self.totalRistance_pa_outPut_lineEdit.setEnabled(False)
        self.totalRistance_h2o_outPut_lineEdit.setEnabled(False)

    # 选择圆形管接收函数，实现圆形管选项可用
    def roundchoose(self):
        self.roundTubeDiameter_inPut_lineEdit.setEnabled(True)
        self.airVolume_inPut_lineEdit.setEnabled(True)
        # 设置互斥的选项不可用
        self.squareTubeLength_inPut_lineEdit.setEnabled(False)
        self.squareTubeWidth_inPut_lineEdit.setEnabled(False)

    # 选择方形管接收函数，实现方形管选项可用
    def squarechoose(self):
        self.squareTubeLength_inPut_lineEdit.setEnabled(True)
        self.squareTubeWidth_inPut_lineEdit.setEnabled(True)
        self.airVolume_inPut_lineEdit.setEnabled(True)
        # 设置互斥的选项不可用
        self.roundTubeDiameter_inPut_lineEdit.setEnabled(False)

    # 展示help对话框
    def showhelp(self):
        self.w = HelpWindow()
        self.w.show()

    # 展示about对话框
    def showabout(self):
        self.w = AboutWindow()
        self.w.show()
