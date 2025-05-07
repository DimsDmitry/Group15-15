import pandas as pd
df = pd.read_csv('GoogleApps.csv')

# Сколько стоит (Price) самое дешёвое платное приложение (Type == 'Paid)?
print(df[df['Type'] == 'Paid']['Price'].min())

# Чему равно медианное (median) количество установок (Installs)
# приложений из категории (Category) "ART_AND_DESIGN"?
print(df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median())


# На сколько максимальное количество отзывов (Reviews) для бесплатных приложений (Type == 'Free')
# больше максимального количества отзывов для платных приложений (Type == 'Paid')?
free = df[df['Type'] == 'Free']['Reviews'].max()
paid = df[df['Type'] == 'Paid']['Reviews'].max()

print('Разница в отзывах:', free-paid)


# Каков минимальный размер (Size) приложения для тинейджеров (Content Rating == 'Teen')?
result = df[df['Content Rating'] == 'Teen']['Size'].min()
print(round(result, 3))

# *К какой категории (Category) относится приложение с самым большим количеством отзывов (Reviews)?
result = df[df['Reviews'] == df['Reviews'].max()]['Category']
print(result)

# *Каков средний (mean) рейтинг (Rating) приложений стоимостью (Price) более 20 долларов и 
# с количеством установок (Installs) более 10000?
result = df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean()
print(result)
