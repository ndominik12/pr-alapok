# hazi_feladat_08.py
szam = int(input(f"Kérem, adjon meg egy egész számot: "))
if szam > 0 and szam % 2 == 0:
    print(f"Az ön által megadott szám ({szam}) pozitív páros szám.")
elif szam < 0 and szam % 2 != 0:
    print(f"Az ön által megadott szám ({szam}) negatív páratlan szám.")
else:
    print(f"Az ön által megadott szám nem felel meg a kritériumoknak.")