import random
sozluk = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
soru = int(input("Kaç haneden oluşsun"))
password = ""
for i in range(soru):
    password += random.choice(sozluk)
print("Şifreniz : ",password)
