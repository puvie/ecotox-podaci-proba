import numpy as np

# ovdje sam iskoristio fajl gdje imaju samo 4 vrste podataka: 
# CAS broj, Chemical Analysis, ECOTOX broj i godina publikacije
# na osnovu ovih podataka nema se sta izvuci (srednja vrijednost, devijacija i sl)
# al to svakako nije nesto pretjerano tesko, malo sam se igrao s tim i nije problem stvarno
# jedina razlika bi bila da dtype gdje izvlacis takve podatke mora biti int ili float

cijelaTabela = np.loadtxt('AquaticReport.txt', dtype='str', delimiter='|', skiprows=1)
casBroj = np.loadtxt('AquaticReport.txt', dtype='str', usecols = 0, delimiter='|', skiprows=1)
hemAnaliza = np.loadtxt('AquaticReport.txt', dtype='str', usecols = 1, delimiter='|', skiprows=1)
ecotoxBroj = np.loadtxt('AquaticReport.txt', dtype='str', usecols = 2, delimiter='|', skiprows=1)
godPublikacije = np.loadtxt('AquaticReport.txt', dtype='str', usecols = 3, delimiter='|', skiprows=1)

choice = input("Odaberi koju kolonu da prikazem: 'cas', 'analiza', 'ecotox', 'godina', ili 'full' za sve 4: ")
if choice == "full":
    print(cijelaTabela)
elif choice == "cas":
    for cas in casBroj:
        print(cas)
elif choice == "analiza":
    for analiza in hemAnaliza:
        print(analiza)
elif choice == "ecotox":
    for eco in ecotoxBroj:
        print(eco)
elif choice == "godina":
    for god in godPublikacije:
        print(god)
else:
    print("Nepoznata komanda")