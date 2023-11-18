# Egy változóban eltárolunk egy szót
szo = "hello"

# Próbáljuk meg az int típussá konvertálni
try:
    szo_int = int(szo)
except ValueError as e:
    print(f"Hiba: {e}")
# A "hello" nem egy érvényes szám ezért nem lehet int tipussá konvertálni.