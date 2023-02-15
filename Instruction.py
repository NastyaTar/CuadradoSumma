from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instruction(object):
    def setupUi(self, Instruction):
        Instruction.setObjectName("Instruction")
        Instruction.resize(400, 300)
        Instruction.setStyleSheet("background-color:black")
        self.inst = QtWidgets.QTextBrowser(Instruction)
        self.inst.setGeometry(QtCore.QRect(20, 20, 361, 261))
        self.inst.setStyleSheet("background-color:#00FFF5")
        self.inst.setObjectName("inst")

        self.retranslateUi(Instruction)
        QtCore.QMetaObject.connectSlotsByName(Instruction)

    def retranslateUi(self, Instruction):
        _translate = QtCore.QCoreApplication.translate
        Instruction.setWindowTitle(_translate("Instruction", "Dialog"))
        self.inst.setHtml(_translate("Instruction", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.15094pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Цель игры:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">Cобрать в каждом ряду и столбце сумму, которая указана в крайних серых квадратиках, закрашивая нажатием бирюзовые квадратки в фиолетовый. Как только сумма наберется, серый квадратик станет белым.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.15094pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Так же вы можете посмотреть уже набранную Вами сумму, нажав на серый квадратик.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">Нажав кнопку &quot;Заново&quot; поле &quot;сбрасывается&quot;.</span></p></body></html>"))

