class BankAccount:
    def __init__(self):
        self._balance = 0       # Начальный баланс 
        self.history = []       # История операций
    
    def deposit(self, amount):
        """Пополнение счета"""
        if amount <= 0:
            print("Ошибка: сумма должна быть положительной")
            return
            
        self._balance += amount
        self.history.append(f"Пополнение: +{amount}")
        print(f"Баланс пополнен на {amount}. Текущий баланс: {self._balance}")
    
    def withdraw(self, amount): #cнятие
        if amount <= 0:
            print("Ошибка: сумма должна быть положительной")
            return
            
        if amount > self._balance:
            print("Ошибка: недостаточно средств")
            return
            
        self._balance -= amount
        self.history.append(f"Снятие: -{amount}")
        print(f"Снято {amount}. Текущий баланс: {self._balance}")
    
    def check_balance(self): #проверка баланс
        print(f"Текущий баланс: {self._balance}")
    
    def show_history(self): #история
        print("\nИстория операций:")
        for op in self.history:
            print(f"- {op}")

# Демонстрация работы
if __name__ == "__main__":
    print("Создаем новый счет...")
    account = BankAccount()
    
    print("\nТестируем пополнение:")
    account.deposit(1000)    # Успешно
    account.deposit(500)     # Успешно 
    account.deposit(-200)    # Ошибка
    
    print("\nТестируем снятие:")
    account.withdraw(300)    # Успешно
    account.withdraw(2000)   # Ошибка 
    account.withdraw(-100)   # Ошибка
    
    print("\nПроверяем состояние счета:")
    account.check_balance()
    account.show_history()