import random
# Véletlenszámok generálása és kiírása
osszeg = 0  # Számolja a 3-mal osztható számokat
for _ in range(20):
    veletlenszam = random.randint(1, 12)
    if veletlenszam % 3 == 0:
        print(f"{veletlenszam} (3-mal osztható)")
        osszeg += 1
# Eredmények kiírása
print(f"A generált véletlenszámok közül {osszeg} darab volt 3-mal osztható.")