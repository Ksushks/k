import numpy as np  # для работы с числами и массивами
import matplotlib.pyplot as plt  # для построения графиков

# Создаем фигуру с 3 графиками в ряд
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 1. График y = x²
x = np.linspace(0, 10, 50)
axes[0].plot(x, x**2)
axes[0].set_title("y = x²")  # заголовок
axes[0].grid()

# 2. Точечный график случайных точек
x_points = np.random.rand(50)  # 50 случайных чисел от 0 до 1
y_points = np.random.rand(50)
axes[1].scatter(x_points, y_points)
axes[1].set_title("Случайные точки")
axes[1].grid()

# 3. Столбчатая диаграмма
categories = ['A', 'B', 'C']
values = [3, 7, 2]
axes[2].bar(categories, values)
axes[2].set_title("Категории A, B, C")
axes[2].grid()

plt.tight_layout()  # автоматически настраивает отступы
plt.show()