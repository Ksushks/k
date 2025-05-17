# Импортируем необходимые модули
import random  # Для генерации случайного числа
import time    # Для измерения времени игры

# Загадываем случайное число от 1 до 100
secret_number = random.randint(1, 100)

# Инициализируем счетчик попыток
attempts = 0

# Запоминаем время начала игры
start_time = time.time()

# Выводим приветственное сообщение
print("Я загадал число от 1 до 100. Попробуй угадать!")

# Основной игровой цикл
while True:
    # Получаем ввод от пользователя
    user_input = input("Введи число: ")
    
    # Проверяем, хочет ли пользователь выйти
    if user_input.lower() == 'q':
        print(f"Игра окончена. Я загадал число {secret_number}.")
        break
        
    # Проверяем, что введено число
    if not user_input.isdigit():
        print("Пожалуйста, введи число!")
        continue  # Переходим к следующей итерации цикла
        
    # Преобразуем ввод в число
    guess = int(user_input)
    # Увеличиваем счетчик попыток
    attempts += 1
    
    # Сравниваем число пользователя с загаданным
    if guess < secret_number:
        print("Мое число больше!")
    elif guess > secret_number:
        print("Мое число меньше!")
    else:
        # Если угадали, вычисляем время игры
        game_time = round(time.time() - start_time, 1)
        print(f"Поздравляю! Ты угадал за {attempts} попыток и {game_time} секунд!")
        
        # Сохраняем результат в файл
        with open("/Users/ksenia/Desktop/все лабы /игра/game_results.txt", "a") as results_file:
            results_file.write(f"Попыток: {attempts}, Время: {game_time} сек\n")
        break