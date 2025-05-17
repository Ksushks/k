import random  # Импортируем модуль для генерации случайных чисел

# Функция для выдачи случайной карты от 2 до 11
def draw_card():
    return random.randint(2, 11)  # Возвращает случайное число от 2 до 11

# Функция для подсчета суммы карт
def get_total(cards_list):
    # Если всего 2 карты и их сумма 21 — это Blackjack, возвращаем 0 как специальное обозначение
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0  
    return sum(cards_list)  # Возвращаем сумму карт

# Функция для определения победителя
def determine_winner(user_score, opponent_score):
    # Если игрок перебрал (больше 21), он автоматически проиграл
    if user_score > 21:
        return "Перебор! Противник выиграл."
    # Если противник перебрал, игрок выигрывает
    if opponent_score > 21:
        return "Противник перебрал! Игрок выиграл."
    # Если счёты равны, это ничья
    if user_score == opponent_score:
        return "Ничья!"
    # Если у игрока Blackjack, он побеждает
    if user_score == 0:
        return "Игрок выиграл с Blackjack!"
    # Если у противника Blackjack, он побеждает
    if opponent_score == 0:
        return "Противник выиграл с Blackjack!"
    # Сравниваем очки: у кого больше — тот и выигрывает
    return "Игрок выиграл!" if user_score > opponent_score else "Противник выиграл!"

# Основная функция для игры
def start_game():
    # Создаем списки для карт игрока и противника
    user_hand = [draw_card(), draw_card()]  # Две случайные карты для игрока
    opponent_hand = [draw_card(), draw_card()]  # Две случайные карты для противника
    
    # Игровой цикл игрока
    while True:
        # Считаем очки игрока и противника
        user_score = get_total(user_hand)
        opponent_score = get_total(opponent_hand)
        
        # Показываем карты игрока и первую карту противника
        print(f"Карты игрока: {user_hand}, сумма: {user_score}")
        print(f"Первая карта противника: {opponent_hand[0]}")

        # Проверяем условия окончания игры
        # Если у игрока Blackjack или перебор, игра заканчивается
        if user_score >= 21 or opponent_score == 0:
            break

        # Спрашиваем у игрока, хочет ли он взять ещё карту
        action = input("Взять карту? (+/-): ").strip()

        # Если игрок выбрал "+", добавляем ещё одну карту
        if action == "+":
            user_hand.append(draw_card())
        # Если "-", заканчиваем ход игрока
        else:
            break

    # Ход противника — пока у него меньше 17 очков, он берет карты
    while opponent_score < 17 and opponent_score != 0:
        opponent_hand.append(draw_card())
        opponent_score = get_total(opponent_hand)

    # Показываем финальные карты и очки игрока и противника
    print(f"Карты игрока: {user_hand}, сумма: {user_score}")
    print(f"Карты противника: {opponent_hand}, сумма: {opponent_score}")

    # Определяем и выводим победителя
    print(determine_winner(user_score, opponent_score))

# Основная функция программы
def main():
    print("Добро пожаловать в игру '21 очко'!")  # Приветствие

    # Бесконечный цикл для игры
    while input("Начать игру? (да/нет): ").strip().lower() == "да":
        start_game()  # Запуск новой игры

    print("Спасибо за игру!")  # Прощание при выходе из игры

# Условие для запуска программы
if __name__ == "__main__":
    main()