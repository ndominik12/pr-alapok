while True:
    # Felhasználótól szám bekérése
    szam = int(input(f"Kérem, adjon meg egy páros számot: "))
    # Páros szám ellenőrzése
    if szam % 2 == 0:
        print(f"A megadott páros szám: {szam}")
        break
    else:
        print(f"A megadott szám páratlan. Kérem, adjon meg egy páros számot!")