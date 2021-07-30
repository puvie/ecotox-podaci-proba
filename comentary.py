import numpy as np
#ovo je ostalo isto
whole_table = np.loadtxt('AquaticReport.txt', dtype='str', delimiter='|', skiprows=1)
#ovdje je dict al i key i value su str, vidjeces kasnie zasto
my_dict = {
    'cas' : '0',
    'ana' : '1',
    'tox' : '2',
    'god' : '3'  
}

x = input('Unesi keyword cas, ana, tox ili god // ili odg. broj (0,1,2,3): ')
#zbog ovoga ispod moraju oba biti str, pa ih prebacim u int da bi mogao kasnije napraviti kolonu

# prvi if provjerava je li jedan od keys napisan u input, ako jest, uzima njegov value 
# i prebacuje ga u int
if x in my_dict.keys():
    b = my_dict.get(x)
    b = np.int(b)
# drugi if provjerava je li jedan od values napisan u input, ako jest prebacuje taj value u int
elif x in my_dict.values():
    x=np.int(x)
    b=x
else:
    print("Nepoznat keyword")
#ovdje pravim kolonu od date vrijednosti u inputu
column_filter = whole_table[:, b]
#for jer printam element po element radi preglednosti
for element in column_filter:
    print(element)

