import datetime

class Odam:
    def __init__(self,ism):
        self.ism=ism
        self.sekund_1=0


    def yugurush(self):
        self.sekund_1=datetime.datetime.now().strftime("%S")
        print(f"{self.ism} yugurishni boshlandi!!!")

    
    def yiqilish(self):
        if self.sekund_1==0:
            print("yugurish xali boshlanmadi")
        else:
            while True:
                self.sekund_2=datetime.datetime.now().strftime("%S")
                if int(self.sekund_2)-int(self.sekund_1)==5:
                    print(f"{self.ism} yiqildi")
                    break


odam_1=Odam("Davlat")
odam_1.yugurush()
odam_1.yiqilish()