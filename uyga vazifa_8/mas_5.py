import os



a=input("Fayl yo'lini ko'rsating>>>\n")

if os.path.exists(a):
    os.remove(a)
    print("fayl muvoffaqiyatli o'chirildi")
else:
    print("fayl topilmadi")