szam = int(input("Kérek egy számot: "))
print(f"A megadott számod: {szam}")

# ... -1, 0, 1, 2, ... 8, 9
#if szam < 10:
#    print(f"A szám kisebb mint 10!")

# ... -1, 0, 1, 2, ... 8, 9, 10
if szam <= 10 or szam == 100: # szam < 11 vagy a szam == 100
    print(f"A szám kisebb vagy egyenlő mint 10 vagy a szám egyenlő 100-zal!")
else:
    print(f"A szám nem kisebb vagy egyenlő mint 10 vagy a szám egyenlő 100-zal!")