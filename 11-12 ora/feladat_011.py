# feladat_011

szám1=input("Írj be egy számot /szam1/ ")
szám2=input("Írj be egy másik számot /szam2/")
szam1=int(szam1)
szam2=int(szam2)

if szám1 < szám2:
    print(f"A szám1 kisebb mint a szám2")
elif szám2 < szám1:
    print(f"A szám2 kisebb mint a szám1")
else:
    print(f"A szám1 egyenlő a szám2-vel")