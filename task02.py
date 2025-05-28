from random import randint
name = str(input("ism  kiriting: "))
last_name = str(input("familiya kiriting: "))
d = randint(0, 100)
print(f"{name}.{last_name}")
print(f"{last_name}\\_{name}")
print(f"{name[0]}{last_name}{d}")
print(f"{name}{last_name[0]}")
