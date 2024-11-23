from PyQt5.QtWidgets import *
from database import *

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(350,400)

        self.ismbox=QHBoxLayout()
        self.ismlabel=QLabel('Ism:')
        self.ismline=QLineEdit()
        self.ismbox.addWidget(self.ismlabel)
        self.ismbox.addWidget(self.ismline)

        self.sharbox=QHBoxLayout()
        self.sharlabel=QLabel('Sharif:')
        self.sharline=QLineEdit()
        self.sharbox.addWidget(self.sharlabel)
        self.sharbox.addWidget(self.sharline)

        self.yoshbox=QHBoxLayout()
        self.yoshlabel=QLabel('Yosh:')
        self.yoshline=QLineEdit()
        self.yoshbox.addWidget(self.yoshlabel)
        self.yoshbox.addWidget(self.yoshline)

        self.jins=QHBoxLayout()
        self.jinslabel=QLabel("Jins:")
        self.rbterkak=QRadioButton('Erkak')
        self.rbtayol=QRadioButton('Ayol')
        self.jins.addWidget(self.jinslabel)
        self.jins.addWidget(self.rbterkak)
        self.jins.addWidget(self.rbtayol)

        self.vilbox=QHBoxLayout()
        self.villabel=QLabel('Viloyat:')
        self.vilcombox=QComboBox()
        self.vilcombox.addItems(['Toshkent viloyati','Andijon viloyati','Farg\'ona viloyati','Namangan viloyati','Samarqand viloyati','Buxoro viloyati','Navoiy viloyati','Qashqadaryo viloyati','Surxondaryo viloyati','Jizzax viloyati','Sirdaryo viloyati','Xorazm viloyati'])
        self.vilbox.addWidget(self.villabel)
        self.vilbox.addWidget(self.vilcombox)

        self.telefon=QHBoxLayout()
        self.tellabel=QLabel('Telefon:')
        self.telline=QLineEdit()
        self.telefon.addWidget(self.tellabel)
        self.telefon.addWidget(self.telline)

        self.fakultet=QHBoxLayout()
        self.faklabel=QLabel('Fakultet:')
        self.fakline=QLineEdit()
        self.fakultet.addWidget(self.faklabel)
        self.fakultet.addWidget(self.fakline)

        self.kursbox=QHBoxLayout()
        self.kurslabel=QLabel('Kurs:')
        self.kurscombox=QComboBox()
        self.kurscombox.addItems(['1-kurs','2-kurs','3-kurs','4-kurs'])
        self.kursbox.addWidget(self.kurslabel)
        self.kursbox.addWidget(self.kurscombox)


        self.btn=QPushButton('Saqlash')
    


        self.umum=QVBoxLayout()
        self.umum.addLayout(self.ismbox)
        self.umum.addLayout(self.sharbox)
        self.umum.addLayout(self.yoshbox)
        self.umum.addLayout(self.jins)
        self.umum.addLayout(self.vilbox)
        self.umum.addLayout(self.telefon)
        self.umum.addLayout(self.fakultet)
        self.umum.addLayout(self.kursbox)
        self.umum.addWidget(self.btn)

        self.setLayout(self.umum)

        self.btn.clicked.connect(self.datagayoz)

    

    def datagayoz(self):
        try:
            ismi=self.ismline.text()
            sharif=self.sharline.text()
            yoshi=self.yoshline.text()
            viloyati = self.vilcombox.currentText()
            telefoni=self.telline.text()
            fakul=self.fakline.text()
            kursi=self.kurscombox.currentText()
            if self.rbterkak.isChecked(): 
                jinsi='Erkak'
            elif self.rbtayol.isChecked():
                jinsi='Ayol'
            else:
                jinsi=''
            if ismsharif(ismi) and ismsharif(sharif) and yosh(yoshi) and telefon(telefoni) and fakultet(fakul) and jinsi!="":
                if datayoz(ismi, sharif, yoshi, jinsi, viloyati, telefoni, fakul, kursi):
                    QMessageBox.information(None, ' Muvaffaqiyatli', 'Malumotlar muvaffaqiyatli saqlandi')
                else:
                    QMessageBox.critical(None, ' Xatolik', 'databazaga yozishda xatolik')
            else:
                QMessageBox.critical(None, ' Xatolik', 'Malumotlarni to\'g\'ri formatda kiriting')

        except:
            QMessageBox.critical(None, 'Xatolik', 'Malumotlarni to\'g\'ri formatda kiriting')


def ismsharif(ism: str):
    try:
        if len(ism)!=0 and ism[0].isupper():
            for i in range(1,len(ism)):
                if ism[i].isdigit() or ism[i].isupper():
                    return False
            return True
        else:
            return False
    except:
        return False


def yosh(yoshi):
    try:
        yoshi= int(yoshi)
        if 10<yoshi<100:
            return True
        return False
    except:
        return False
    
def telefon(raqam):
    try:
        if raqam[0]=='+' and len(raqam)<=15:
            for i in range(1,len(raqam)):
                if raqam[i].isalpha():
                    return False
            return True
        else:
            return False
    except:
        return False
    
def fakultet(mal):
    if len(mal)>0:
        return True
    return False
 
    

if __name__=="__main__":
    app=QApplication([])
    win=Main()
    win.show()
    app.exec_()