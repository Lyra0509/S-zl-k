import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifre uzunluğu giriniz: "))
sifre = ""
for i in range(uzunluk):
    x = random.choice(karakterler)
    sifre += x

print("Seçilen parola:" , sifre)