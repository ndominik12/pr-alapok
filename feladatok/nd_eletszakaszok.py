# Keresztnev bekérése
keresztnev = input(f"Kérem, adja meg a keresztnevét: ")
# Életkor bekérése
eletkor = int(input(f"Kérem, adja meg az életkorát: "))
# Életszakasz
if eletkor < 1:
    ertek = "csecsemő"
elif eletkor <= 6:
    ertek = "kisgyerek"
elif eletkor <= 12:
    ertek = "gyerek"
elif eletkor <= 16:
    ertek = "serdülő"
elif eletkor <= 25:
    ertek = "ifjú"
elif eletkor < 65:
    ertek = "felnőtt"
else:
    ertek = "nyugdíjas"
# Eredmények kiírása a koráról
print(f" {keresztnev} a kora alapján: {ertek}")