

class Odam:
    def __init__(self, ism):
        self.ism=ism

    def salomlashish(self):
        return f"Salom {self.ism}"
    
a=Odam(input("ismni kiriting>>>"))
print(a.salomlashish())