import pandas as pd
df = pd.read_csv('Math_Test_Results_by_Grade.csv')

#Number Tested
print(round(df['Number Tested'].mean(), 2))
print(round(df['Number Tested'].median(), 2))
print(round(df['Number Tested'].max(), 2))
print(round(df['Number Tested'].min(), 2))

# Mean Scale Score
print(round(df['Mean Scale Score'].mean(), 2))
print(round(df['Mean Scale Score'].median(), 2))
print(round(df['Mean Scale Score'].max(), 2))
print(round(df['Mean Scale Score'].min(), 2))

#Black Mean Scale Score
black = df[df['Category'] == 'Black']
print(round(black['Mean Scale Score'].mean(), 2))
print(round(black['Mean Scale Score'].median(), 2))
print(round(black['Mean Scale Score'].max(), 2))
print(round(black['Mean Scale Score'].min(), 2))

#Level 1 %
print(round(df['Level 1 %'].mean(), 2))
print(round(df['Level 1 %'].median(), 2))
print(round(df['Level 1 %'].max(), 2))
print(round(df['Level 1 %'].min(), 2))
