# Гипотеза: У мальчиков, чьи родители не имеют высшего образования, показатели математического теста хуже,
# чем у тех чьи родители имеют степень бакалавра
import pandas as pd
df = pd.read_csv('StudentsPerformance .csv')
no_bd = df[df['parental level of education'] == 'some college']
bd = df[df['parental level of education'] == "bachelor's degree"]
no_bd_children = no_bd['math score'].mean()
bd_children = bd['math score'].mean()
if no_bd_children < bd_children:
    print('True')
else:
    print('False')