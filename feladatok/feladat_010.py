# feladat_010

szam1 = input("Irj be egy számot /szam1/:")
szam2 = input("Irj be mégegy számot /szam2/:")
szam1 = int(szam1)
szam2 = int(szam2)

if szam1 < szam2:
    print(f"A szam1 kisebb mint a szam2")
elif szam2 < szam1:
    print(f"A szam2 kisebb mint a szam1")
else:
    print(f"A szam1 egyenlo a szam2-vel")