"""
Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""

yakan_miktar = float(input("Kilometrede yakan miktari giriniz:"))
yapilan_km = int(input("Gidilen KM yi giriniz:"))

print("Toplam Tutar: {} Tl".format(yakan_miktar * yapilan_km))

