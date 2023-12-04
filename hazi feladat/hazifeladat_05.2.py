# hazi_feladat_05.2
valasz = input(f"Jó napod van? (igen/nem): ")
if valasz.lower() == "igen":
    print(f"Örülök, hogy jó napod van!")
elif valasz.lower() == "nem":
    print(f"Ne aggódj, holnap jobb napod lesz!")
else:
    print(f"Sajnos nem értem a válaszodat!")