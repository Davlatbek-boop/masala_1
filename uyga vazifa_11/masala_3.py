
from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism, varoq):
        self.ism=ism
        self.kitob=int(varoq)//15
        self.pul=10_000_000


    
    def pul_berish(self):
        if self.kitob//15>0:
            self.pul - 13000
            print(f"{self.ism} - ga 13000 so'm berildi")
        else:
            print("Ko'proq kitob o'qish kerak")


class Ogil_1(Ota):
    pass

class Ogil_2(Ota):
    pass

abbos=Ogil_1("Abbos","1000")
abbos.pul_berish()
alisher=Ogil_2("Alisher","3")
alisher.pul_berish()
   