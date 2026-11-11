import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

true_slope = 3
true_intercept = 5
samples = 100

#Создайте 100 значений x: случайные числа от 0 до 10.
values = np.random.randint(0, 11, (samples,))

#Создайте y = 3 * x + 5 + шум, где шум это случайное число от -2 до 2 (своё для каждой точки).
noise = np.random.uniform(-2, 2, (samples,))
y = 3 * values + 5 * noise

#Положите x и y в таблицу DataFrame. Выведите первые 5 строк.
df = pd.DataFrame({'X':values,'Y':y})
print(df.head())

#Посмотрите на данные: нарисуйте точечный график средствами pandas (df.plot).
df.plot(kind='scatter', x='X', y='Y', title='y = 3 * x + 5 + noise')

#Посчитайте коэффициент корреляции Пирсона между x и y.
pirson_factor = stats.pearsonr(values, y)
print(pirson_factor.statistic)

#Найдите линейную регрессию: наклон, сдвиг и R². Выведите их рядом с истинными значениями 3 и 5.
lrg = stats.linregress(values, y)
print(lrg.slope, lrg.intercept, lrg.rvalue ** 2)
print(lrg.slope, ' against :', true_slope)
print(lrg.intercept, ' against :', true_intercept)

#Нарисуйте точки и красную линию регрессии на одном графике.
reg_x = np.linspace(0, 10, samples)
reg_y = lrg.slope * reg_x + lrg.intercept

plt.figure(figsize=(8, 5))

plt.scatter(df['X'], df['Y'], color='blue', alpha=0.6, label='y = 3 * x + 5 + noise')

plt.plot(reg_x, reg_y, color='red', linewidth=2, label='R')

plt.title('Summury')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

plt.show()
