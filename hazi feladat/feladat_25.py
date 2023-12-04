# A program funkcióinak a leírása:
# Ez a program kiszámolja egy kör kerületét és területét, amikor megadott sugarú körrel dolgozik.

# Konstansként tároljuk a PI értékét
PI = 3.14159

# Egy másik változóban tároljuk a kör sugarát (cm)
kor_sugar_cm = 5.0

# Kiszámoljuk a kör kerületét és területét
kor_kerulet_cm = 2 * PI * kor_sugar_cm
kor_terulet_cm2 = PI * kor_sugar_cm**2

# Eredmények kiírása a képernyőre
print(f"A kör kerülete: {kor_kerulet_cm:.2f} cm")
print(f"A kör területe: {kor_terulet_cm2:.2f} cm^2")
