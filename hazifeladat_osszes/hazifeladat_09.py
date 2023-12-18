# hazi_feladat_09
henrik_kosarazik = input(f"Jön Henrik ma kosarazni? (igen/nem): ").lower()
hanna_kosarazik = input(f"Jön Hanna ma kosarazni? (igen/nem): ").lower()
if henrik_kosarazik == 'igen' and hanna_kosarazik == 'igen':
    print(f"Mindketten jönnek kosarazni.")
elif henrik_kosarazik == 'nem' and hanna_kosarazik == 'nem':
    print(f"Egyikük sem jön kosarazni.")
else:
    print(f"Csak az egyikük jön kosarazni.")