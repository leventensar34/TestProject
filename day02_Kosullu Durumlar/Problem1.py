"""
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""

boy = float(input("Boyunuzu giriniz:"))
kilo = float(input("Kilonuzu giriniz:"))

bki = kilo / (boy ** 2)
print("Beden Kitle Endexi", bki)

if (bki < 18.5):
    print("Zayif")
elif (bki >= 18 and bki < 25):
    print("Normal")
elif (bki >= 25 and bki < 30):
    print("Fazla kilolu")
else:
    print("Obez")
