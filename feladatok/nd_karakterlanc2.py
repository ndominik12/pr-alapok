# Mondat bekérése
mondat = input(f"Adjon meg egy mondatot (ENTER-rel kilép): ")
while mondat:
    karakter = mondat[-1]
# Mondatfajta    
    if karakter == "?":
        mondatfajta = "kérdő"
    elif karakter == "!":
        mondatfajta = "felkiáltó vagy felszólító vagy óhajtó"
    elif karakter == ".":
        mondatfajta = "kijelentő"
    else:
        mondatfajta = "ismeretlen"
# Eredmények        
    print(f"A mondatfajta tipusa: {mondatfajta}")
# Másik mondat bekérése
    mondat = input(f"Adjon egy másik mondatot (ENTER-rel kilép): ")