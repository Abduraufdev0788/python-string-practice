from random import randint
name = str(input("ism familyangizni kiriting: "))
a = name.split(" ")
d = randint(0, 100)
b = a[0]
c = a[1]
print(f"{b}.{c}")
print(f"{c}\\_{b}")
print(f"{b[0]}{c}{d}")
print(f"{b}{c[0]}")
