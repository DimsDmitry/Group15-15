import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# 1 Сколько всего приложений с категорией ('Category') 'BUSINESS'?
res = df['Category'].value_counts()['BUSINESS']
print(res)
# 2 Чему равно соотношение количества приложений для подростков ('Teen') и для детей старше 10 ('Everyone 10+')?
# Ответ запиши с точностью до сотых.
table = df['Content Rating'].value_counts()
res = table['Teen']/table['Everyone 10+']
print(round(res, 2))


print('\n' + 100 * '=' + '\n')
# 3.1 Чему равен средний рейтинг ('Rating') платных ('Paid') приложений? 
# Ответ запиши с точностью до сотых.
res = df.groupby(by='Type')['Rating'].mean()
print(round(res['Paid'], 2))

# 3.2 На сколько средний рейтинг ('Rating') бесплатных ('Free') приложений меньше среднего рейтинга платных ('Paid')?
# Ответ запиши с точностью до сотых.
res = res['Paid'] - res['Free']
print(round(res, 2))

# 4 Чему равен минимальный и максимальный размер ('Size') приложений в категории ('Category') 'COMICS'?
# Запиши ответы с точностью до сотых.
res = df.groupby(by='Category')['Size'].agg(['min', 'max'])
print(round(res['min'][5], 2))
print(round(res['max'][5], 2))

print('\n' + 100 * '=' + '\n')
# Бонус 1. Сколько приложений с рейтингом ('Rating') строго больше 4.5 в категории ('Category') 'FINANCE'?
res = df[df['Rating'] > 4.5]['Category'].value_counts()
print(res['FINANCE'])

# Бонус 2. Чему равно соотношение бесплатных ('Free') и платных ('Paid') игр с рейтингом ('Rating') больше 4.9?
res = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]['Type'].value_counts()
print(res['Free']/res['Paid'])
