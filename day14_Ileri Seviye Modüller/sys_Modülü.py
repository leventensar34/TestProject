import sys

# print(dir(sys))

"""
a = int(input("a:"))
b = int(input("b:"))

sys.exit()  # exit()--> sistemden cikar 

c = int(input("c:"))

*************************************

sys.stderr.write("Bu bir hata mesajidir\n")
sys.stderr.flush()   # kirmizi yaziyla yailan mesaji yazdirir

sys.stdout.write("Bu bir normal yazidir\n")  # normal bir yazi ile yazilani yazdirir

"""


# Bu sys dosyasi örnegi terminal üzerinden calistirildi ve katsayilar yazilarak kökler bulundu.

def kok_bulma(a, b, c):
    delta = b ** 2 - 4 * a * c
    if (delta < 0):
        print("Reeel kok yok")
    else:
        x1 = (-b - delta ** 0.5) / 2 * a
        x2 = (-b + delta ** 0.5) / 2 * a
        return (x1, x2)


if len(sys.argv) == 4:
    print("Kok bulma", kok_bulma(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
else:
    sys.stderr.write("Lütfen dogru degerler giriniz...")
    sys.stderr.flush()
