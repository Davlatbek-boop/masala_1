

class Shaxs:
    def __init__(self, ism, familiya):
        self.ism=ism
        self.familiya=familiya
    
class Talaba(Shaxs):
    def __init__(self, ism, familiya):
        super().__init__(ism, familiya)
        self.fanlar=[]

    def fanga_yozil(self, fani):
        self.fanlar.append(fani)

    def remove_fan(self, r_fan):
        if r_fan in self.fanlar:
            self.fanlar.remove(r_fan)
        else:
            print("Siz bu fanga yozilmagansiz")

    def get_info(self):
        fanlar_ruyxati = ', '.join([fan.nomi for fan in self.fanlar]) if self.fanlar else "Hozircha fan yo'q"
        return f"""       
Ismi:           {self.ism}
Familiyasi:     {self.familiya}
Fanlari:        {fanlar_ruyxati}
        """

class Fan:
    def __init__(self, nomi):
        self.nomi=nomi

fan1=Fan("Matematika")
fan2=Fan("Dasturlash")
fan3=Fan("Kimyo")

talaba_1=Talaba("Salimov","Davlat")
talaba_1.fanga_yozil(fan1)
talaba_1.fanga_yozil(fan2)
talaba_1.fanga_yozil(fan3)

talaba_1.remove_fan(fan1)

print(talaba_1.get_info())
