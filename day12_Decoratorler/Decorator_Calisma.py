def extra(fonk):
    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0

        for sayi in sayilar:

            if (sayi % 2 == 0):

                ciftler_toplami += sayi
                cift_sayilar += 1
            else:
                tekler_toplami += sayi
                tek_sayilar += 1
        print("Teklerin Ortalamasi:", tekler_toplami / tek_sayilar)

        print("Ciftlerin Ortalamasi:", ciftler_toplami / cift_sayilar)

        fonk(sayilar)
    return wrapper


@extra
def ortalamabul(sayilar):
    toplam = 0

    for sayi in sayilar:
        toplam += sayi
    print("Genel Ortalama:", toplam / len(sayilar))


ortalamabul([1, 2, 3, 4, 34, 60, 63, 32, 100, 105])

print("-----------------------------")

ortalamabul(range(150))
