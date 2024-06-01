import random

simbols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

vopros = int(input('Напишите длину пароля'))

parol =''

for i in range(vopros):
    parol += random.choice(simbols)

print(parol)
