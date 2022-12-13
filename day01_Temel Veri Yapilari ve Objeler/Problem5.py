"""
Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
"""

a = int(input("a:"))
b = int(input("b:"))

a, b = b, a

print("a: {}\nb: {}".format(a, b))

