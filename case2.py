# Гипотеза: В стране Восточной Европы с самым маленьким население живет меньше людей, чем в среднем в каждой стране Океании
import pandas as pd
df = pd.read_csv('countries of the world.csv')
eeu = df[df['Region'] == 'EASTERN EUROPE                     ']
ocn = df[df['Region'] == 'OCEANIA                            ']

eepop = eeu['Population'].min()
ocnpop = ocn['Population'].mean()

if eepop < ocnpop:
    print('True')
else:
    print('False')