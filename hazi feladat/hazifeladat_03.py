#hazi_feladat_03
import random
def szam_gondolasa():
    gondolt_szam = random.randint(1, 5)
    return gondolt_szam
def jatek():
    gondolt_szam = szam_gondolasa()
    while True:
        tipp = int(input(f"Kérem, adjon meg egy számot 1 és 5 között: "))
        if 1 <= tipp <= 5:
            if tipp == gondolt_szam:
                print(f"Gratulálok! Eltaláltad a számot!")
                break
            elif tipp < gondolt_szam:
                print(f"A gondolt szám nagyobb!")
            else:
                print(f"A gondolt szám kisebb!")
        else:
            print(f"A megadott szám nincs a megengedett tartományban. Kérem, adjon meg egy számot 1 és 5 között.")