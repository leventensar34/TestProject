print("""**************************
Kullanici Girisi
**************************
""")

sys_kullanici_adi = "ensar"
sys_parola = "12345"

kullanici_adi = input("Kullanici Adi:")
parola = input("Parola:")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Parola hatali....")
elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Kullanici Adi hatali....")
elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Kullanici Adi ve Parola hatali....")
else:
    print("Sisteme basariyla giris yapildi....")
