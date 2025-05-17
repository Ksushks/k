import numpy as np  # для работы с числами и массивами
import matplotlib.pyplot as plt  # для построения графиков
# Создаем массив x от 0 до 10 с 100 точками
x = np.linspace(0, 10, 100)

# Вычисляем sin(x) и cos(x)
y = np.sin(x)
z = np.cos(x)

# Создаем график
plt.figure(figsize=(10, 5))  # размер графика 
plt.plot(x, y, label='sin(x)')  # рисуем sin(x)
plt.plot(x, z, label='cos(x)')  # рисуем cos(x)
plt.title("Графики sin(x) и cos(x)")  # заголовок
plt.xlabel("x")  # подпись оси X
plt.ylabel("y")  # подпись оси Y
plt.legend()  # добавляем легенду
plt.grid()  # добавляем сетку
plt.show()  # показываем график