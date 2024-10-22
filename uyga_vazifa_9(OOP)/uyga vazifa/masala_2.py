

class Odam:
    def __init__(self,ism):
        self.ism=ism
        self.q=0
        self.w=0

    def kuylash(self):
        self.q=1
    
    def eshitish(self):
        self.w=1

    def gapirish(self):
        if self.w==1 and self.q==1:
            print("kuylandi va eshitildi")
        elif self.q==1 and self.w==0:
            print("Kuylandi lekin eshitilmadi")
        elif self.q==0 and self.w==1:
            print("Eshitildi lekin kuylanmadi")
        else:
            print("kuylanmadiyam eshitilmadiyam")
            
a=Odam("Davlat")
a.kuylash()
a.eshitish()
a.gapirish()