#задание 1
a=int(input())
b=int(input())
c=int(input())
# 2,3,4 строки - ввод чисел
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
# цикл определяющий максимальное число
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)
#цикл определящий минимальное число 
if a==b==c:
    print("Одинаковые")
else:
    print("Разные")
#цикл которые сравниввает числа и выдает текст в зависимости от чисел 
