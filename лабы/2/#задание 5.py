#задание 5.5
# Создаем список чисел от 1 до 20
numbers = list(range(1, 21))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

increased_numbers = list(map(lambda x: x + 10, even_numbers))

sorted_numbers = sorted(increased_numbers, reverse=True)

# Выводим результаты
print(numbers)
print(even_numbers)
print(increased_numbers)
print(sorted_numbers)