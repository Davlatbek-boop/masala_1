# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kalkulyator.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QGraphicsDropShadowEffect, QWidget
from PyQt5.QtGui import QColor
import math
class Ui_Hisoblagich(object):
    def setupUi(self, Hisoblagich):
        Hisoblagich.setObjectName("Hisoblagich")
        Hisoblagich.resize(299, 372)
        Hisoblagich.setStyleSheet("background-color: rgb(0, 0, 0);")

        button_style = """
QPushButton {
    border-radius: 15px; 
    border: 2px solid blue;
    font: 15pt "MS Shell Dlg 2";
    color: white;
    background-color: black; /* Tugmaning normal holatdagi fon rangi */
    transition: background-color 5s, color 5s; /* Yumshoq o'zgarishlar */
}

QPushButton:hover {
    background-color: blue; /* Sichqoncha tugma ustida yurganda fon rangi */
    color: yellow; /* Hover holatdagi matn rangi */
    border: 2px solid darkblue; /* Hover holatdagi chegara rangi */
}
"""
        self.ishora = QtWidgets.QPushButton(Hisoblagich)
        self.ishora.setGeometry(QtCore.QRect(80, 118, 70, 40))
        self.ishora.setStyleSheet(button_style)
        self.ishora.setObjectName("ishora")
        self.nol = QtWidgets.QPushButton(Hisoblagich)
        self.nol.setGeometry(QtCore.QRect(80, 327, 70, 40))
        self.nol.setStyleSheet(button_style)
        self.nol.setObjectName("nol")
        self.teng = QtWidgets.QPushButton(Hisoblagich)
        self.teng.setGeometry(QtCore.QRect(224, 327, 70, 40))
        self.teng.setStyleSheet(button_style)
        self.teng.setObjectName("teng")
        self.butun = QtWidgets.QPushButton(Hisoblagich)
        self.butun.setGeometry(QtCore.QRect(152, 327, 70, 40))
        self.butun.setStyleSheet(button_style)
        self.butun.setObjectName("butun")
        self.uch = QtWidgets.QPushButton(Hisoblagich)
        self.uch.setGeometry(QtCore.QRect(152, 285, 70, 40))
        self.uch.setStyleSheet(button_style)
        self.uch.setObjectName("uch")
        self.ikki = QtWidgets.QPushButton(Hisoblagich)
        self.ikki.setGeometry(QtCore.QRect(80, 285, 70, 40))
        self.ikki.setStyleSheet(button_style)
        self.ikki.setFlat(False)
        self.ikki.setObjectName("ikki")
        self.plyus = QtWidgets.QPushButton(Hisoblagich)
        self.plyus.setGeometry(QtCore.QRect(224, 285, 70, 40))
        self.plyus.setStyleSheet(button_style)
        self.plyus.setObjectName("plyus")
        self.bir = QtWidgets.QPushButton(Hisoblagich)
        self.bir.setGeometry(QtCore.QRect(8, 285, 70, 40))
        self.bir.setStyleSheet(button_style)
        self.bir.setObjectName("bir")
        self.olti = QtWidgets.QPushButton(Hisoblagich)
        self.olti.setGeometry(QtCore.QRect(152, 243, 70, 40))
        self.olti.setStyleSheet(button_style)
        self.olti.setObjectName("olti")
        self.yetti = QtWidgets.QPushButton(Hisoblagich)
        self.yetti.setGeometry(QtCore.QRect(8, 202, 70, 40))
        self.yetti.setStyleSheet(button_style)
        self.yetti.setObjectName("yetti")
        self.kopaytir = QtWidgets.QPushButton(Hisoblagich)
        self.kopaytir.setGeometry(QtCore.QRect(224, 202, 70, 40))
        self.kopaytir.setStyleSheet(button_style)
        self.kopaytir.setObjectName("kopaytir")
        self.toqqiz = QtWidgets.QPushButton(Hisoblagich)
        self.toqqiz.setGeometry(QtCore.QRect(152, 202, 70, 40))
        self.toqqiz.setStyleSheet(button_style)
        self.toqqiz.setObjectName("toqqiz")
        self.sakkiz = QtWidgets.QPushButton(Hisoblagich)
        self.sakkiz.setGeometry(QtCore.QRect(80, 202, 70, 40))
        self.sakkiz.setStyleSheet(button_style)
        self.sakkiz.setObjectName("sakkiz")
        self.besh = QtWidgets.QPushButton(Hisoblagich)
        self.besh.setGeometry(QtCore.QRect(80, 243, 70, 40))
        self.besh.setStyleSheet(button_style)
        self.besh.setObjectName("besh")
        self.minus = QtWidgets.QPushButton(Hisoblagich)
        self.minus.setGeometry(QtCore.QRect(224, 243, 70, 40))
        self.minus.setStyleSheet(button_style)
        self.minus.setObjectName("minus")
        self.tort = QtWidgets.QPushButton(Hisoblagich)
        self.tort.setGeometry(QtCore.QRect(8, 243, 70, 40))
        self.tort.setStyleSheet(button_style)
        self.tort.setObjectName("tort")
        self.ildiz = QtWidgets.QPushButton(Hisoblagich)
        self.ildiz.setGeometry(QtCore.QRect(152, 160, 70, 40))
        self.ildiz.setStyleSheet(button_style)
        self.ildiz.setObjectName("ildiz")
        self.foiz = QtWidgets.QPushButton(Hisoblagich)
        self.foiz.setGeometry(QtCore.QRect(8, 118, 70, 40))
        self.foiz.setStyleSheet(button_style)
        self.foiz.setObjectName("foiz")
        self.bitta_uchir = QtWidgets.QPushButton(Hisoblagich)
        self.bitta_uchir.setGeometry(QtCore.QRect(224, 118, 70, 40))
        self.bitta_uchir.setStyleSheet(button_style)
        self.bitta_uchir.setObjectName("bitta_uchir")
        self.barchasini_uchir = QtWidgets.QPushButton(Hisoblagich)
        self.barchasini_uchir.setGeometry(QtCore.QRect(152, 118, 70, 40))
        self.barchasini_uchir.setStyleSheet(button_style)
        self.barchasini_uchir.setObjectName("barchasini_uchir")
        self.shartmas_2 = QtWidgets.QPushButton(Hisoblagich)
        self.shartmas_2.setGeometry(QtCore.QRect(8, 327, 70, 40))
        self.shartmas_2.setStyleSheet(button_style)
        self.shartmas_2.setObjectName("shartmas_2")
        self.kvadrat = QtWidgets.QPushButton(Hisoblagich)
        self.kvadrat.setGeometry(QtCore.QRect(80, 160, 70, 40))
        self.kvadrat.setStyleSheet(button_style)
        self.kvadrat.setObjectName("kvadrat")
        self.bolish = QtWidgets.QPushButton(Hisoblagich)
        self.bolish.setGeometry(QtCore.QRect(224, 160, 70, 40))
        self.bolish.setStyleSheet(button_style)
        self.bolish.setObjectName("bolish")
        self.kasr = QtWidgets.QPushButton(Hisoblagich)
        self.kasr.setGeometry(QtCore.QRect(8, 160, 70, 40))
        self.kasr.setStyleSheet(button_style)
        self.kasr.setObjectName("kasr")
        self.shartmas = QtWidgets.QLabel(Hisoblagich)
        self.shartmas.setGeometry(QtCore.QRect(20, 90, 271, 21))
        self.shartmas.setStyleSheet("border-radius: 15px; border: 2px solid;font: 10pt \"MS Shell Dlg 2\";color: white")
        self.shartmas.setObjectName("shartmas")
        self.hisoblash = QtWidgets.QLabel(Hisoblagich)
        self.hisoblash.setGeometry(QtCore.QRect(18, 33, 271, 51))
        self.hisoblash.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.hisoblash.setStyleSheet("border-radius: 15px; border: 2px solid blue;font: 15pt \"MS Shell Dlg 2\";color: white")
        self.hisoblash.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hisoblash.setObjectName("hisoblash")

        self.retranslateUi(Hisoblagich)
        QtCore.QMetaObject.connectSlotsByName(Hisoblagich)

        self.add_funcsion()
        self.yagona=False

    def retranslateUi(self, Hisoblagich):
        _translate = QtCore.QCoreApplication.translate
        Hisoblagich.setWindowTitle(_translate("Hisoblagich", "Hisoblagich"))
        self.ishora.setText(_translate("Hisoblagich", "+/-"))
        self.nol.setText(_translate("Hisoblagich", "0"))
        self.teng.setText(_translate("Hisoblagich", "="))
        self.butun.setText(_translate("Hisoblagich", "."))
        self.uch.setText(_translate("Hisoblagich", "3"))
        self.ikki.setText(_translate("Hisoblagich", "2"))
        self.plyus.setText(_translate("Hisoblagich", "+"))
        self.bir.setText(_translate("Hisoblagich", "1"))
        self.olti.setText(_translate("Hisoblagich", "6"))
        self.yetti.setText(_translate("Hisoblagich", "7"))
        self.kopaytir.setText(_translate("Hisoblagich", "×"))
        self.toqqiz.setText(_translate("Hisoblagich", "9"))
        self.sakkiz.setText(_translate("Hisoblagich", "8"))
        self.besh.setText(_translate("Hisoblagich", "5"))
        self.minus.setText(_translate("Hisoblagich", "-"))
        self.tort.setText(_translate("Hisoblagich", "4"))
        self.ildiz.setText(_translate("Hisoblagich", "√x"))
        self.foiz.setText(_translate("Hisoblagich", "%"))
        self.bitta_uchir.setText(_translate("Hisoblagich", "⌫"))
        self.barchasini_uchir.setText(_translate("Hisoblagich", "C"))
        self.shartmas_2.setText(_translate("Hisoblagich", "00"))
        self.kvadrat.setText(_translate("Hisoblagich", "x²"))
        self.bolish.setText(_translate("Hisoblagich", "÷"))
        self.kasr.setText(_translate("Hisoblagich", "1/x"))
        self.shartmas.setText(_translate("Hisoblagich", " MC       MR       M+       M-       MS        M>"))
        self.hisoblash.setText(_translate("Hisoblagich", "0"))


    def add_funcsion(self):
        self.bir.clicked.connect(lambda:self.write_func(self.bir.text()))
        self.ikki.clicked.connect(lambda:self.write_func(self.ikki.text()))
        self.uch.clicked.connect(lambda:self.write_func(self.uch.text()))
        self.tort.clicked.connect(lambda:self.write_func(self.tort.text()))
        self.besh.clicked.connect(lambda:self.write_func(self.besh.text()))
        self.olti.clicked.connect(lambda:self.write_func(self.olti.text()))
        self.yetti.clicked.connect(lambda:self.write_func(self.yetti.text()))
        self.sakkiz.clicked.connect(lambda:self.write_func(self.sakkiz.text()))
        self.toqqiz.clicked.connect(lambda:self.write_func(self.toqqiz.text()))
        self.nol.clicked.connect(lambda:self.write_func(self.nol.text()))

        self.butun.clicked.connect(lambda:self.nuqta(self.butun.text()))

        self.plyus.clicked.connect(lambda:self.write_func(self.plyus.text()))
        self.minus.clicked.connect(lambda:self.write_func(self.minus.text()))

        self.ishora.clicked.connect(self.ishora_almashtirish)
        
        self.kopaytir.clicked.connect(lambda:self.write_func("*"))
        self.bolish.clicked.connect(lambda:self.write_func("/"))
        self.kvadrat.clicked.connect(self.darajaga_kotar) 
        self.ildiz.clicked.connect(self.ildizdan_chiqarish)
        self.teng.clicked.connect(self.amallar)
        self.foiz.clicked.connect(self.foiz_chiqar)
        self.barchasini_uchir.clicked.connect(self.clear)
        self.bitta_uchir.clicked.connect(self.bir_uchir)
    
    def nuqta(self, nuqtacha):
        if "." not in self.hisoblash.text():
            self.hisoblash.setText(self.hisoblash.text()+nuqtacha)
        else:
            self.hisoblash.setText(self.hisoblash.text())
             
             

    def ishora_almashtirish(self):
        tekshirish=self.hisoblash.text()
        if tekshirish[0].isdigit():
            if tekshirish=="0":
                self.hisoblash.setText("-")
            else:
                tekshirish="-"+tekshirish
                self.hisoblash.setText(tekshirish)
        else:
            tekshirish=tekshirish[1:]
            self.hisoblash.setText(tekshirish)
            

    def write_func(self, raqam):
        if self.hisoblash.text()=='0' or self.yagona:
            if raqam in "+*/.":
                self.hisoblash.setText(self.hisoblash.text()+raqam)
            else:
                self.hisoblash.setText(raqam)
                self.yagona=False
        else:
            tekshirish=self.hisoblash.text()
            if tekshirish and tekshirish[-1] not in "+-*/.":
                    self.hisoblash.setText(self.hisoblash.text()+raqam)
            else:
                if raqam.isdigit():
                    self.hisoblash.setText(self.hisoblash.text()+raqam)
                else:
                    self.hisoblash.setText(tekshirish)

    def amallar(self):
        tekshirish=self.hisoblash.text()
        if tekshirish and tekshirish[-1] not in "+-*/":
            yigindi=eval(tekshirish)
            self.hisoblash.setText(str(yigindi))
            self.yagona=True
        else:
            tekshirish=tekshirish[:-1]
            yigindi=eval(tekshirish)
            self.hisoblash.setText(str(yigindi))
            self.yagona=True

    def foiz_chiqar(self):
        foizda=eval(self.hisoblash.text())
        self.hisoblash.setText(str(foizda/100))

    def clear(self):
        self.hisoblash.setText("0")

    def bir_uchir(self):
        text_1=self.hisoblash.text()
        if len(text_1)!=1:
                text_2=text_1[:-1]
                self.hisoblash.setText(text_2)
        else:
                self.hisoblash.setText("0")

    def darajaga_kotar(self):
        tekshirish=self.hisoblash.text()
        if tekshirish and tekshirish[-1] in "+-*/":
                tekshirish=tekshirish[:-1]
                daraja_1=tekshirish
                daraja_2=pow(float(daraja_1),2)
                self.hisoblash.setText(str(daraja_2))
                self.yagona=True
        else:
                daraja_1=self.hisoblash.text()
                daraja_2=pow(float(daraja_1),2)
                self.hisoblash.setText(str(daraja_2))
                self.yagona=True
    
    def ildizdan_chiqarish(self):
        tekshirish=self.hisoblash.text()
        if tekshirish and tekshirish[-1] in "+-*/":
                tekshirish=tekshirish[:-1]
                daraja_1=tekshirish
                daraja_2=math.sqrt(float(daraja_1))
                self.hisoblash.setText(str(daraja_2))
                self.yagona=True
        else:
                daraja_1=self.hisoblash.text()
                daraja_2=math.sqrt(float(daraja_1))
                self.hisoblash.setText(str(daraja_2))
                self.yagona=True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hisoblagich = QtWidgets.QWidget()
    ui = Ui_Hisoblagich()
    ui.setupUi(Hisoblagich)
    Hisoblagich.show()
    sys.exit(app.exec_())
