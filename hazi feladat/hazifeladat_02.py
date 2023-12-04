#hazi_feladat_02
import math
def kor_kerulet_terulet_szamolo(sugar):
    kerulet = 2 * math.pi * sugar
    terulet = math.pi * sugar**2
    return kerulet, terulet
sugar = float(input("Kérem, adja meg a kör sugarát: "))
kerulet, terulet = kor_kerulet_terulet_szamolo(sugar)
print(f"A kör kerülete: {kerulet:.2f}")
print(f"A kör területe: {terulet:.2f}")
