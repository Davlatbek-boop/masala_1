import os
import shutil


a=input("Fayl yo'lini ko'rsating>>>\n")

if os.path.exists(a):
    shutil.rmtree(a)
    print("Papka muvoffaqiyatli o'chirildi")
else:
    print("papka topilmadi")