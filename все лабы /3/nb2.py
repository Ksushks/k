# Базовый класс 
class Person:
    def __init__(self, name, age):
        self.name = name  # Имя 
        self.age = age    # Возраст 

# Класс преподавателя 
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Инициализация 
        self.subject = subject       # Преподаваемый предмет
        self.students = []          # Список студентов
    
    # Добавление студента к преподавателю
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Студент {student.name} добавлен к преподавателю {self.name}")
        else:
            print(f"Студент {student.name} уже в списке {self.name}")
    
    # Удаление студента из списка
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} удален у преподавателя {self.name}")
        else:
            print(f"Студент {student.name} не найден в списке")

    # Вывод списка студентов
    def list_students(self):
        print(f"Студенты преподавателя {self.name} ({self.subject}):")
        for student in self.students:
            print(f"  - {student.name}")

# Класс студента 
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # Инициализация родительского класса
        self.student_id = student_id  # Уникальный ID студента
# Пример использования
t = Teacher("Иванова", 40, "Математика")
s1 = Student("Петров", 20, "S001")
s2 = Student("Сидорова", 19, "S002")

t.add_student(s1)
t.add_student(s2)
t.list_students()
    

