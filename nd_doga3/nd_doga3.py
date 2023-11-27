import random
szam = 0
veletlen_szam = random.randint(1, 3)
int(input("Adj meg egy számot:"))

if szam == veletlen_szam:
    print(f"Helyes!")
else:
    print(f"A szám helytelen. Próbálja újra!")