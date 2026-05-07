# Задание 1
# Класс Student
class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []
    def add_grade(self, grade):
        self.grades.append(grade)
    def show_grades(self):
        print(f'Оценки студента {self.name}: {self.grades}')
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nВозраст: {self.age}\nОценки: {self.grades}'

# Класс Car
class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def show_info(self):
        print(f'Автомобиль {self.brand} {self.model}')
        print(f'Скорость: {self.speed} км/ч')
        print(f'Год выпуска: {self.year}')

    def __str__(self):
        return f'Бренд: {self.brand}\nМодель: {self.model}\nСкорость: {self.speed}\nГод выпуска: {self.year}'

while True:
    print('\n===== МЕНЮ =====')
    print('1. Создать студента')
    print('2. Создать машину')
    print('3. Выход')

    choice = input('Выберите пункт: ')

    if choice == '1':
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        age = int(input('Введите возраст: '))

        student = Student(name, surname, age)

        while True:
            grade = input('Введите оценку (или stop для завершения): ')

            if grade.lower() == 'stop':
                break

            student.add_grade(int(grade))

        print('\nИнформация о студенте:')
        print(student)

        student.show_grades()

    elif choice == '2':
        brand = input('Введите бренд: ')
        model = input('Введите модель: ')
        speed = int(input('Введите скорость: '))
        year = int(input('Введите год выпуска: '))

        car = Car(brand, model, speed, year)

        print('\nИнформация об автомобиле:')
        print(car)

        car.show_info()

    elif choice == '3':
        print('Программа завершена.')
        break

    else:
        print('Неверный пункт меню!')

# Задание 2
import math
# Класс Circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Круг: радиус = {self.radius}'
    
# Класс Rectangle

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f'Прямоугольник: {self.width} x {self.height}'

# Класс Triangle

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def __str__(self):
        return f'Треугольник: стороны {self.a}, {self.b}, {self.c}'

while True:
    print("\n===== МЕНЮ =====")
    print("1. Круг")
    print("2. Прямоугольник")
    print("3. Треугольник")
    print("4. Выход")

    choice = input("Выберите фигуру: ")

    if choice == "1":
        r = float(input("Введите радиус: "))
        circle = Circle(r)

        print(circle)
        print("Площадь:", circle.area())
        print("Периметр:", circle.perimeter())

    elif choice == "2":
        w = float(input("Введите ширину: "))
        h = float(input("Введите высоту: "))
        rect = Rectangle(w, h)

        print(rect)
        print("Площадь:", rect.area())
        print("Периметр:", rect.perimeter())


    elif choice == "3":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))

        triangle = Triangle(a, b, c)

        print(triangle)
        print("Площадь:", triangle.area())
        print("Периметр:", triangle.perimeter())

    elif choice == "4":
        print("Выход...")
        break

    else:
        print("Неверный выбор!")