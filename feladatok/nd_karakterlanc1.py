# Mondat bekérése
mondat = input(f"Kérem, írjon be egy mondatot: ")
utolso_karakter = mondat[-1]
# Mondatfajta
if utolso_karakter == ".":
    mondatfajta = "kijelentő"
elif utolso_karakter == "?":
    mondatfajta = "kérdő"
elif utolso_karakter == "!":
    mondatfajta = "felkiáltó vagy felszólító vagy óhatjtó"
else:
    mondatfajta = "ismeretlen"
# Eredmények
print(f"A megadott mondatfajta: {mondatfajta}")