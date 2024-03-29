"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti )
o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4

"""

sayi = input("Sayi:")
basamak_sayisi = len((sayi))
sayi = int(sayi)
toplam = 0
basamak = 0

gecici_sayi = sayi

while (gecici_sayi > 0):
    basamak = gecici_sayi % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayi //= 10
if (toplam == sayi):
    print(sayi, "bir Armstrong sayidir.")
else:
    print(sayi, "bir Armstrong sayi degildir.")
