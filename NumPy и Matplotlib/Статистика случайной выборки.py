import numpy as np
import matplotlib.pyplot as plt

#Сгенерируйте 1000 случайных «температур» в диапазоне от 10 до 40 градусов

samples = 1000
inputs = np.random.uniform(10, 40, (1000, ))

#Выведите форму массива, среднее, минимум и максимум.
inputs_min = np.min(inputs)
inputs_max = np.max(inputs)
inputs_avg = np.mean(inputs)
print(inputs.shape, inputs_min, inputs_max, inputs_avg)

#Посчитайте, сколько значений выше среднего.
count_above = np.sum(inputs > inputs_avg)
print(count_above)

#Выведите индексы первых 5 таких значений.
above_avg_idxs = np.where(inputs > inputs_avg)[0]
print(above_avg_idxs[:5])

#Приведите значения к диапазону от 0 до 1 по формуле (x - min) / (max - min)
inputs_normalized = (inputs - inputs_min) / (inputs_max - inputs_min)
print(inputs_normalized[:5])

#Выведите минимум и максимум нового массива.

print(np.min(inputs_normalized), np.max(inputs_normalized))

#Постройте две гистограммы рядом: до нормировки и после. У каждой нужны заголовок, подписи осей и сетка.
plt.figure(figsize=(12, 5))

# Левый график (До нормировки)
plt.subplot(1, 2, 1)
plt.hist(inputs, bins=20, color='orange', edgecolor='black')
plt.title('До нормировки')
plt.xlabel("Температура")
plt.ylabel("Количество значений")
plt.grid(True)

# Правый график (После нормировки)
plt.subplot(1, 2, 2)
plt.hist(inputs_normalized, bins=20, color='green', edgecolor='black')
plt.title('После нормировки')
plt.xlabel("Нормированная температура")
plt.ylabel("Количество значений")
plt.grid(True)

# Отображаем оба графика
plt.tight_layout()
plt.show()
