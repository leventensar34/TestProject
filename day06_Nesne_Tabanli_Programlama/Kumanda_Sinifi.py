import random
import time


class Kumanda():

    def __init__(self, tv_durum="kapali", tv_ses=0, kanal_listesi=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_ac(self):

        if (self.tv_durum == "Acik"):
            print("Tv zaten acik...")
        else:
            print("Tv aciliyor...")
            self.tv_durum = "Acik"

    def tv_kapat(self):

        if (self.tv_durum == "Kapali"):
            print("Tv zaten kapali.")
        else:
            print("Tv kapaniyor...")
            self.tv_durum = "Kapali"

    def ses_ayarlari(self):

        while True:
            cevap = input("Sesi Azalt: '<'\nSesi Arttir: '>'\nCikis: cikis")

            if (cevap == "<"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses", self.tv_ses)
            elif (cevap == ">"):
                if (self.tv_ses != 32):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")

    def rastgele_kanal(self):

        rastgele = random.randint(0, len(self.kanal_listesi) - 1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Su anki Kanal:", self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal Listesi: {}\nSu anki Kanal: {}\n".format(self.tv_durum, self.tv_ses,
                                                                                         self.kanal_listesi, self.kanal)


kumanda = Kumanda()

print("""
*****************************
Televizyon Uygulamasi

1.Tv Ac
2.Tv Kapat
3.Ses Ayarlari
4.Kanal Ekle
5.Kanal Sayiyi Ögrenme
6.Rastgele Kanala Gecme
7.Televizyon Bilgileri

cikmak icin 'q' basin
*****************************
""")

while True:

    islem = input("Islemi seciniz:")
    if (islem == "q"):
        print("Program sonlandiriliyor...")
        break
    elif (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()

    elif (islem == "3"):
        kumanda.ses_ayarlari()

    elif (islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayirarak giriniz:")

        kanal_listesi = kanal_isimleri.split(",")

        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == "5"):
        print("Kanal sayisi:", len(kumanda))

    elif (islem == "6"):
        kumanda.rastgele_kanal()

    elif (islem == "7"):
        print(kumanda)
    else:
        print("Gecersiz islem...")
