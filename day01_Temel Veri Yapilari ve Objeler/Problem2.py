"""
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
"""

a = float(input("a:"))
b = float(input("b:"))
ki = (b / a ** 2)
print("Boy: {}\nKilo: {}\nBeden Kitle Endeksi: {}".format(a, b, ki))
