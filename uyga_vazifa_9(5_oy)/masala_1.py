import numpy as np 

A=np.random.uniform(1.01, 9.99, size=(10, 10))
np.set_printoptions(precision=2)

ortacha=np.mean(A)
min=np.min(A)
max=np.max(A)
median=np.median(A)
dispers=np.var(A)
std_ogish=np.std(A)
dioganal=np.diagonal(A)

print(A)
print (f"Massiv o'rtachasi = {ortacha}")
print(f'Massiv minimumi = {min}')
print(f'Massiv maximumi = {max}')
print(f'Massiv mediani = {median}')
print(f'Massiv dispersiyasi= {dispers}')
print(f"Massiv standart og'ishi = {std_ogish}")
print(f'dioganal elementlar')
print(dioganal)