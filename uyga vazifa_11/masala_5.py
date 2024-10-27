
from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism):
        self.ism=ism
        self.kitob=['farxod va shirin','otgan kunlar','men','mehrobdan chayon','sherlok holms']

    def kitob_qidir(self, okitob):
        if okitob in self.kitob:
            print(f"{self.ism} o'qidi")
        else:
            print(f"oooo {self.ism} {okitob} nomli yangi kitob o'qibdi!!!")



class Ogil_1(Ota):
    def __init__(self, ism, pkitob):
        super().__init__(ism)
        self.pkitob=pkitob

    
        

abbos=Ogil_1("Abbos","farxod va shirin")
abbos.kitob_qidir(abbos.pkitob)
alisher=Ogil_1("Alisher","hamsa")
alisher.kitob_qidir(alisher.pkitob)
   