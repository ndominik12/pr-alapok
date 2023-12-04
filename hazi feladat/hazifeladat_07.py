# hazi_feladat_07
import random
gep_gondolt_szam = random.randint(1, 5)
felhasznalo_szam = int(input(f"Kérem, adjon meg egy számot 1 és 5 között: "))
if felhasznalo_szam == gep_gondolt_szam:
    print(f"Az ön által megadott szám ({felhasznalo_szam}) egyenlő a gép által gondolt számmal!")
elif felhasznalo_szam < gep_gondolt_szam:
    print(f"Az ön által megadott szám ({felhasznalo_szam}) kisebb, mint a gép által gondolt szám.")
else:
    print(f"Az ön által megadott szám ({felhasznalo_szam}) nagyobb, mint a gép által gondolt szám.")