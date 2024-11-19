import numpy as np

data = np.array([
    ["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"],
    [1000, 1200, 1500, 1350, 1400, 1300, 1250, 1450, 1300, 1550, 1600, 1700],  # Zavod 1
    [800, 900, 1000, 950, 1000, 1100, 1200, 1150, 1000, 1100, 1200, 1300],      # Zavod 2
    [1200, 1300, 1250, 1400, 1500, 1600, 1650, 1700, 1600, 1550, 1500, 1400],   # Zavod 3
    [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450],     # Zavod 4
])

raqam=data[1:].astype(int)
zavod=[]
for i in range(len(raqam)):
    zavod.append(np.sum(raqam[i]))
    print(f'Zavod {i+1} - {np.sum(raqam[i])} ta yuk moshin')
        
sum=np.sum(zavod)
print(f'Umumiy ishlab chiqarish = {sum} ta ')
for i in range(len(zavod)):
    if zavod[i]==max(zavod):
        q=i
print(f"{q+1} -  zavod eng ko'p islab chiqorgan")

# print(zavod)