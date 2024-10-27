
from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism, yosh):
        self.ism=ism
        self.yosh=yosh
    
    def foydalan(self):
        self.pul=10_000_000
        if int(self.yosh)<18:
            print(f"{self.pul}- shuncha pul ishlatseng buladi")
        else:
            print("Foydalanish xuquqi yo'q")


class Ogil_1(Ota):
    pass
class Ogil_2(Ota):
    pass

abbos=Ogil_1("Abbos","15")
abbos.foydalan()
alisher=Ogil_2("Alisher","35")
alisher.foydalan()
   