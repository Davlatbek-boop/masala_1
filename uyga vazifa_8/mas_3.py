import shutil
import os


a = os.listdir("D:/")



k= r"C:/Users/User/Desktop/kochirish_uchun.txt"
c = r"D:/Maan_bekorchiman" 
with open(k,"w") as f:
    f.write("Salimov Davlatning ko'chirish uchun .txt fayli Ustoz fayl ko'chgan bolishi kerak manda ko'chdi yani ishladi!!!")


if os.path.exists(k):
    if os.path.isfile(k):  
        b = shutil.copy2(k, c)
        print("Fayl muvaffaqiyatli nusxalandi.")
    elif os.path.isdir(k):
        shutil.copytree(k, c, dirs_exist_ok=True)  
        print("Papka muvaffaqiyatli nusxalandi.")
else:
    print(f"{k} fayl yoki papka topilmadi.")
