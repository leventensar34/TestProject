"""
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.

    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF


"""

vize1 = float(input("Vize 1 notunu giriniz:"))
vize2 = float(input("Vize 2 notunu giriniz:"))
final = float(input("Final notunu giriniz:"))

toplam_not = (vize1 * 3 / 10 + vize2 * 3 / 10 + final * 4 / 10)

print("Toplam Not:", toplam_not)

if (toplam_not >= 90):
    print("AA")
elif (toplam_not >= 85):
    print("BA")
elif (toplam_not > 80):
    print("BB")
elif (toplam_not >= 75):
    print("CB")
elif (toplam_not > 70):
    print("CC")
elif (toplam_not >= 65):
    print("DC")
elif (toplam_not > 60):
    print("DD")
elif (toplam_not >= 55):
    print("FD")
else:
    print("FF")
