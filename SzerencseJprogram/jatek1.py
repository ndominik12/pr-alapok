import random

def main():
    osszes = 0

    while True:
        veletlen_szam = random.randint(2, 22)
        print(f"Generált szám: {veletlen_szam}")
        if veletlen_szam in [2, 3, 4, 7, 8, 9, 10, 11]:
            print(f"benne van a nyerő lapokba")
            osszes += veletlen_szam

        valasz = input(f"Szeretnél még egy kártyát (igen/nem)? ").lower()
        if valasz != "igen":
        
            break

if __name__ == "__main__":
    main()