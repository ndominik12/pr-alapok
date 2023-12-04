#hazi_feladat_04
valasz = input(f"Jó napja van? (igen/nem): ")
if valasz.lower() == "igen":
    print(f"Örülök, hogy jó napja van!")
elif valasz.lower() == "nem":
    print(f"Remélem, hogy jobb lesz hamarosan!")
else:
    print(f"Nem megfelelő válasz, válaszolj 'igen' vagy 'nem'!")