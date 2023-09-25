masodperc = int(input("a teszt eredménye : "))
if masodperc <= 15:
    print(f"Az elért eredmény szuper .")
elif masodperc <= 25:
    print(f"Az elért eredmény kitűnő .")
elif masodperc <= 35:
    print(f"Az elért eredmény jó .")
elif masodperc <= 45:
    print(f"Az elért eredmény közepes szint .")
elif masodperc <= 55:
    print(f"Az elért eredmény rossz .")
else:
    print(f"Az elért eredmény nagyon rossz .")