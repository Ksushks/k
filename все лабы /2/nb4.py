# Открываем и читаем файл 
with open("/Users/ksenia/Desktop/все лабы /2/text.txt") as file:
    text = file.read()  # Сохраняем весь текст 

# Функция для поиска email
def find_emails(text):
    emails = []  # Создаем пустой список для email
    words = text.split()  # Разбиваем текст на отдельные слова
    for word in words:
        # Проверяем, содержит ли слово '@' и '.'
        if '@' in word and '.' in word:  
            # Добавляем слово в список
            emails.append(word.strip('.,!?'))  
    return emails  # Возвращаем найденные email

# Функция для поиска телефонных номеров
def find_phones(text):
    phones = []  # Создаем пустой список для телефонов
    words = text.split()  # Разбиваем текст на слова
    for word in words:
        # Проверяем, начинается ли слово с +7- и имеет длину 15 символов
        if word.startswith('+7-') and len(word) == 16:  
            # Добавляем номер в список
            phones.append(word.strip('.,!?'))  
    return phones  # Возвращаем найденные номера

# Функция для поиска слов, начинающихся с заглавной буквы
def find_capital_words(text):
    capital_words = []  # Создаем пустой список для слов
    words = text.split()  # Разбиваем текст на слова
    for word in words:
        # Проверяем, что слово не пустое и начинается с заглавной буквы
        if len(word) > 0 and word[0].isupper():  
            # Добавляем слово в список
            capital_words.append(word.strip('.,!?'))  
    return capital_words  # Возвращаем найденные слова

# Получаем списки email, телефонов и слов с заглавной буквы
emails = find_emails(text)
phones = find_phones(text)
capital_words = find_capital_words(text)

# Записываем email в файл
with open('/Users/ksenia/Desktop/все лабы /2/emails.txt', 'w') as file:
    for email in emails:  # Перебираем все email
        file.write(email + '\n')  # Записываем каждый email на новой строке

# Записываем телефоны в файл
with open('/Users/ksenia/Desktop/все лабы /2/phones.txt', 'w') as file:
    for phone in phones:  # Перебираем все телефоны
        file.write(phone + '\n')  # Записываем каждый телефон на новой строке

# Записываем слова с заглавной буквы в файл
with open('/Users/ksenia/Desktop/все лабы /2/capital_words.txt', 'w') as file:
    for word in capital_words:  # Перебираем все слова
        file.write(word + '\n')  # Записываем каждое слово на новой строке

# Выводим результаты в консоль
print("Найденные email-адреса:", emails)
print("Найденные номера телефонов:", phones)
print("Слова, начинающиеся с заглавной буквы:", capital_words)