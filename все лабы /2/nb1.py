# Открываем файл 
with open("/Users/ksenia/Desktop/все лабы /2/data.txt") as file:
    # Читаем файл построчно
    for line in file:
        # Преобразуем все числа из файла в список целых чисел
        num = list(map(int, file.read().split()))
        # Выводим полученный список чисел
        print(num)
        
        # Вычисляем сумму всех чисел
        suma = sum(num)
        # Подсчитываем количество чисел
        cn = len(num)
        # Вычисляем среднее значение
        srz = sum(num) // cn
        # Находим максимальное значение
        maxi = max(num)
        # Находим минимальное значение
        mini = min(num)
        
        # Выводим результаты вычислений
        print(suma)
        print(srz)
        print(maxi)
        print(mini)

# Открываем файл для записи результатов
with open("/Users/ksenia/Desktop/все лабы /2/result.txt", "w") as file:
    # Записываем сумму чисел
    file.writelines([f"Сумма:{suma}\n"])
    # Записываем максимальное значение
    file.writelines([f"Максимальное значение:{maxi}\n"])
    # Записываем минимальное значение
    file.writelines([f"Минимальное значение:{mini}\n"])
    # Записываем среднее значение
    file.writelines([f"Среднее значение:{srz}\n"])

# Закрываем файлы 
file.close()
file.close()
    






    

        


        
        

    
