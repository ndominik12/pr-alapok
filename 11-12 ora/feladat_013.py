# be: szam
# ki: a szám negatív

"""
szam = int(input('Adj meg egy számot!'))
if szam < 0:
    print(f'A megadott szám {szam} negatív')
print(f'>> A program vége! <<')
"""

# be: szam
# ki: a szám negatív vagy nemnegatív

"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print('A megadott szám negatív.')
elif szam == 0:
    print('A megadott szám nulla.')
else:
    print('A megadott szám pozitív.')
print('>> A program vége! <<')
"""

# be: szam
# ki: a szám negatív vagy a szám pozitív vagy a szám 0

"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
else:
    print(f'A megadott szám {szam} pozitív.')
print('>> A program vége! <<')
"""

szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam < 0:
    print(f'A megadott szám {szam} pozitív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
print(f'>> A program vége! <<')