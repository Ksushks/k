import numpy as np  # для работы с числами и массивами
import matplotlib.pyplot as plt  # для построения графиков
data = np.random.normal(0, 1, 1000)
# Строим гистограмму
plt.figure(figsize=(10, 5))
plt.hist(data, bins=20, edgecolor='black')  # bins — количество столбцов
plt.title("Гистограмма случайных данных")  # заголовок
plt.xlabel("Значение")  # подпись оси X
plt.ylabel("Количество")  # подпись оси Y
plt.grid()  # сетка
plt.show()