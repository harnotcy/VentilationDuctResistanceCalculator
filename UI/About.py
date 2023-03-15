# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'About.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QTextBrowser, QWidget)

class Ui_about_Dialog(object):
    def setupUi(self, about_Dialog):
        if not about_Dialog.objectName():
            about_Dialog.setObjectName(u"about_Dialog")
        about_Dialog.resize(400, 300)
        about_Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.about_buttonBox = QDialogButtonBox(about_Dialog)
        self.about_buttonBox.setObjectName(u"about_buttonBox")
        self.about_buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.about_buttonBox.setFocusPolicy(Qt.NoFocus)
        self.about_buttonBox.setOrientation(Qt.Horizontal)
        self.about_buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.label_2 = QLabel(about_Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 19, 61, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.about_textBrowser = QTextBrowser(about_Dialog)
        self.about_textBrowser.setObjectName(u"about_textBrowser")
        self.about_textBrowser.setGeometry(QRect(30, 10, 341, 221))
        self.about_textBrowser.setMouseTracking(False)
        self.about_textBrowser.setAcceptDrops(True)
        self.about_textBrowser.setInputMethodHints(Qt.ImhNone)

        self.retranslateUi(about_Dialog)
        self.about_buttonBox.accepted.connect(about_Dialog.accept)
        self.about_buttonBox.rejected.connect(about_Dialog.reject)

        QMetaObject.connectSlotsByName(about_Dialog)
    # setupUi

    def retranslateUi(self, about_Dialog):
        about_Dialog.setWindowTitle(QCoreApplication.translate("about_Dialog", u"\u5173\u4e8e", None))
        self.label_2.setText("")
        self.about_textBrowser.setHtml(QCoreApplication.translate("about_Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">\u901a\u98ce\u7ba1\u9053\u963b\u529b\u8ba1\u7b97\u5668   </span><span style=\" font-size:10pt;\">V1.0</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Ventilation Duct Resistance Calculator   V1.0</span></p>\n"
"<p style"
                        "=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4f7f\u7528MIT\u534f\u8bae\u5f00\u6e90</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Verdana','Geneva','Arial','Helvetica','sans-serif'; font-size:12px; color:#000000; background-color:#ffffff;\">License: The MIT License (MIT) </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Verdana','Geneva','Arial','Helvetica','sans-serif'; font-size:12px; color:#000000; background-color:#ffffff;\">Copyright </span><span style=\" font-family:'-apple-system','SF UI Text','Arial','PingFang SC','Hiragino Sans GB','Microsoft YaHei','WenQuanYi Micro Hei','sans-serif'; font-size:16px; color:#4d4d4d; background-color:#ffffff;\">\u00a9</span><span style=\" font-family:'Verdana','Geneva','Aria"
                        "l','Helvetica','sans-serif'; font-size:12px; color:#000000; background-color:#ffffff;\"> 2023 harnotcy</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u672c\u8f6f\u4ef6\u5728\u5f00\u53d1\u4e2d\uff0c\u5728\u529f\u80fd\u4e0a\u53c2\u8003\u4e86\u8881\u4ee3\u5149\uff08ydg99@sina.com\uff09\u6240\u5236\u4f5c\u7684\u7a0b\u5e8f\u8fdb\u884c\u8bbe\u8ba1\u3002\u672c\u8f6f\u4ef6\u8ba1\u7b97\u7ed3\u679c\u4ec5\u4f9b\u53c2\u8003\uff0c\u8f6f\u4ef6\u4f5c\u8005\u4e0d\u5bf9\u8ba1\u7b97\u7ed3\u679c\u7684\u6b63\u786e\u6027\u505a\u4efb\u4f55\u4fdd\u8bc1\uff0c\u4ea6\u4e0d\u4e3a\u8ba1\u7b97\u7ed3\u679c\u8d1f\u4efb\u4f55\u8d23\u4efb\u3002</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4f7f\u7528 Python 3.10 \u4e0e PySide 6 \u5f00\u53d1\u3002</p></body></html>", None))
    # retranslateUi

