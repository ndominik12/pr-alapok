# 7x7-es mező létrehozása és feltöltése
mező = [['.']*7 for _ in range(7)]
# Főátlóra és mellékátlóra kerülő "O" karakterek beállítása
for i in range(7):
    mező[i][i] = 'O'
    mező[i][6-i] = 'O'
# Mező kiírása
for sor in mező:
    print(' '.join(sor))