import sys
from PyQt5.QtWidgets import QWidget, QPushButton,QApplication,QLineEdit

class Yangi(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("masala_3")
        self.setGeometry(300, 200, 300, 300)

        self.lnd=QLineEdit(self)
        self.lnd.setGeometry(100,50,100,50)
        self.lnd.setStyleSheet("font-size: 24px;")
        
        self.btn_ok=QPushButton("Ok",self)
        self.btn_ok.setGeometry(100,100,100,50)

        self.btn_1=QPushButton("0",self)
        self.btn_1.setGeometry(65,160,50,50)

        self.btn_2=QPushButton("0",self)
        self.btn_2.setGeometry(130,160,50,50)

        self.btn_3=QPushButton("0",self)
        self.btn_3.setGeometry(195,160,50,50)

        self.btn_ok.clicked.connect(self.sonlar)

    def sonlar(self):
        a=self.lnd.text()
        if a.isdigit() and len(a)<4:
            a=int(a)
            k=a%10
            b=a//10%10
            y=a//100%10
            self.btn_1.setText(str(y))
            self.btn_2.setText(str(b))
            self.btn_3.setText(str(k))
        else:
            self.lnd.clear()
            self.lnd.setPlaceholderText("ERROR")
            


        
    

if __name__=="__main__":
    app=QApplication([])
    window = Yangi()
    window.show()
    sys.exit(app.exec_())