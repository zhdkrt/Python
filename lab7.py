# Задание 1.
# Создайте абстрактный класс Shape с методом calculate_area().
# Определите два класса, Circle и Rectangle, которые наследуются от Shape.
# В каждом из этих классов реализуйте метод calculate_area(), чтобы он возвращал площадь соответствующей фигуры.
# Создайте объекты Circle и Rectangle и вызовите их методы calculate_area().
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def calculate_area(self):
        return self.sideA * self.sideB


circ1 = Circle(10)
print(f"площадь окружности: {circ1.calculate_area()}")

rect1 = Rectangle(2,5)
print(f"площадь прямоугольника: {rect1.calculate_area()}")

# Задание 2.
# Создайте класс Animal с методом make_sound().
# Определите классы Dog, Cat и Cow, которые наследуются от Animal.
# В каждом из этих классов переопределите метод make_sound(), чтобы он возвращал соответствующий звук животного.
# Создайте список объектов разных типов (например, Dog, Cat и Cow) и вызовите для каждого объекта метод make_sound().
class Animal:
    def make_sound(self):
        return "животное говорит: "


class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + "гав-гав"
    

class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + "мяу-мяу"


class Cow(Animal):
    def make_sound(self):
        return super().make_sound() + "му-му"


animalList = [Dog(), Cat(), Cow()]

for animal in animalList:
    print(animal.make_sound())

# Задание 3.
# Создайте класс Person с закрытыми атрибутами name и age.
# Определите методы get_name(), set_name(), get_age() и set_age(), чтобы получить и установить значения атрибутов.
# Создайте объект класса Person и используйте методы для получения и установки значений атрибутов.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print('возраст введен неправильно')


pers1 = Person('Артём', 20)
print(f"имя: {pers1.get_name()}, возраст: {pers1.get_age()}")

pers1.set_name("Богдан")
pers1.set_age(19)

print(f"имя: {pers1.get_name()}, возраст: {pers1.get_age()}")

# Задание 4.
# Создайте класс Place с атрибутами area и address и методом to_sell(), который выводит сообщение о продаже данной недвижимости с указанием площади и адреса .
# Определите класс Apartment , который наследуется от Place и добавляет атрибут rooms.
# Определите класс House, который также наследуется от Place и добавляет атрибут floors.
# Создайте объекты Apartment и House и вызовите их методы.

class Place:
    def __init__(self, area, address):
        self.area = area
        self.address = address
    
    def to_sell(self):
        print(f"продается недвижимость {self.area}м2 по адресу: {self.address}")


class Apartment(Place):
    def __init__(self, area, address, rooms):
        super().__init__(area, address)
        self.rooms = rooms

    def to_sell(self):
        print(f"продается квартира {self.area}м2, {self.rooms} комнат, по адресу: {self.address}")


class House(Place):
    def __init__(self, area, address, floors):
        super().__init__(area, address)
        self.floors = floors
    
    def to_sell(self):
        print(f"продается дом {self.area}м2, {self.floors} этажей, по адресу: {self.address}")


apart1 = Apartment(70,'Академика Высоцкого 9', 3)
house1 = House(70,'Академика Высоцкого 9', 2)

apart1.to_sell()
house1.to_sell()

# Задание 5.
# Создайте класс Engine с методом start(), который выводит сообщение о запуске двигателя.
# Создайте класс Car с атрибутом engine, который будет экземпляром класса Engine.
# Определите метод start_engine(), который будет вызывать метод start() у объекта engine.
# Создайте объект класса Car и вызовите метод start_engine().

class Engine:
    def start(self):
        print("двигатель запущен")


class Car:
    def __init__(self):
        self.engine = Engine()
    
    def start_engine(self):
        self.engine.start()


car1 = Car()
car1.start_engine()

# Задание 6.
# Создайте класс Animal с атрибутами name и age.
# Определите класс Zoo с атрибутом animals, который будет списком объектов класса Animal.
# Реализуйте методы add_animal() и remove_animal() для добавления и удаления животных из списка.
# Создайте объект класса Zoo и добавьте несколько объектов класса Animal. Затем вызовите методы add_animal() и remove_animal().

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)

zoo = Zoo()

a1 = Animal("Барсик", 3)
a2 = Animal("Гром", 5)
a3 = Animal("Луна", 2)

zoo.add_animal(a1)
zoo.add_animal(a2)
zoo.add_animal(a3)

for animal in zoo.animals:
    print(animal.name, animal.age)

zoo.remove_animal(a2)

for animal in zoo.animals:
    print(animal.name, animal.age)