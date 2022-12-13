print("""
************************
Kullanici Girisi Programi
************************
""")

sys_kullanici_adi = "ensar"
sys_parola = "12345"
giris_hakki = 3

while True:
    kullanici_adi = input("Kullanici Adi:")
    parola = input("Parola:")
    if (kullanici_adi != sys_kullanici_adi and parola == sys_parola):
        print("Kullanici adi hatali...")
        giris_hakki -= 1
    elif (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
        print("Parola hatali...")
        giris_hakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and parola != sys_parola):
        print("Kullanici Adi ve Parola hatali...")
        giris_hakki -= 1
    else:
        print("Basarili bir giris yaptiniz...")
        break
    if (giris_hakki == 0):
        print("Giris hakkiniz bitti...")
        break
