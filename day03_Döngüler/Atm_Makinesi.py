print("""
****************************
Atm Makinesine Hos Geldiniz.

islemler;

1. Bakiye sorgulama

2. Para Yatirma

3. Para Cekme

Programdan cikmak icin 'q' ya basin...
****************************
""")

bakiye = 1000

while True:
    islem = input("islem seciniz:")

    if (islem == "q"):
        print("Yine bekleriz")
        break
    elif (islem == "1"):
        print("Bakiyeniz {} tl dir".format(bakiye))

    elif (islem == "2"):
        miktar = int(input("Miktari giriniz:"))

        bakiye += miktar

    elif (islem == "3"):
        miktar = int(input("Miktari giriniz:"))

        if (bakiye - miktar < 0):
            print("Böyle bir miktar cekemezsiniz... ")
            continue
        bakiye -= miktar
    else:
        print("Gecersiz islem....")
