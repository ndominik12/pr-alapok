# Adatbekérés while-ciklussal (adatkérés megszakítása ENTER-rel)

szo = None
while szo != '':
    szo = input('Adj meg szavakat! Ha kilépnél, a szó helyett csak egy ENTER-t üss! ')    
    print(szo)
print('Program vége!')