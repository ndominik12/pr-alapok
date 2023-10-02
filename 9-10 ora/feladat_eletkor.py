#Életkor bekérése a felhasználótól
eletkor = int(input("Kérem adja meg az életkorát: "))

#Életkor kategória megállapítása
if eletkor < 0:
    print(f" még nem születtél meg!")
elif eletkor < 5:
    print(f" még nem jársz általános iskolába!")
elif eletkor < 14:
    print(f" általános iskolába jársz!")
elif eletkor < 64:
    print(f" tanulsz vagy dolgozol!")
elif eletkor >= 65:
    print(f" nyugdíjas. ")