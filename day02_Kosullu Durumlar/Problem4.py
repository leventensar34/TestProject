"""
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""
print("""***********************************
Geometrik Sekil Bulma
***********************************
""")
sekil_tipi = input("Hangi seklin tipini ogrenmek istiyorsun?\nDortgen mi?\nUcgen?\nLutfen bir sekil seciniz:")

if (sekil_tipi == "Dörtgen"):
    print("Lutfen kenarlari yaziniz:")
    a = int(input("Birinci kenar:"))
    b = int(input("Ikinci kenar:"))
    c = int(input("Ucuncu kenar:"))
    d = int(input("Dördüncu kenar"))

    if (a == b and a == c and a == d):
        print("Dörtgen bir Kare dir")
    elif (a == c and b == d):
        print("Dörtgen bir Dikdörtgendir")
    else:
        print(" Dörtgen siradan bir dörtgendir")
elif (sekil_tipi == "Ucgen"):
    print("Lutfen kenarlari yaziniz:")
    a = int(input("Birinci kenar:"))
    b = int(input("Ikinci kenar:"))
    c = int(input("Ucuncu kenar:"))
    if (abs(a + b) > c and abs(a + c) > b and abs(b + c) > a):
        if (a == b and a == c):
            print(" Ucgen Eskenar ucgendir")
        elif ((a == b and a != c) or (b == c and b != a) or (a == c and a != b)):
            print("Ucgen Ikizkenar ucgendir")
        else:
            print("Ucgen siradan bir Ucgendir")
    else:
        print("Ucgen belirtmiyor")
else:
    print("Yanlis bir secim yaptiniz......")
