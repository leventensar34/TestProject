print("""************************
Hesap Makinesi Programi

islemler;

1. Toplama islemi

2. Cikarma islemi

3. Carpma islemi

4. Bölme islemi

*************************
""")

a = int(input("Birinci Sayi:"))
b = int(input("Ikinci Sayi:"))

islem = input("Islem giriniz:")

if islem == "1":
    print("{} ile {} in toplami {} dir".format(a, b, a + b))
elif islem == "2":
    print("{} ile {} in farki {} dir".format(a, b, a - b))
elif islem == "3":
    print("{} ile {} in carpimi {} dir".format(a, b, a * b))
elif islem == "4":
    print("{} ile {} in bölümü {} dir".format(a, b, a / b))
else:
    print("Gecersiz islem...")
