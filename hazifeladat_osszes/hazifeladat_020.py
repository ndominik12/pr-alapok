# 5x5-ös mező létrehozása és feltöltése
mező = [['.']*5 for _ in range(5)]
# Főátlóra kerülő "O" karakterek beállítása
for i in range(5):
    mező[i][i] = 'O'
# Mező kiírása
for sor in mező:
    print(' '.join(sor))