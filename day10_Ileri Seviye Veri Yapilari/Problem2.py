"""
"şiir.txt" şeklinde bir dosya oluşturun ve içinde şu satırlar yer alsın.
Bu dosyanın herbir satırını okuyun. Satırların baş harflerini birbirine ekleyerek bir string oluşturun ve bu string'i ekrana yazdırın.

"""

bas_harfler = ""

with open("siir.txt", "r", encoding="utf-8") as file:
    for satir in file:
        bas_harfler += satir[0]
print(bas_harfler)
