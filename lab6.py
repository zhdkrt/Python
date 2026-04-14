# Задание 1
# Создайте текстовый файл example.txt и запишите в него несколько строк текста на русском языке.
# Откройте файл example.txt в режиме чтения и считайте из него данные 4 разными способами. Выведите полученные данные на экран.
with open('example1.txt','w', encoding='utf-8') as file:
    file.write('текстText1\n')
    file.write('текстText2\n')
    file.write('текстText3\n')

with open('example1.txt', 'r', encoding='utf-8') as file:
    res1 = file.read()

res2 = []
with open('example1.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    while line:
        res2.append(line.strip())
        line = file.readline()

res3 = []
with open('example1.txt','r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        res3.append(line.strip())

res4 = []
with open('example1.txt','r', encoding='utf-8') as file:
    for line in file:
        res4.append(line.strip())

print(res1,res2,res3,res4, sep='\n')

# Задание 2
# Напишите программу, которая анализирует текстовый файл и выводит следующие статистические данные:
# Общее количество слов.
# Общее количество уникальных слов.
# Самое длинное слово и его длина.
# Самое короткое слово и его длина.
import re

with open('example2.txt','r',encoding='utf-8') as file:
    text = file.read()

cleanText = re.sub(r'[^\w\s]', '', text)

textList = cleanText.lower().split(' ')
print(textList)
print(f"общее количество слов: {len(textList)}")

textUnique = set(textList)
print(f"уникальное количество слов: {len(textUnique)}")

maxWord = max(textList, key=len)
print(f"самое длинное слово: {maxWord} c длиной {len(maxWord)}")

minWord = min(textList, key=len)
print(f"самое короткое слово: {minWord} c длиной {len(minWord)}")

# Задание 3
# Напишите программу, которая ищет все вхождения слова “казнить” в текстовом файле и заменяет их на слово “помиловать”, при этом учитывая регистр оригинального слова.
# Программа должна сохранять изменения в том же файле.

text = """Судья вынес приговор: казнить нельзя помиловать.
Королева приказала: Казнить всех преступников немедленно!
Народ требовал: КАЗНИТЬ изменника без суда!
Адвокат настаивал: нельзя казнить человека без доказательств.
Летописец записал: "КАЗНИТЬ или помиловать — вот в чём вопрос."
Указ гласил: Казнить — значит проявить слабость правителя.
Мудрец говорил: казнить легко, простить — труднее."""

with open('example3.txt', 'w', encoding='utf-8') as file:
    file.write(text)

with open('example3.txt','r',encoding='utf-8') as file:
    text = file.read()

def wordSwap(word):
    origWord = word.group()
    replaceWord = 'помиловать'

    if origWord.isupper():
        return replaceWord.upper()
    elif origWord.istitle():
        return replaceWord.capitalize()
    else:
        return replaceWord

replacedText = re.sub(r'казнить', wordSwap, text)

with open('example3.txt', 'w', encoding='utf-8' ) as file:
    file.write(replacedText)

# Задание 4
# Создайте программу, которая объединяет несколько три текстовых файла в один. Программа должна запрашивать у пользователя имена файлов для объединения и имя выходного файла.
# При объединении необходимо удалить дубликаты строк и сохранить порядок появления строк.
fileName1 = input('введите имя первого файла: ')
fileName2 = input('введите имя второго файла: ')
fileName3 = input('введите имя третьего файла: ')
finalName = input('введите имя выходного файла: ')

lines = []

for fileName in [fileName1,fileName2,fileName3]:
    with open(fileName, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line not in lines:
                lines.append(line)

with open(finalName,'w', encoding='utf-8') as file:
    file.write('\n'.join(lines))

# Задание 5
# Создайте файл с некоторым содержимым, например, data.txt.
# Импортируйте модуль os.
# Измените название файла data.txt на datadatadata.txt,
# Используя удалите файл datadatadata.txt с диска.
# Проверьте, что файл успешно удален, попытавшись открыть его в режиме чтения.
import os
text = "Судья вынес приговор: казнить нельзя помиловать."

with open('example5.txt', 'w', encoding='utf-8') as file:
    file.write(text)

os.rename('example5.txt','example5example5example5.txt')
os.remove('example5example5example5.txt')

try:
    with open('example5example5example5.txt', 'r') as file:
        text = file.read()
except:
    print('файл не существует')

# Задание 6
# Напишите программу, которая спрашивает сколько папок надо создать = N. 
# После этого создает в папке PRIM нужное количество папок с именами prim1, prim2, … primN.
# Удалите папки с именами prim2 и prim4.
N = int(input('введите количество папок'))

if not os.path.exists('PRIM'):
    os.mkdir('PRIM')

for i in range(1, N + 1):
    if not os.path.exists(f'PRIM/prim{i}'):
        os.mkdir(f'PRIM/prim{i}')

if os.path.isdir('PRIM/prim2'):
    os.rmdir('PRIM/prim2')

if os.path.isdir('PRIM/prim4'):
    os.rmdir('PRIM/prim4')

# Задание 7
# Напишите программу, которая читает JSON-файл, содержащий информацию о студентах (имя, возраст, оценки). Программа должна выводить:
# Общее количество студентов.
# Средний возраст студентов.
# Студентов с оценками выше 90.
import json

with open('students.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

countStudents = len(data)
print(f"количество студентов: {countStudents}")

avgYears = 0

for st in data:
    avgYears += st["age"]

avgYears = avgYears/len(data)
print(f"средний возраст: {avgYears}")

print("имена студентов с оценкой выше 90")
for st in data:
    if st["grade"] >= 90:
        print(st["name"])

# Задание 8
# Создайте программу, которая загружает JSON-файл с информацией о товарах (название, цена, количество на складе), добавляет новый товар и обновляет количество существующего товара.
# После изменений программа должна записать обновленные данные обратно в тот же файл.
products = [
    {"name": "Ноутбук", "price": 1200.00, "count": 15},
    {"name": "Смартфон", "price": 800.00,  "count": 30},
    {"name": "Наушники", "price": 150.00,  "count": 50},
    {"name": "Клавиатура", "price": 75.00,   "count": 40},
    {"name": "Монитор", "price": 400.00,  "count": 20}
]

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(products, file, ensure_ascii = False, indent=4)

with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

print("до изменений:")
for p in data:
    print(f"{p['name']}, цена: {p['price']}$, склад: {p['count']} шт.")

newProduct = {"name": "Мышь", "price": 45.00, "count": 60}
data.append(newProduct)

updateName = "Смартфон"
newCount = 25

for product in data:
    if product["name"] == updateName:
        product["count"] = newCount
        break

with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("после изменений:")
for p in data:
    print(f"{p['name']}, цена: {p['price']}$, склад: {p['count']} шт.")

# Задание 9
# Создайте словарь, содержащий некоторые данные, например, информацию о пользователе.
# Импортируйте модуль pickle.
# С помощью функции pickle.dump() сериализуйте словарь в файл с расширением .pickle.
# Затем считайте содержимое файла обратно с помощью функции pickle.load() и выведите его на экран.
import pickle as p

user = {"name": "Артём Жидик", "age": 20, "email": "artemzhidik@gmail.com", "city": "Baranovichi"}

with open('user.pickle', 'wb') as file:
    p.dump(user, file)

with open('user.pickle', 'rb') as file:
    result = p.load(file)

print("данные из файла:")
for key, value in result.items():
    print(f"{key}: {value}")

# Задание 10
# Импортируйте модуль shelve.
# Создайте файл базы данных mydata.db с помощью функции shelve.open().
# Добавьте в базу данных несколько записей, используя ключи и значения. Закройте базу данных.
# Вновь откройте базу данных mydata.db и получите значение по ключу. Выведите полученное значение на экран.
import shelve as sh

with sh.open('mydata.db') as db:
    db['name'] = 'Artem'
    db['age'] = 20
    db['city'] = 'baranovichi'

with sh.open('mydata.db') as db:
    print(f"имя: {db['name']}, возраст: {db['age']}")

# Задание 11
# Создайте базу данных ВАШЕГО ВАРИАНТА SQLite3 с помощью модуля sqlite3.
# Создайте перечисленные таблицы и установите связи. 
# Вставьте несколько записей в КАЖДУЮ таблицу, используя оператор INSERT INTO.
# Сохраните изменения в базе данных и закройте соединение.

# База данных студентов
# Хранит информацию о студентах, курсах и преподавателях.
# student: id, name, birth_date, course_id
#  course: id, name, professor_id
#  professor: id, name, department
# student.course_id -> course.id, 
# course.professor_id -> professor.id

import sqlite3 as sql

conn = sql.connect('univer.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS professor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT NOT NULL
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS course (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        professor_id INTEGER,
        FOREIGN KEY (professor_id) REFERENCES professor(id)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_date TEXT NOT NULL,
        course_id INTEGER,
        FOREIGN KEY (course_id) REFERENCES course(id)
    )
''')

cur.executemany('INSERT INTO professor (name, department) VALUES (?, ?)', [
    ('Иванов Иван Иванович', 'Кафедра информатики'),
    ('Петрова Мария Сергеевна', 'Кафедра математики'),
    ('Сидоров Алексей Петрович', 'Кафедра физики'),
])

cur.executemany('INSERT INTO course (name, professor_id) VALUES (?, ?)', [
    ('Python программирование', 1),
    ('Высшая математика', 2),
    ('Физика', 3),
    ('Базы данных', 1),
])

cur.executemany('INSERT INTO student (name, birth_date, course_id) VALUES (?, ?, ?)', [
    ('Артём Жидик','2006-02-10', 1),
    ('Карелина Вероника','2005-10-15', 2),
    ('Лелеш Богдан', '2006-06-31', 1),
])

conn.commit()
conn.close()

# Подключитесь к базе данных SQLite3.
# Используя оператор SELECT, выполните запрос к одной из таблиц и получите все записи. Выведите полученные данные на экран.
# Приведите 3 примера различных запросов данных из таблиц с использованием WHERE. Выведите полученные данные на экран.
# Объедините в новом запросе две таблицы и выведите полученную информацию.
conn = sql.connect('univer.db')
cur = conn.cursor()

cur.execute('SELECT * FROM student')

for row in cur.fetchall():
    print(row)

cur.execute('SELECT name, birth_date FROM student WHERE course_id = 1')
for row in cur.fetchall():
    print(row)

cur.execute("SELECT name FROM professor WHERE department = 'Кафедра информатики'")
for row in cur.fetchall():
    print(row)

cur.execute("SELECT name, birth_date FROM student WHERE birth_date > '2004-01-01'")
for row in cur.fetchall():
    print(row)

cur.execute('''
    SELECT student.name, course.name, professor.name
    FROM student
    JOIN course ON student.course_id = course.id
    JOIN professor ON course.professor_id = professor.id
''')

for row in cur.fetchall():
    print(f"Студент: {row[0]}, Курс: {row[1]}, Преподаватель: {row[2]}")

conn.close()

# Подключитесь к базе данных SQLite3.
# Используя оператор UPDATE, обновите данные в таблице.
# Сохраните изменения в базе данных и закройте соединение.
conn = sql.connect('univer.db')
cur = conn.cursor()

cur.execute("UPDATE student SET course_id = 4 WHERE name = 'Мария Козлова'")

conn.commit()
conn.close()

# Подключитесь к существующей базе данных SQLite3.
# Используя оператор DELETE, удалите определенные записи из таблицы (по какому-то критерию).
# Сохраните изменения в базе данных и закройте соединение.
conn = sql.connect('univer.db')
cur = conn.cursor()

cur.execute("DELETE FROM student WHERE birth_date < '2004-01-01'")

conn.commit()
conn.close()