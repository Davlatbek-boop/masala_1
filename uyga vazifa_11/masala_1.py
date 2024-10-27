from abc import ABC, abstractmethod

class Ota(ABC):
    def __init__(self, ism, yosh, prava):
        self.ism=ism
        self.yosh=yosh
        self.prava=prava

    @abstractmethod
    def haydash(self):
        if self.prava=="bor":
            return f"{self.ism} ga ruxsat bor"
        else:
            return f"{self.ism} ruxsat yoooooq"


class Ogil_1(Ota):
    def __init__(self, ism, yosh, prava):
        super().__init__(ism, yosh, prava)

    def haydash(self):
        return f"man prava oldim"

class Ogil_2(Ota):
    pass

abbos=Ogil_1("Abbos","21","bor")


print(abbos.haydash())
try:
    alisher=Ogil_2("Alisher","35","yoq")
    print(alisher.haydash())
except:
    print("ruxsat yoq")