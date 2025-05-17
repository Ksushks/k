import math
from abc import ABC, abstractmethod

# Абстрактный базовый класс для геометрических фигур
class Shape(ABC):
    @abstractmethod
    def area(self): #площадь
        pass
    
    @abstractmethod
    def perimeter(self): #периметр
        pass

# Класс прямоугольника
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)  
    
    def __str__(self):
        return f"Прямоугольник (ширина={self.width}, высота={self.height})"

# Класс круга
class Circle(Shape):
    def __init__(self, radius):  
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Круг (радиус={self.radius})"

# Класс треугольника
class Triangle(Shape):
    def __init__(self, side1, side2, side3):  
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        # Формула Герона
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        return f"Треугольник (стороны={self.side1}, {self.side2}, {self.side3})"

# Функция для вывода информации о фигуре
def print_shape_info(shape):
    print(shape)
    print(f"Площадь: {shape.area():.2f}")
    print(f"Периметр: {shape.perimeter():.2f}")
    print()

# Проверка
if __name__ == "__main__":
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Triangle(3, 4, 5)
    ]
    
    for shape in shapes:
        print_shape_info(shape)

