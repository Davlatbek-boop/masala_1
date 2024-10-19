import os

path=os.path.join("D:","Maan_bekorchiman")

if not os.path.exists(path):    
    os.mkdir(path)
    print(path,"Fayl yaratildi!")
else:
    print("Fayl mavjud!!!")