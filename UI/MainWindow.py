# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 612)
        MainWindow.setIconSize(QSize(36, 36))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainWindowSoftName_label = QLabel(self.centralwidget)
        self.mainWindowSoftName_label.setObjectName(u"mainWindowSoftName_label")
        self.mainWindowSoftName_label.setGeometry(QRect(20, 10, 561, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.mainWindowSoftName_label.setFont(font)
        self.inPut_groupBox = QGroupBox(self.centralwidget)
        self.inPut_groupBox.setObjectName(u"inPut_groupBox")
        self.inPut_groupBox.setGeometry(QRect(20, 50, 561, 191))
        font1 = QFont()
        font1.setPointSize(12)
        self.inPut_groupBox.setFont(font1)
        self.layoutWidget = QWidget(self.inPut_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 525, 153))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.squareTubeWidth_inPut_lineEdit = QLineEdit(self.layoutWidget)
        self.squareTubeWidth_inPut_lineEdit.setObjectName(u"squareTubeWidth_inPut_lineEdit")
        self.squareTubeWidth_inPut_lineEdit.setEnabled(True)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.squareTubeWidth_inPut_lineEdit)

        self.squareTubeLength_inPut_lineEdit = QLineEdit(self.layoutWidget)
        self.squareTubeLength_inPut_lineEdit.setObjectName(u"squareTubeLength_inPut_lineEdit")
        self.squareTubeLength_inPut_lineEdit.setEnabled(True)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.squareTubeLength_inPut_lineEdit)

        self.roundTubeDiameter_inPut_lineEdit = QLineEdit(self.layoutWidget)
        self.roundTubeDiameter_inPut_lineEdit.setObjectName(u"roundTubeDiameter_inPut_lineEdit")
        self.roundTubeDiameter_inPut_lineEdit.setEnabled(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.roundTubeDiameter_inPut_lineEdit)

        self.roundTubeDiameter_inPut_label = QLabel(self.layoutWidget)
        self.roundTubeDiameter_inPut_label.setObjectName(u"roundTubeDiameter_inPut_label")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.roundTubeDiameter_inPut_label)

        self.squareTubeLength_inPut_label = QLabel(self.layoutWidget)
        self.squareTubeLength_inPut_label.setObjectName(u"squareTubeLength_inPut_label")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.squareTubeLength_inPut_label)

        self.squareTubeWidth_inPut_label = QLabel(self.layoutWidget)
        self.squareTubeWidth_inPut_label.setObjectName(u"squareTubeWidth_inPut_label")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.squareTubeWidth_inPut_label)

        self.roundTube_radioButton = QRadioButton(self.layoutWidget)
        self.roundTube_radioButton.setObjectName(u"roundTube_radioButton")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.roundTube_radioButton)

        self.squareTube_radioButton = QRadioButton(self.layoutWidget)
        self.squareTube_radioButton.setObjectName(u"squareTube_radioButton")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.squareTube_radioButton)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 2, 1)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.airVolume_inPut_label = QLabel(self.layoutWidget)
        self.airVolume_inPut_label.setObjectName(u"airVolume_inPut_label")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.airVolume_inPut_label)

        self.airVolume_inPut_lineEdit = QLineEdit(self.layoutWidget)
        self.airVolume_inPut_lineEdit.setObjectName(u"airVolume_inPut_lineEdit")
        self.airVolume_inPut_lineEdit.setEnabled(True)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.airVolume_inPut_lineEdit)

        self.pipeLength_checkBox = QCheckBox(self.layoutWidget)
        self.pipeLength_checkBox.setObjectName(u"pipeLength_checkBox")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.pipeLength_checkBox)

        self.pipeLength_inPut_lineEdit = QLineEdit(self.layoutWidget)
        self.pipeLength_inPut_lineEdit.setObjectName(u"pipeLength_inPut_lineEdit")
        self.pipeLength_inPut_lineEdit.setEnabled(True)
        self.pipeLength_inPut_lineEdit.setDragEnabled(False)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.pipeLength_inPut_lineEdit)

        self.enptyHolder_label_1 = QLabel(self.layoutWidget)
        self.enptyHolder_label_1.setObjectName(u"enptyHolder_label_1")

        self.formLayout_3.setWidget(0, QFormLayout.SpanningRole, self.enptyHolder_label_1)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.line)

        self.emptyHolder_label_2 = QLabel(self.layoutWidget)
        self.emptyHolder_label_2.setObjectName(u"emptyHolder_label_2")

        self.formLayout_3.setWidget(1, QFormLayout.SpanningRole, self.emptyHolder_label_2)

        self.emptyHolder_label_3 = QLabel(self.layoutWidget)
        self.emptyHolder_label_3.setObjectName(u"emptyHolder_label_3")

        self.formLayout_3.setWidget(5, QFormLayout.SpanningRole, self.emptyHolder_label_3)


        self.gridLayout_2.addLayout(self.formLayout_3, 0, 2, 1, 1)

        self.line_2 = QFrame(self.layoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_2, 0, 1, 1, 1)

        self.result_groupBox = QGroupBox(self.centralwidget)
        self.result_groupBox.setObjectName(u"result_groupBox")
        self.result_groupBox.setGeometry(QRect(20, 259, 421, 321))
        self.result_groupBox.setFont(font1)
        self.formLayoutWidget_3 = QWidget(self.result_groupBox)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(20, 30, 381, 291))
        self.formLayoutWidget_3.setFont(font1)
        self.formLayout_4 = QFormLayout(self.formLayoutWidget_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.flowRate_outPut_label = QLabel(self.formLayoutWidget_3)
        self.flowRate_outPut_label.setObjectName(u"flowRate_outPut_label")
        self.flowRate_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.flowRate_outPut_label)

        self.flowRate_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.flowRate_outPut_lineEdit.setObjectName(u"flowRate_outPut_lineEdit")
        self.flowRate_outPut_lineEdit.setEnabled(True)
        self.flowRate_outPut_lineEdit.setFont(font1)
        self.flowRate_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.flowRate_outPut_lineEdit)

        self.airVolume_outPut_label = QLabel(self.formLayoutWidget_3)
        self.airVolume_outPut_label.setObjectName(u"airVolume_outPut_label")
        self.airVolume_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.airVolume_outPut_label)

        self.airVolume_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.airVolume_outPut_lineEdit.setObjectName(u"airVolume_outPut_lineEdit")
        self.airVolume_outPut_lineEdit.setEnabled(True)
        self.airVolume_outPut_lineEdit.setFont(font1)
        self.airVolume_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.airVolume_outPut_lineEdit)

        self.roundTubeDiameter_outPut_label = QLabel(self.formLayoutWidget_3)
        self.roundTubeDiameter_outPut_label.setObjectName(u"roundTubeDiameter_outPut_label")
        self.roundTubeDiameter_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.roundTubeDiameter_outPut_label)

        self.roundTubeDiameter_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.roundTubeDiameter_outPut_lineEdit.setObjectName(u"roundTubeDiameter_outPut_lineEdit")
        self.roundTubeDiameter_outPut_lineEdit.setEnabled(True)
        self.roundTubeDiameter_outPut_lineEdit.setFont(font1)
        self.roundTubeDiameter_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.roundTubeDiameter_outPut_lineEdit)

        self.squareTubeLength_outPut_label = QLabel(self.formLayoutWidget_3)
        self.squareTubeLength_outPut_label.setObjectName(u"squareTubeLength_outPut_label")
        self.squareTubeLength_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.squareTubeLength_outPut_label)

        self.squareTubeLength_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.squareTubeLength_outPut_lineEdit.setObjectName(u"squareTubeLength_outPut_lineEdit")
        self.squareTubeLength_outPut_lineEdit.setEnabled(True)
        self.squareTubeLength_outPut_lineEdit.setFont(font1)
        self.squareTubeLength_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.squareTubeLength_outPut_lineEdit)

        self.squareTubeWidth_outPut_label = QLabel(self.formLayoutWidget_3)
        self.squareTubeWidth_outPut_label.setObjectName(u"squareTubeWidth_outPut_label")
        self.squareTubeWidth_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.squareTubeWidth_outPut_label)

        self.squareTubeWidth_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.squareTubeWidth_outPut_lineEdit.setObjectName(u"squareTubeWidth_outPut_lineEdit")
        self.squareTubeWidth_outPut_lineEdit.setEnabled(True)
        self.squareTubeWidth_outPut_lineEdit.setFont(font1)
        self.squareTubeWidth_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.squareTubeWidth_outPut_lineEdit)

        self.bimodalResistance_pa_outPut_label = QLabel(self.formLayoutWidget_3)
        self.bimodalResistance_pa_outPut_label.setObjectName(u"bimodalResistance_pa_outPut_label")
        self.bimodalResistance_pa_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.bimodalResistance_pa_outPut_label)

        self.bimodalResistance_pa_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.bimodalResistance_pa_outPut_lineEdit.setObjectName(u"bimodalResistance_pa_outPut_lineEdit")
        self.bimodalResistance_pa_outPut_lineEdit.setEnabled(True)
        self.bimodalResistance_pa_outPut_lineEdit.setFont(font1)
        self.bimodalResistance_pa_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.bimodalResistance_pa_outPut_lineEdit)

        self.bimodalResistance_h2o_outPut_label = QLabel(self.formLayoutWidget_3)
        self.bimodalResistance_h2o_outPut_label.setObjectName(u"bimodalResistance_h2o_outPut_label")
        self.bimodalResistance_h2o_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.bimodalResistance_h2o_outPut_label)

        self.bimodalResistance_h2o_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.bimodalResistance_h2o_outPut_lineEdit.setObjectName(u"bimodalResistance_h2o_outPut_lineEdit")
        self.bimodalResistance_h2o_outPut_lineEdit.setEnabled(True)
        self.bimodalResistance_h2o_outPut_lineEdit.setFont(font1)
        self.bimodalResistance_h2o_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.bimodalResistance_h2o_outPut_lineEdit)

        self.totalRistance_pa_outPut_label = QLabel(self.formLayoutWidget_3)
        self.totalRistance_pa_outPut_label.setObjectName(u"totalRistance_pa_outPut_label")
        self.totalRistance_pa_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.totalRistance_pa_outPut_label)

        self.totalRistance_pa_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.totalRistance_pa_outPut_lineEdit.setObjectName(u"totalRistance_pa_outPut_lineEdit")
        self.totalRistance_pa_outPut_lineEdit.setEnabled(True)
        self.totalRistance_pa_outPut_lineEdit.setFont(font1)
        self.totalRistance_pa_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.totalRistance_pa_outPut_lineEdit)

        self.totalRistance_h2o_outPut_label = QLabel(self.formLayoutWidget_3)
        self.totalRistance_h2o_outPut_label.setObjectName(u"totalRistance_h2o_outPut_label")
        self.totalRistance_h2o_outPut_label.setFont(font1)

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.totalRistance_h2o_outPut_label)

        self.totalRistance_h2o_outPut_lineEdit = QLineEdit(self.formLayoutWidget_3)
        self.totalRistance_h2o_outPut_lineEdit.setObjectName(u"totalRistance_h2o_outPut_lineEdit")
        self.totalRistance_h2o_outPut_lineEdit.setEnabled(True)
        self.totalRistance_h2o_outPut_lineEdit.setFont(font1)
        self.totalRistance_h2o_outPut_lineEdit.setReadOnly(True)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.totalRistance_h2o_outPut_lineEdit)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 0, 0))
        self.splitter.setOrientation(Qt.Vertical)
        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(0, 0, 2, 2))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(460, 268, 121, 311))
        self.verticalLayout = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.calculate_pushButton = QPushButton(self.layoutWidget3)
        self.calculate_pushButton.setObjectName(u"calculate_pushButton")
        self.calculate_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.calculate_pushButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.resultClear_pushButton = QPushButton(self.layoutWidget3)
        self.resultClear_pushButton.setObjectName(u"resultClear_pushButton")
        self.resultClear_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.resultClear_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.help_pushButton = QPushButton(self.layoutWidget3)
        self.help_pushButton.setObjectName(u"help_pushButton")
        self.help_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.help_pushButton)

        self.about_pushButton = QPushButton(self.layoutWidget3)
        self.about_pushButton.setObjectName(u"about_pushButton")
        self.about_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.about_pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.exec_pushButton = QPushButton(self.layoutWidget3)
        self.exec_pushButton.setObjectName(u"exec_pushButton")
        self.exec_pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.exec_pushButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.roundTube_radioButton, self.squareTube_radioButton)
        QWidget.setTabOrder(self.squareTube_radioButton, self.roundTubeDiameter_inPut_lineEdit)
        QWidget.setTabOrder(self.roundTubeDiameter_inPut_lineEdit, self.squareTubeLength_inPut_lineEdit)
        QWidget.setTabOrder(self.squareTubeLength_inPut_lineEdit, self.squareTubeWidth_inPut_lineEdit)
        QWidget.setTabOrder(self.squareTubeWidth_inPut_lineEdit, self.airVolume_inPut_lineEdit)
        QWidget.setTabOrder(self.airVolume_inPut_lineEdit, self.pipeLength_checkBox)
        QWidget.setTabOrder(self.pipeLength_checkBox, self.pipeLength_inPut_lineEdit)
        QWidget.setTabOrder(self.pipeLength_inPut_lineEdit, self.calculate_pushButton)
        QWidget.setTabOrder(self.calculate_pushButton, self.flowRate_outPut_lineEdit)
        QWidget.setTabOrder(self.flowRate_outPut_lineEdit, self.airVolume_outPut_lineEdit)
        QWidget.setTabOrder(self.airVolume_outPut_lineEdit, self.roundTubeDiameter_outPut_lineEdit)
        QWidget.setTabOrder(self.roundTubeDiameter_outPut_lineEdit, self.squareTubeLength_outPut_lineEdit)
        QWidget.setTabOrder(self.squareTubeLength_outPut_lineEdit, self.squareTubeWidth_outPut_lineEdit)
        QWidget.setTabOrder(self.squareTubeWidth_outPut_lineEdit, self.bimodalResistance_pa_outPut_lineEdit)
        QWidget.setTabOrder(self.bimodalResistance_pa_outPut_lineEdit, self.bimodalResistance_h2o_outPut_lineEdit)
        QWidget.setTabOrder(self.bimodalResistance_h2o_outPut_lineEdit, self.totalRistance_pa_outPut_lineEdit)
        QWidget.setTabOrder(self.totalRistance_pa_outPut_lineEdit, self.totalRistance_h2o_outPut_lineEdit)
        QWidget.setTabOrder(self.totalRistance_h2o_outPut_lineEdit, self.resultClear_pushButton)
        QWidget.setTabOrder(self.resultClear_pushButton, self.help_pushButton)
        QWidget.setTabOrder(self.help_pushButton, self.about_pushButton)
        QWidget.setTabOrder(self.about_pushButton, self.exec_pushButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u901a\u98ce\u7ba1\u9053\u963b\u529b\u8ba1\u7b97\u5668", None))
        self.mainWindowSoftName_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">\u901a\u98ce\u7ba1\u9053\u963b\u529b\u8ba1\u7b97\u5668</span></p></body></html>", None))
        self.inPut_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6570\u636e", None))
        self.roundTubeDiameter_inPut_label.setText(QCoreApplication.translate("MainWindow", u"\u76f4\u5f84(mm)", None))
        self.squareTubeLength_inPut_label.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6(mm)", None))
        self.squareTubeWidth_inPut_label.setText(QCoreApplication.translate("MainWindow", u"\u5bbd\u5ea6(mm)", None))
        self.roundTube_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5706\u5f62\u7ba1", None))
        self.squareTube_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u77e9\u5f62\u7ba1", None))
        self.airVolume_inPut_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u98ce\u91cf(m<span style=\" vertical-align:super;\">3</span>/h)</p></body></html>", None))
        self.pipeLength_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u7ba1\u6bb5\u957f\u5ea6(mm)", None))
        self.enptyHolder_label_1.setText("")
        self.emptyHolder_label_2.setText("")
        self.emptyHolder_label_3.setText("")
        self.result_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.flowRate_outPut_label.setText(QCoreApplication.translate("MainWindow", u"\u6d41\u901f(m/s)", None))
        self.airVolume_outPut_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u98ce\u91cf(m<span style=\" vertical-align:super;\">3</span>/h)</p></body></html>", None))
        self.roundTubeDiameter_outPut_label.setText(QCoreApplication.translate("MainWindow", u"\u5706\u7ba1\u76f4\u5f84(mm)", None))
        self.squareTubeLength_outPut_label.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u7ba1\u8fb9\u957f(mm)", None))
        self.squareTubeWidth_outPut_label.setText(QCoreApplication.translate("MainWindow", u"\u65b9\u7ba1\u8fb9\u5bbd(mm)", None))
        self.bimodalResistance_pa_outPut_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6bd4\u6469\u963b(Pa/m)</p></body></html>", None))
        self.bimodalResistance_h2o_outPut_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u6bd4\u6469\u963b(mmH<span style=\" vertical-align:sub;\">2</span>O/m)</p></body></html>", None))
        self.totalRistance_pa_outPut_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u603b\u963b\u529b(Pa)</p></body></html>", None))
        self.totalRistance_h2o_outPut_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u603b\u963b\u529b(mmH<span style=\" vertical-align:sub;\">2</span>O)</p></body></html>", None))
        self.calculate_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97(&C)", None))
        self.resultClear_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664(&R)", None))
        self.help_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.about_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e(&A)", None))
        self.exec_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa(&E)", None))
    # retranslateUi

