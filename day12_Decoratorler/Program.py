"""
1'den 1000'e kadar olan asal sayıları ekrana yazdıran bir program yazın.
 Daha sonra bir tane decorator fonksiyon kullanarak bu fonksiyona 1'den 1000'e kadar olan mükemmel sayıları yazdırma özelliği ekleyin.

"""


def extra(fonk):
    def wrapper():
        print("Mükemmel sayilar...")

        for sayi in range(1, 1001):
            toplam = 0
            i = 1

            while (i < sayi):
                if (sayi % i == 0):
                    toplam += i
                i += 1
            if (toplam == sayi):
                print(sayi)
        fonk()

    return wrapper


@extra
def asal_sayilar():
    print("Asal Sayilar...")

    for sayi in range(2, 1001):
        i = 2
        sayac = 0
        while (i < sayi):
            if (sayi % i == 0):
                sayac += 1
            i += 1
        if (sayac == 0):
            print(sayi)


asal_sayilar()
