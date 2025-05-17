import numpy as np  # для работы с числами и массивами
import matplotlib.pyplot as plt  # для построения графиков

# Создаем матрицу 5×5 со случайными числами от 1 до 10
matrix = np.random.randint(1, 11, size=(5, 5))

# Выводим матрицу
print("Матрица 5×5:")
print(matrix)

# Находим среднее значение
print("\nСреднее значение:", np.mean(matrix))

# Находим максимум и минимум
print("Максимальный элемент:", np.max(matrix))
print("Минимальный элемент:", np.min(matrix))

# Сумма по столбцам (axis=0 — столбцы, axis=1 — строки)
print("Сумма по столбцам:", np.sum(matrix, axis=0))

plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='viridis')  # рисуем тепловую карту
plt.colorbar()  # добавляем шкалу цветов
plt.title("Тепловая карта матрицы")

# Добавляем числа в ячейки
for i in range(5):  # перебираем строки
    for j in range(5):  # перебираем столбцы
        plt.text(j, i, matrix[i, j], ha='center', va='center', color='white')

plt.show()