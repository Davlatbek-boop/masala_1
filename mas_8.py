import os

a=input("Papka yo'lini kiriting>>>\n")

if os.path.exists(a):
    b=os.listdir(a)
    print(f"Papkadagi papkalar soni:\n{len(b)}")
else:
    print("papka yuli topilmadi")
    