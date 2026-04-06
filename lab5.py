# Задание 1
# Создайте функцию convert_units(value, from_unit='meters', to_unit='feet'), которая преобразует значения между различными единицами измерения (например, метры в футы).
# Реализуйте поддержку нескольких единиц и добавьте возможность добавления новых единиц через аргументы.

def convert_units(value, from_unit='meters', to_unit='feet', **kwargs):
    units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'feet': 0.3048,
        'miles': 1609.344,
        'kilograms': 1000,
    }

    units.update(kwargs)

    return value * units[from_unit] / units[to_unit]

print(convert_units(2,'kilometers','meters'))
print(convert_units(2.5,'kilograms','grams', grams = 1))

# Задание 2
# Разработайте функцию median(*args), которая принимает переменное количество чисел и возвращает медиану. Убедитесь, что функция корректно обрабатывает четное количество чисел.

def median(*args):
    args = list(args)
    args.sort()

    if len(args) % 2 != 0:
        index = (len(args) // 2) 
        res = args[index]
    else:
        index = (len(args) // 2)
        res = (args[index] + args[index - 1]) / 2
    return res

print(median(2,3,9,4,6))
print(median(2,3,4,5,6,8,9,10))

# Задание 3
# Разработайте функцию classify_numbers(*args, threshold=0), которая принимает переменное количество чисел и возвращает список, разделенный на положительные, отрицательные и нулевые числа.
# Параметр threshold помогает определить, какие числа считать положительными.

def classify_numbers(*args, threshold = 0):
    positivs = []
    negativs = []
    zeros = []
    res = [positivs, negativs, zeros]

    for i in args:
        if i < threshold:
            res[1].append(i)
        elif i > threshold:
            res[0].append(i)
        else:
            res[2].append(i)
    
    for i in res:
        i.sort()

    return res

print(classify_numbers(-2, 5, -3, 12, -5, -9, -44, 0, 112, 43, 0))

# Задание 4
# Создайте функцию format_string(template, **kwargs), которая принимает строку-шаблон и словарь с параметрами.
# Функция должна заменять в шаблоне ключи из словаря на соответствующие значения.

def format_string(template, **kwargs):
    for key in kwargs:
        template = template.replace(f"{{{key}}}", str(kwargs[key]))

    return template

print(format_string("это строка {шаблон} для замены слов на {значения} из словаря", шаблон = "машина", значения = "стол"))

# Задание 5
# Создайте функцию generate_report(title, *sections, **options), которая принимает заголовок отчета, переменное количество секций и ключевые аргументы для настройки
# (например, author, date). Функция должна возвращать строку, представляющую отчет в формате:
# Отчет: {title}
# Автор: {author}
# Дата: {date}
# {sections}
# Если author и date не указаны, используйте значения по умолчанию: "Неизвестен" для автора и "Сегодня" для даты.

def generate_report(title, *sections, **options):
    author = options.get("author", "Неизвестно")
    date = options.get("date", "Сегодня")
    sections = '\n'.join(sections)

    return f"Отчет: {title}\nАвтор: {author}\nДата: {date}\n{sections}"
     
print(generate_report("№1", "введение", "итог", "выводы", author="Артём", date="2026-04-05"))

# Задание 6
# Создайте модуль с функцией convert_units(value, from_unit='meters', to_unit='feet'), которая преобразует значения между различными единицами измерения (например, метры в футы).
# Реализуйте поддержку нескольких единиц и добавьте возможность добавления новых единиц через аргументы.
import myModule as mm

# Задание 7
# Напишите модуль lists, в котором содержится 5 функций:
# 1)Функция randomList, принимающую 1 аргумент n - длина списка. Которая возвращает список данной длины, заполненной случайными числами от -99 до 99.
# 2)Функция randomMatrix, принимающую 1 аргумент n – длина двумерного списка NxN. Которая возвращает двумерный список данной длины, заполненный случайными числами от 0 до 9.
# 3)Функция maxLength, принимает 1 аргумент X – список, состоящий из слов. Функция должна определить самое длинное слова в списке. Функция должна вернуть данное слова.
# 4)Функция currentSums, принимающая 1 аргумент X – список чисел. Функция возвращает новый массив из такого же числа элементов, в котором на каждой позиции будет находиться сумма элементов списка X до этой позиции включительно.
# 5)Функция threeSimbol, принимающая 1 аргумент S – предложение. Функция создает список, элементы которого будут состоять из строк, каждый элемент состоит из 3 последовательный символов предложения.
# Подключите модуль с своему файлу и проверьте как работают функции.
import lists as l

print (l.randomList(10))

print (l.randomMatrix(3))

print(l.maxLength(['a','bb','dddddd','ccc','gggg']))

print(l.currentSums([1,2,3,4,5]))

print(l.threeSimbol('строка для разбиения'))

# Задание 8
# Напишите функцию capitalize_strings, которая принимает строку и возвращает преобразованной таким образом, чтобы первая буква в ней была большая,
# а остальные - маленькие (вспоминаем методы строк).
# Создайте список из 5 строк, введенных пользователем с клавиатуры.
# Используйте функцию map, чтобы ко всем строкам из списка применить функцию capitalize_strings. Результат вывести на экран.

def capitalize_strings(s):
    s = s.capitalize()

    return s

strList = []

for i in range(5):
    temp = input(f"Введите стркку №{i + 1}: ")
    strList.append(temp)

res = list(map(capitalize_strings,strList))

for i in res:
    print(i)


# Задание 9
# Создайте список с 15 произвольными числами от -100 до 100.
# Напишите функцию kratno_10, которая принимает число и возвращает True, когда число кратно 10, иначе - False.
# Используйте функцию filter, чтобы ко всем числам из списка применить функцию kratno_10.
# Создайте ещё 2 любые функции на проверку кратности числа на любое другое (2, 3, 4, 5, 11, 100 или другие). Примените их к списку используя функцию filter.
import random as rand

l1 = [rand.randint(-100,100) for x in range(15)]

def kratno_10(num):
    if num % 10 == 0:
        return True
    else:
        return False
    
res10 = list(filter(kratno_10, l1))
print(f"Кратно 10: {res10}")

def kratno_5(num):
    if num % 5 == 0:
        return True
    else:
        return False

res5 = list(filter(kratno_5, l1))
print(f"Кратно 5: {res5}")


def kratno_4(num):
    if num % 4 == 0:
        return True
    else:
        return False

res4 = list(filter(kratno_4, l1))
print(f"Кратно 4: {res4}")


# Задание 10
# Дан список чисел, например [1, 2, 3, 4]. Напишите программу, которая вычисляет их произведение, используя reduce().
from functools import reduce

numLst = [1,2,3,4]

def cmps(x, y):
    return x * y

res = reduce(cmps,numLst)

print(res)

# Задание 11
# Используя функцию sorted(), напишите программу, которая сортирует список строк по их длине.
strLst = ['aaa','bb','cccccc','dddd','ee','f']

def sort_lenghts(s):
    return len(s)

sortedStr = sorted(strLst, key = sort_lenghts)

print(sortedStr)

# Задание 12
# Дан список оценок студентов 15 студентов по контрольной (каждая оценка — это случайное число от 1 до 10).
# Используя лямбда-выражения, необходимо:
# Найти все оценки, которые больше или равны 4.
# Найти среднюю оценку студентов.
# Найти минимальную и максимальную оценки.
# Найти количество студентов с оценками выше среднего.
marks = [rand.randint(1,10) for x in range(15)]
print(marks)

lowMarks = list(filter(lambda x: x >= 4, marks))
print(lowMarks)

avgMarks = reduce(lambda x, y: x + y, marks) / len(marks) 
print(avgMarks)

minMaxMarks = lambda x: (max(x), min(x))
print(minMaxMarks(marks))

countStudents = len(list(filter(lambda x: x >= avgMarks, marks)))
print(countStudents)

# Задание 13
# Напишите декоратор timer, который выводит время выполнения функции. Примените его к функции, которая выполняет долгие вычисления (например, вычисление факториала большого числа).
import  time as t
def time_decor(func):
    def wrapper(*args, **kwargs):
        startTime = t.time()
        result = func(*args, **kwargs)
        endTime = t.time()

        print(f"Время выполнения: {endTime - startTime:.5f} секунд")
        return result
    return wrapper

def factoriall(n):
    if n == 0:
        return 1
    else:
        return n * factoriall(n-1)

@time_decor
def factorial(n):
    return factoriall(n)
    
print(factorial(500))


# Задание 14
# Напишите функцию second, создающую по заданному списку строк новый список, в котором содержатся те же строки, что и в исходном списке, по каждая вторая строка выброшена из списка
# (т.е. в списке останутся только строки с нечетными номерами), а в каждой из оставшихся строк удален каждый второй символ. 
# Например, если аргументом программы является список строк
# ["Близнецами", "называется", "пара", "натуральных", "чисел"] 
# то результатом работы должен быть список строк
# ["Бинцм", "пр", "чсл"]

words = ["Близнецами", "называется", "пара", "натуральных", "чисел"]
def second(strings):
    filt = strings[::2]
    res = [s[::2] for s in filt]

    return res

print(second(words))
    
# Задание 15
# Напишите функцию invers, которая вычисляет количество инверсий в заданном списке элементов. 
# Инверсией называется пара элементов списка, в которой первый элемент имеет в списке меньший индекс, чем индекс второго элемента, но больше его по значению. 
# Например в списке [3,5,7,6,8,5] инверсию образуют пары (7,6), (7,5), (6,5) и (8,5) — всего четыре инверсии.
lst = [3, 5, 7, 6, 8, 5]

def invers(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                count += 1
    return count

print(invers(lst))