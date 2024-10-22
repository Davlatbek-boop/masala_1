import os
import shutil


a=r"D:Maan_bekorchiman"

if os.path.exists(a):
    shutil.rmtree(a)
else:
    print("papke topilmadi")