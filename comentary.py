import numpy as np

# 5 puta se ucitava isti file na stari nacin...

#ovako jednom ucitam i koristim ga u memoriji kroz cijelu skrptu
whole_table = np.loadtxt('AquaticReport.txt', dtype='str', delimiter='|', skiprows=1)

#pogledaj dobro razliku izmedju array-a i python dictionary
#ovo je kao objekat u javascript-u
inputs = {
          'full': -1,
          'cas': 0,
          'analiza': 1,
          'ecotox': 2,
          'godina': 3,
          }

def get_column(table, column_num):
    # posto mi je inputs['full'] == -1 onda provjerim ako je manje onda mi vrati sve
    if column_num < 0:
        return whole_table
    # nije idealno... ima boljih nacina izvlacenja kolona odavde ali to ako ti se da sa numpy naci, jos bolje 
    column = []
    for row in whole_table:
        column.append(row[column_num])
    return column

choice = input("Odaberi koju kolonu da prikazem: 'cas', 'analiza', 'ecotox', 'godina', ili 'full' za sve 4: ")
# get_column mi vraca moju kolonu... inputs['choice'] mi je drugi argument (column_num)... 
# prvi argument mi je tabela
print(get_column(whole_table, inputs[choice]))