# Задание 1
# Используя списки и их методы, а также знания, полученные в предыдущих лабораторных работах решите задачу своего варианта.
# Создайте программу «Менеджер игр». В списке хранятся игры. Пользователю бесконечно (пока он не введёт «конец») предлагается выбрать действие:
# •	добавить игру в список
# •	вывести на экран весь список
# •	вывести количество игр
# •	удалить игру по названию
# •	удалить игру по индексу
# •	заменить одну игру на другую (по названию)
# •	добавить несколько игр (вводятся через запятую в одну строку)
# •	получить комбинацию из N (введённое с клавиатуры, проверяется, что оно меньше общего числа игр) случайных игр из списка.

import random as rand
gamesList = ['игра1','игра2','игра3']
flag = True
menu = '''
1 - вывести на экран весь список
2 - вывести количество игр
3 - удалить игру по названию
4 - удалить игру по индексу
5 - заменить одну игру на другую
6 - добавить несколько игр
7 - получить комбинацию из N случайных игр из списка.
конец - выход из менеджера
'''
while (flag):
    print(menu)
    
    action = input("введите действие: ").lower()

    match action:
        case "1":
            for game in gamesList:
                print(game)
        case "2":
            print("количество игр:", len(gamesList))
        case "3":
            gameName = input("введите название игры: ")
            if gameName in gamesList:
                gamesList.remove(gameName)
            else:
                print("игры нет в списке")
        case "4":
            gameIndex = int(input("введите номер игры: "))
            gamesList.pop(gameIndex - 1)
        case "5":
            gameName = input("введитк название игры: ")
            gameFind = input("введите название игры которую надо заменить: ")
            if gameFind in gamesList:
                gamesList[gamesList.index(gameFind)] = gameName
            else:
                print("введенной игры нет в списке")
        case "6":
            gamesNames = input("введите название игр, которые нужно добавить: ")
            newGamesList = gamesNames.split(" ")
            gamesList.extend(newGamesList)
        case "7":
            N = int(input("введите количество игр: "))
            print(" ".join(rand.sample(gamesList, N)))
        case "конец":
            flag = False
        case _:
            print("выберите существующее действие!")
        
# Задание 2
# Используя списочные выражения создайте и выведите на экран ( при помощи цикла) списки вашего варианта.

# СГЕНЕРИРУЙТЕ список Х из всех нечетных чисел от 1 до 15.
X = list(range(1,16,2))
print(X)

# Пользователь вводит строки в переменные S1 и S2.
# Необходимо СГЕНЕРИРОВАТЬ списки из всех букв строк соответственно. 
# Соедините получившиеся списки в новый, выведите его на экран и укажите сколько в нём элементов.
S1 = input("введите строку S1: ")
S2 = input("введите строку S2: ")

L1,L2 = list(S1), list(S2)

L3 = L1.copy()
L3.extend(L2)

print(L3)

print(len(L2))
for elem in L3:
    print(elem, end = "")

# Необходимо СГЕНЕРИРОВАТЬ список, состоящий только из чётных элементов Х.
L1 = []

L1 = X[1::2]

print(L1)

# Дан список  s = [10, -5, -15, 1, -42, 31] и список о = [22, -8, 44, 101, -4, 8] Необходимо СГЕНЕРИРОВАТЬ:
s, o = [10,-5,-15,1,-42,31], [22,-8,44,101,-4,8]


# Список, состоящий из суммы элементов списков s и о.
L = []
for element in range(len(s)):
    L.append(s[element] + o[element])

print(L)

# Список, состоящий из произведения элементов списков s и о.
L = []
for element in range(len(s)):
    L.append(s[element] * o[element])

print(L)

# Список, состоящий из положительных элементов списков s и о.
L = []

for element in range(len(s)):
    if s[element] > 0:
        L.append(s[element])

for element in range(len(o)):
    if o[element] > 0:
        L.append(o[element])

print(L)

# Список, состоящий из отрицательных элементов списков s и о.
L = []

for element in range(len(s)):
    if s[element] < 0:
        L.append(s[element])

for element in range(len(o)):
    if o[element] < 0:
        L.append(o[element])

print(L)

# Список, состоящий из отрицательных элементов списка s и положительных элементов списка о.
L = []

for element in range(len(s)):
    if s[element] < 0:
        L.append(s[element])

for element in range(len(o)):
    if o[element] > 0:
        L.append(o[element])

print(L)

# Задание 3
# Проходит турнир по танцам. Каждый участник имеет порядковый номер от 0 до 5. Турнир судят 4 тренера, каждый выставляет оценку от 1 до 10.
# Итоги конкурса записаны в двумерный список ( у вас он должен заполняться случайным образом) 
# А = [  [ 9, 9, 10, 8  ],
# [ 8, 7, 5, 5   ],
# [ 6, 4, 5, 8 ], 
# [ 10, 9, 10, 10  ],
#  	[ 9, 9, 10, 8 ],
# [ 7, 6, 8, 10  ], ]
# в этом списке каждая строчка соответствует участнику, а столбец - тренеру. Т.е. участник с номером 0 получил оценки [ 9, 9, 10, 8  ].
players, trainers = 6, 4

L = []

for i in range(players):
    player = []
    for k in range(trainers):
        mark = rand.randint(1,10)
        player.append(mark)
    L.append(player)

print(L)

# Определите и запишите в новый ОДНОМЕРНЫЙ список Н итоговый балл (сумму всех оценок) каждого участника турнира.
results = []
for i in L:
    results.append(sum(i))

print(results)

# Выведите номер и количество баллов участника, который победил (набрал больше всего баллов).
print(f"Номер участника: {results.index(max(results))}, количество баллов: {max(results)}")

# Определите самого строго и самого лояльного члена жюри ( кто суммарно поставил минимальное количество баллов и максимальное соответственно).
# Выведите их порядковые номера на экран.
trainersMark = []

for i in range(trainers):
    trainerMark = 0
    for k in range(players):
        trainerMark += L[k][i]
    trainersMark.append(trainerMark)

print(trainersMark)

print(f"номер строгого тренера: {trainersMark.index(max(trainersMark))}, номер лояльного тренера: {trainersMark.index(min(trainersMark))}")

# Задание 4
# Создайте кортеж temp с дневной температурой каждого дня марта. 
# В кортеже должно быть 31 случайное значений от -10 до 20.

L = []
for elem in range(31):
    L.append(rand.randint(-10,20))

temp = tuple(L)
print(temp)
print(len(temp))

# Сохраните в отдельные кортежи и выведите на экран значения температур по декадам ( в каждом по 10 значений, в последнем - 11).
temp1 = temp[:10]
temp2 = temp[10:20]
temp3 = temp[20:]
print(temp1)
print(temp2)
print(temp3)

# Выведите максимальную и минимальную температуру в каждой неделе неделе с соответствующей надписью. Укажите в какой день она была (0 – понедельник, 1 – вторник и т.д.)
weeks = [temp[:7], temp[7:14], temp[14:21], temp[21:28], temp[28:],]
day = ('пн','вт','ср','чт','пт','сб','вс')

for index, elem in enumerate(weeks):
    maxTemp = max(elem)
    minTemp = min(elem)

    maxDay = elem.index(maxTemp)
    minDay = elem.index(minTemp)

    print(f"неделя №{index + 1}")
    print(f"максимальная температуры = {maxTemp} была в {day[maxDay]}")
    print(f"минмальаня температура = {minTemp} была в {day[minDay]}")

# Найдите среднюю температуру за месяц и выведите её на экран. 
avgTemp = sum(temp)/len(temp)
print(avgTemp)

# Задание 5
# Решите представленные задачи с помощью словарей.

# 1. Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:
# •	0 на zero;
# •	1 на one;
# •	2 на two;
# •	3 на three;
# •	4 на four;
# •	5 на five;
# •	6 на six;
# •	7 на seven;
# •	8 на eight;
# •	9 на nine.

digits = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine"}

number = (input("введите натуральное число: "))

result = []
for digit in number:
    result.append(digits[int(digit)])

result = " ".join(result)
    
print(result)

# 3. На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
text = input("введите текст: ").lower()
text = text.split(" ")

words = {}

for word in text:
    words[word] = words.get(word, 0) + 1

minCount = min(words.values())

result = []

for word in words:
    count = words[word]
    if count == minCount:
        result.append(word)

print(min(result))

# Задание 6
# Используя методы и операции над множествами, решите три задачи своего варианта.
# Напишите программу для определения общего количества различных слов в строке текста.
text = input("введите текст: ")

words = text.split(" ")

s = set()
for word in words:
    s.add(word)

print(len(s))

# На вход программе подаются натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

n = int(input())


first = input().strip()
common = set(first)

for i in range(n - 1):
    num = input().strip()
    digits = set(num)
    common &= digits

for d in sorted(common):
    print(d, end=' ')

# Даны по 10-балльной шкале оценки по физике трех учеников. Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.
s1 = set(map(int, input("введите оценку первого ученика: ").split()))
s2 = set(map(int, input("введите оценку второго ученика: ").split()))
s3 = set(map(int, input("введите оценку третьего ученика: ").split()))

result = s3 - s1 - s2

for mark in sorted(result):
    print(mark, end=' ')

# Задание 7
# Подключите модуль collections. Решите представленные задачи используя namedtuple,defaultdic,Counter.
# Создайте программу, в которой вы будете использовать namedtuple из модуля collections для управления информацией о студентах. Определите именованный кортеж Student, который будет содержать поля: 
# name (имя студента),
# age (возраст студента), 
# grade (оценка студента) 
# email (электронная почта студента).
# Создайте список студентов, добавив несколько экземпляров Student. 
# Выведите информацию о всех студентах в удобочитаемом формате.
# Найдите и выведите информацию о конкретном студенте по его имени.
# Отредактируйте информацию об одном студенте.
# Реализуйте сортировку списка студентов по имени или возрасту и выведите отсортированный список.
from collections import namedtuple, defaultdict, Counter

Student = namedtuple("Student",["name","age","grade","email"])

students = [
    Student(name='Artem', age=20, grade=8, email='artemzhidik@gmail.com'),
    Student(name='Veronika',  age=20, grade=8.9, email='kanico228@gmail.com'),
    Student(name='Bogdan',  age=19, grade=6, email='bogomdan@gmail.com'),
]

for s in students:
    print(f'Имя: {s.name}, возраст: {s.age}, оценка: {s.grade}, email: {s.email}')

searchName = input("введите имя для поиска: ")
found = False
for s in students:
    if s.name == searchName:
        found = s
        break

if found:
    print(f'имя: {found.name}, возраст: {found.age}, оценка: {found.grade}, email: {found.email}')
else:
    print('студент не найден')

editName = 'Bogdan'
newEmail = 'lelesh@gmail.com'
newGrade = 7

for i, s in enumerate(students):
    if s.name == editName:
        students[i] = s._replace(email=newEmail, grade=newGrade)
        break

for s in students:
    print(f'имя: {s.name}, возраст: {s.age}, оценка: {s.grade}, email: {s.email}')

nameSort = sorted(students)

for s in nameSort:
    print(f'имя: {s.name}, возраст: {s.age}, оценка: {s.grade}, email: {s.email}')

# Создайте программу, в которой вы будете использовать defaultdict из модуля collections для учета посещаемости студентов в классе. 
# Создайте defaultdict, который будет хранить имена студентов в качестве ключей и количество их посещений в качестве значений.
# Добавьте несколько студентов и увеличьте их счетчик посещений на 1 при каждом добавлении.
# Выведите информацию о всех студентах и количестве их посещений.
# Найдите количество посещений для конкретного студента по его имени.
visits = defaultdict(int)

studentsToAdd = ['Artem', 'Veronika', 'Bogdan', 'Daniil', 'Arina', 'Andrey']

for name in studentsToAdd:
    visits[name] += 1

print('посещаемость студентов:')
for name, count in visits.items():
    print(f'{name}: {count}')

searchName = input('введите имя студента: ')
print(f'посещений у {searchName}: {visits[searchName]}')

# Создайте программу, в которой вы будете использовать Counter из модуля collections для анализа частоты слов в заданном тексте.
# Создайте строку текста и очистите ее от знаков препинания, приведя все слова к нижнему регистру.
# Используйте Counter для подсчета частоты каждого слова в тексте.
# Выведите 5 самых частых слов и их частоту.
# Найдите и выведите частоту конкретного слова из текста.
text = input("введите текст: ")

cleanedText = ""
for ch in text:
    if ch.isalnum() or ch.isspace():
        cleanedText += ch.lower()

words = cleanedText.split()

counter = Counter(words)

print("5 частых слов: ")
for word, freq in counter.most_common(5):
    print(word, "-", freq)

searchWord = input("введите слово для поиска частоты: ").lower()
print(f"частота слова '{searchWord}':", counter[searchWord])
