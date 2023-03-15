# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Help.ui'
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
    QSizePolicy, QTextBrowser, QWidget)

class Ui_help_Dialog(object):
    def setupUi(self, help_Dialog):
        if not help_Dialog.objectName():
            help_Dialog.setObjectName(u"help_Dialog")
        help_Dialog.resize(400, 300)
        self.help_buttonBox = QDialogButtonBox(help_Dialog)
        self.help_buttonBox.setObjectName(u"help_buttonBox")
        self.help_buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.help_buttonBox.setOrientation(Qt.Horizontal)
        self.help_buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.help_textBrowser = QTextBrowser(help_Dialog)
        self.help_textBrowser.setObjectName(u"help_textBrowser")
        self.help_textBrowser.setGeometry(QRect(30, 20, 341, 201))

        self.retranslateUi(help_Dialog)
        self.help_buttonBox.accepted.connect(help_Dialog.accept)
        self.help_buttonBox.rejected.connect(help_Dialog.reject)

        QMetaObject.connectSlotsByName(help_Dialog)
    # setupUi

    def retranslateUi(self, help_Dialog):
        help_Dialog.setWindowTitle(QCoreApplication.translate("help_Dialog", u"\u5e2e\u52a9", None))
        self.help_textBrowser.setHtml(QCoreApplication.translate("help_Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u901a\u98ce\u7ba1\u9053\u963b\u529b\u8ba1\u7b97\u8bf4\u660e</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u8ba1\u7b97\u65b9\u6cd5\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6839\u636e \u7a7a"
                        "\u8c03\u3001\u536b\u751f\u5de5\u5b66\u4fbf\u89c8 \u7b2c13\u7248 \u56fd\u571f\u4ea4\u901a\u7701 \u5efa\u7b51\u8bbe\u5907\u8bbe\u8ba1\u57fa\u51c6 2009\u5e74\u7248 \u63d0\u4f9b\u7684\u65b9\u6cd5\u8ba1\u7b97\u3002</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.\u6570\u636e\u8f93\u5165\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u98ce\u7ba1\u5c3a\u5bf8\uff1a\u8f93\u5165\u5706\u7ba1\u76f4\u5f84\u548c\u77e9\u5f62\u7ba1\u7684\u8fb9\u957f\u3002 </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u98ce\u91cf\uff1a\u98ce\u7ba1\u5185\u7684\u98ce\u91cf\u3002</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u98ce\u7ba1\u957f\u5ea6\uff1a\u5982\u679c\u7ed9\u51fa\u98ce\u7ba1\u957f\u5ea6\uff0c"
                        "\u5b83\u5c06\u8ba1\u7b97\u8be5\u7ba1\u6bb5\u7684\u603b\u963b\u529b\u3002</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.\u7ed3\u679c\u8f93\u51fa\uff1a</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6570\u636e\u8f93\u5165\u5b8c\u6210\u540e\uff0c\u6309\u201c\u8ba1\u7b97\u201d\u6309\u626d\uff0c\u5728\u7ed3\u679c\u8f93\u51fa\u680f\u5c06\u7ed9\u51fa\u8ba1\u7b97\u7ed3\u679c\u3002</p></body></html>", None))
    # retranslateUi

