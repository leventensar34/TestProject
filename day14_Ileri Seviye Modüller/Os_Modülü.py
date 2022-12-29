import os
from datetime import datetime

# os.chdir("C:/Users/user/Desktop")  # yeni adres atamasi yapmak icin

# print(os.getcwd())  # dizi adresini verir bize

# print(os.listdir())  #ilgili adreste ne varsa liste olarak bize döner

# for i in os.listdir():
#    print(i)

# print(os.getcwd())

# os.mkdir("Deneme1") # ilgili adreste bir klasor olusturur

# os.makedirs("Deneme2/Deneme3") # ilgili adreste klasorun icinde bir klasor olusturur

# os.rmdir("Deneme2/Deneme3") # ilgili adresteki klasorun altindaki klasorü siler

# os.removedirs("Deneme2") # ilgili adreste olan klasöleri hepsini siler

# os.rename("text.txt", "test2.txt") # bir dosyanin ismini degistirir.

# print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime)) # bir dosyanin degistirme zamanini verir stat() fonk.

for klasör_yolu, klasör_isimleri, dosya_isimler in os.walk("C:/Users/user/Desktop"):
    print("Klasör yolu", klasör_yolu)
    print("Klasör isimleri", klasör_isimleri)
    print("Dosya isimler", dosya_isimler)
    print("****************************")
