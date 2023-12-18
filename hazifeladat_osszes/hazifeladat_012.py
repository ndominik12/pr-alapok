# hazi_feladat_012
import random
felhasznalo_valasztas = input(f"Fej vagy írás? ").lower()
feldobas_eredmeny = random.choice(['fej', 'írás'])
if felhasznalo_valasztas == feldobas_eredmeny:
    print(f"Gratulálok! Eltaláltad! A pénz {feldobas_eredmeny}.")
else:
    print(f"Sajnálom, nem találtad el. A pénz {feldobas_eredmeny} lett.")