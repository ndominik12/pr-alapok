# Felhasználótól alkalomszám bekérése
megadott_alakalom = int(input(f"Kérem, adja meg, hány alkalommal szeretné megismételni a folyamatot: "))
# Ciklus a megadott alkalomig
for _ in range(megadott_alakalom):
    # Felhasználótól szöveg bekérése
    szoveg = input(f"Kérem, írjon be egy szöveget: ")
    # A bekért szöveg kiírása
    print(f"A bekért szöveg: {szoveg}")