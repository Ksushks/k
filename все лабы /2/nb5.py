# 1. Создаем список чисел от 1 до 20
numbers = list(range(1, 21))  # Генерация последовательности [1, 2, 3, ..., 20]

# 2. Фильтрация четных чисел из списка
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Оставляем только четные числа

# 3. Увеличение каждого четного числа на 10
increased_numbers = list(map(lambda x: x + 10, even_numbers))  # Прибавляем 10 к каждому элементу

# 4. Сортировка полученных чисел в обратном порядке
sorted_numbers = sorted(increased_numbers, reverse=True)  # Сортируем по убыванию

# Выводим результаты каждого этапа обработки
print("Исходный список чисел:", numbers)
print("Четные числа из списка:", even_numbers)
print("Четные числа, увеличенные на 10:", increased_numbers)
print("Отсортированный результат по убыванию:", sorted_numbers)