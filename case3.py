# Гипотеза: В среднем блюда из категории "Breakfast" более калорийный, чем все блюда
import pandas as pd
df = pd.read_csv('menu.csv')
breakfast = df[df['Category'] == 'Breakfast']

bf = breakfast['Calories'].mean()
all = df['Calories'].mean()

if bf > all:
    print('True')
else:
    print('False')