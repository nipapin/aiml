import numpy as np
import pandas as pd

samples = 200
city_names = np.array(["Москва", "Казань", "Омск"])
cities = np.random.choice(city_names, samples)
prices = np.random.uniform(100, 1000,(samples,)).round(2)
quantities = np.random.randint(1, 20, (samples,))

df = pd.DataFrame({'Город': cities,'Цена': prices,'Количество': quantities})
df['Выручка'] = df['Цена'] * df['Количество']

print(df.head())
print(df.shape)
print(df.describe())

large_salary = df[df['Выручка'] > 5000]
large_salary_sorted = large_salary.sort_values('Выручка', ascending=False)
print(large_salary_sorted.head())

#Для каждого города посчитайте суммарную выручку и среднюю цену.

salary_by_city = df.groupby("Город")["Выручка"].sum()
avg_price_per_city = df.groupby("Город")["Цена"].mean()

print(salary_by_city)
print(avg_price_per_city)

highest_salary = salary_by_city.sort_values(ascending=False)

print(highest_salary.index[0])

assert abs(by_city.sum() - df['выручка'].sum()) < 1e-6
print('Проверка пройдена')
