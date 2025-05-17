# Ввод трех целых чисел
a = int(input())  # первое число
b = int(input())  # второе число
c = int(input())  # третье число

# Определение и вывод максимального числа
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

# Определение и вывод минимального числа
if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)

# Проверка чисел на одинаковость/различие
if a == b == c:
    print("Одинаковые")
else:
    print("Разные")