# Téglalap szélességének bekérése
szel = float(input(f"Kérem, adja meg a téglalap szélességét: "))
# Téglalap magasságának bekérése
mag = float(input(f"Kérem, adja meg a téglalap magasságát: "))
# Téglalap terület
terulet = szel * mag
# Állapot 
if szel == mag:
    allapot = "Ez egy négyzet"
elif szel > mag:
    allapot = "Ez egy fekvő téglalap"
else:
    allapot = "Ez egy álló téglalap"
# Eredmények a testről
print(f"A téglalap területe: {terulet}")
print(f"A téglalap állapota: {allapot}")