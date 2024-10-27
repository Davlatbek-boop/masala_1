
from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism, varoq):
        self.ism=ism
        self.kitob=int(varoq)//15
        self.pul=10_000_000


    @abstractmethod
    def pul_berish(self):
        if self.kitob//15>0:
            self.pul - 1300
            print(f"{self.ism} - ga  so'm berildi")
        else:
            print("Ko'proq kitob o'qish kerak")


class Ogil_1(Ota):
    def __init__(self, ism, varoq):
        super().__init__(ism, varoq)
        self.pul_1=0

    def pul_berish(self):
        a=self.kitob//15
        if self.kitob//15>0:
            self.pul - 1300
            print(f"{self.pul_1+a*13000} - so'm {self.ism} qo'shildi")
        else:
            print("Ko'proq kitob o'qish kerak")


class Ogil_2(Ota):
    def __init__(self, ism, varoq):
        super().__init__(ism, varoq)
        self.pul_2=0

    def pul_berish(self):
        a=self.kitob//15
        if self.kitob//15>0:
            self.pul - 1300
            print(f"{self.pul_1+a*13000} - so'm {self.ism} ga qo'shildi")
        else:
            print("Ko'proq kitob o'qish kerak")
        

abbos=Ogil_1("Abbos","1000")
abbos.pul_berish()
alisher=Ogil_2("Alisher","73")
alisher.pul_berish()
   