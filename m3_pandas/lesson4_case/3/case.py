import pandas as pd

df = pd.read_csv('menu.csv')
# result = df[df['Calories'] <= 250]['Category']
# print(result)

result = df[(df['Calories'] <= 500) & (df['Category'] == 'Breakfast')]['Item']
print(result)

