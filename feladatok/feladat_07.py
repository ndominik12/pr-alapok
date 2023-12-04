# feladat_007
# dk9 109 oldal

"""
gondolt_szám := 4
ki: „gondoltam egy számra”
be: tipp
tipp átalakítása egésszé
elágazás
ha tipp = gondolt_szám:
ki: kétsoros dicséret
különben:
ki: ugratás
elágazás vége
ki: búcsú
"""

gondolt_szám = 4
tipp = input('Gondoltam egy számra. Tippeld meg! ')
tipp = int(tipp)
if tipp == gondolt_szám:
    print(f'Ügyes!')
    print(f'Gratulálok.')
else:
    print(f'Hosszan gondolkodtál rajta?:)')
    print(f'Nem érte meg.;)')
print(f'Pápá.')