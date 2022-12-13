print("""
**************************
Faktöriyel Bulma Programi

Cikmak icin q' ya basin.
**************************
""")

while True:
    sayi = input("Sayi:")

    if (sayi == "q"):
        print("Program sonlandiriliyor...")
        break
    else:
        sayi = int(sayi)

        faktoriyel = 1

        for i in range(2, sayi + 1):
            print("Faktoriyel:", faktoriyel, "i:", i)
            faktoriyel *= i
        print("Faktoriyel:", faktoriyel)
