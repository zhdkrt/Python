# Задание 7
# Напишите модуль lists, в котором содержится 5 функций:
# 1)Функция randomList, принимающую 1 аргумент n - длина списка. Которая возвращает список данной длины, заполненной случайными числами от -99 до 99.
# 2)Функция randomMatrix, принимающую 1 аргумент n – длина двумерного списка NxN. Которая возвращает двумерный список данной длины, заполненный случайными числами от 0 до 9.
# 3)Функция maxLength, принимает 1 аргумент X – список, состоящий из слов. Функция должна определить самое длинное слова в списке. Функция должна вернуть данное слова.
# 4)Функция currentSums, принимающая 1 аргумент X – список чисел. Функция возвращает новый массив из такого же числа элементов, в котором на каждой позиции будет находиться сумма элементов списка X до этой позиции включительно.
# 5)Функция threeSimbol, принимающая 1 аргумент S – предложение. Функция создает список, элементы которого будут состоять из строк, каждый элемент состоит из 3 последовательный символов предложения.
# Подключите модуль с своему файлу и проверьте как работают функции.
import random as rand

def randomList(n):
    lst = [rand.randint(-99,99) for x in range(n)]
    
    return lst


def randomMatrix(n):
    lst = []
    for i in range(n):
        tempLst = [rand.randint(0,9) for x in range(n)]
        lst.append(tempLst)
    return lst


def maxLength(X):
    max = 0
    for i in X:
        if len(i) > max:
            max = len(i)
            word = i
        
    return word


def currentSums(X):
    newLst = []

    for i in range(len(X)):
        sum = 0
        for k in range(i + 1):
            sum += X[k]

        newLst.append(sum)
    return newLst


def threeSimbol(S):
    newLst = []
    a, b = 0, 3
    
    for x in range(0,len(S),3):
        newLst.append(S[x:x+3])
    
    return newLst