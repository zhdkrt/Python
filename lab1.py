# task1
var1 = input()
var2 = input()
var3 = input()
var4 = input()
var5 = input()

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

var6 = int(input())
var7 = float(input())
var8 = int(input())
var9 = int(input())
var10 = bool(input())

print(f"{type(var6)} {var6}")
print(f"{type(var7)} {var7}")
print(f"{type(var8)} {var8}")
print(f"{type(var9)} {var9}")
print(f"{type(var10)} {var10}")

# task2
a,b,c = 2,3,4

print(b)
print(a)

res1 = a + b
res2 = c - a
res3 = a * c
res4 = c / a
res5 = c % b

a, b = b, a

print(f"{a} {b} {c} {res1} {res2} {res3} {res4} {res5}")

# task3
city = input("введите название города: ")
temp = input("введите температуру: ")
print(f"В городе {city} сейчас {temp} °C")

length = float(input("введите длину прямоугольника: "))
heigth = float(input("введите ширину прямоугольника: "))
print(f"площадь прямоугольника с длиной {length} и шириной {heigth} равна {length * heigth}")

price = float(input("введите стоимость: "))
count = int(input("введите количество: "))
print(f"Итоговая стоимость {count} товаров по цене {price} рублей составляет {round(count*price,3)} рублей.")

seconds = int(input("введите время в секундах: "))
print("Время {0} секунд — это {0} минут и {1} секунд".format(seconds, count) )

# task4

var_a = 34
var_b = 34
print(var_a is var_b)

var_c = 340
var_d = 340
print(var_c is var_d)

str_a = "artem"
str_b = "artem"
str_c = "art" + "em"
part = "em"
str_e = "art" + part

print(str_a is str_b)
print(str_a is str_c)
print(str_a is str_e)


#task 5
import time as t

time_a = t.localtime(t.time())

print(f"Текущая дата и время: {t.strftime("%Y-%m-%d %X", time_a)}")
print(f"Дата: {t.strftime("%d/%m/%Y", time_a)}")
print(f"Время: {t.strftime("%X",time_a)}")

print(f"Текущая дата и время: {t.strftime("%d.%m.%Y %X", time_a)}")
print(f"Дата: {t.strftime("%d %B %Y", time_a)}")
print(f"Время: {t.strftime("%H:%M",time_a)}")

#task 6
import math as m

degr = m.radians(float(input("введите угол в градусах: ")))
print(f"синус = {m.sin(degr)}, косинус = {m.cos(degr)}")


var = 0
print(bool(var))