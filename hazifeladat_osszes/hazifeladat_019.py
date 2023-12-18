# Felhasználótól páros szám bekérése
while True:
    szam = int(input(f"Adj meg egy páros számot: "))
    if szam % 2 == 0:
        break
    else:
        print(f"A megadott szám páratlan. Kérem, adj meg egy páros számot.")
# Pocak rajzolása
for i in range(szam // 2 + 1):
    print("O " * i)
for i in range(szam // 2, 0, -1):
    print("O " * i)