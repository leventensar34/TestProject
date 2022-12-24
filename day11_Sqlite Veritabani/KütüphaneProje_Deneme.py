import time
import trace

from Kütüphane import *

print("""
************************

Kütüphane Programina Hosgeldiniz.

islemler;
1. Kitaplari goster
2. Kitap sorgulama
3. Kitap ekle
4. Kitap sil
5. Baski yukselt

Cikmak icin 'q' ya basin.

************************


""")

kütüphane = Kütüphane()
while True:
    islem = input("Yapacaginiz islem:")

    if (islem == "q"):
        print("Program sonlandiriliyor...")
        print("Yine bekleriz...")
        break
    elif (islem == "1"):
        kütüphane.kitaplari_goster()

    elif (islem == "2"):
        isim = input("Hangi kitabi istiyorsunuz:")
        print("Kitap sorgulaniyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
    elif (islem == "3"):
        isim = input("isim:")
        yazar = input("Yazar:")
        yayinevi = input("Yayinevi:")
        tür = input("Tür:")
        baski = int(input("Baski:"))

        yeni_kitap = Kitap(isim, yazar, yayinevi, tür, baski)

        print("Kitap ekleniyor...")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi....")

    elif (islem == "4"):
        isim = input("Hangi kitabi silmek istiyorsunuz?")

        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi...")

    elif (islem == "5"):
        isim = input("Hangi kitabin baskisini yükseltmek istiyor sunuz?")
        print("Baski yükseltiliyor...")
        time.sleep(2)
        kütüphane.baski_yükselt(isim)
        print("Baski yükseltildi...")
    else:
        print("Gecersiz islem...")
