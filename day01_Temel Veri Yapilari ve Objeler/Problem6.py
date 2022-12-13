"""

Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.

Hipotenüs Formülü: a^2 + b^2 = c^2

"""

a = int(input("Birnci dik kenar:"))
b = int(input("Ikinci dik kenar:"))

c = (a ** 2 + b ** 2) ** 0.5

print("Birnci dik kenar: {}\nIkinci dik kenar: {}\nHipotenus: {}".format(a, b, c))
