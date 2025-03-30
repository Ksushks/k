#задание 4 
with open("/Users/ksenia/Desktop/Новая папка/лабы/2/text.txt") as file:
    text = file.read()

def find_emails(text):
    emails = []
    words = text.split()  
    for word in words:
        if '@' in word and '.' in word:  
            emails.append(word.strip('.,!?'))  

def find_phones(text):
    phones = []
    words = text.split()  
    for word in words:
        if word.startswith('+7-') and len(word) == 15:  
            phones.append(word.strip('.,!?'))  
    return phones


def find_capital_words(text):
    capital_words = []
    words = text.split()  
    for word in words:
        if word[0].isupper():  
            capital_words.append(word.strip('.,!?'))  
    return capital_words


emails = find_emails(text)
phones = find_phones(text)
capital_words = find_capital_words(text)


with open('emails.txt', 'w', encoding='utf-8') as file:
    for emails in email:
        file.write(email + '\n')

with open('phones.txt', 'w', encoding='utf-8') as file:
    for phone in phones:
        file.write(phone + '\n')

with open('capital_words.txt', 'w', encoding='utf-8') as file:
    for word in capital_words:
        file.write(word + '\n')


print("Email-адреса:", emails)
print("Номера телефонов:", phones)
print("Слова, начинающиеся с заглавной буквы:", capital_words)