class Student:
    def __init__(self, name, student_id):
        # Инициализация объекта студента
        self.name = name          # Хранит имя студента
        self.student_id = student_id  # Хранит ID студента
        self.grades = []          # Пустой список для хранения оценок

    def add_grade(self, grade):
        # Добавление оценки с проверкой 
        if grade >= 0 and grade <= 10:  # Проверка что оценка от 0 до 10
            self.grades.append(grade)    # Добавление валидной оценки
            return True
        else:
            print("Ошибка! Такой оценки нет!")  # Сообщение об ошибке
            return False

    def get_average(self):
        # Расчет среднего балла
        if not self.grades:       # Если нет оценок
            return 0
        else:
            return sum(self.grades) / len(self.grades)  # Вычисление среднего

    def display_info(self):
        # Вывод информации 
        print(f"Имя: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Оценки: {', '.join(map(str, self.grades))}")
        print(f"Средний балл: {self.get_average():.1f}")  # Округление 

    def __str__(self):
        # Строковое представление объекта
        return f"Student(name='{self.name}', id={self.student_id}, grades={self.grades}, avg={self.get_average():.2f})"
    
    def __eq__(self, other):
        # Сравнение студентов по ID
        if isinstance(other, Student):  # Проверка что other - объект Student
            return self.student_id == other.student_id
        return False
    
    def __len__(self):
        # Возвращает количество оценок
        return len(self.grades)

# Создание и тестирование объекта студента
s = Student("Илон", "22831")  # Создаем студента
s.add_grade(8)                # Добавляем оценки
s.add_grade(9)
s.add_grade(7)
s.display_info()              # Выводим информацию
print(s)                      
print(f"Количество оценок: {len(s)}")