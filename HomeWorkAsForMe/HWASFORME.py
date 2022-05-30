a = "220"
print(a * 3)  # дублирование строки необходимое количество раз
print(len('example'))  # длина строки, определяет количественно длинну строки  LEN
ex = "baranov"  # выборочно вызвает элемент переменной который указываем
print(ex[6])
print(ex[-1])
srez = "AndrewBaranov"
print(srez[3:6])
print(srez[3::2])  # Интервал
a, b, c = 'HelloKitty!', 'HelloAndrew', 'Helloteacher'
print(a[0:-1])  # вопрос для преподавателя, захватывает до предпоследнего значения игрик !!!!!!!!!!!!
print(a[0])
print(a[-1])  # Захватывает до последнего значения до восклицательного знака !!!!!!!!!!
print(b[0])
print(b[-1])
print(b[0::2])  # Интервал !!!
# Generator of the list
a = []
for i in range(1, 9):
    a.append(i)
print(a[0::2])
# NEW topick  IF
print("Hello!")
print("Hello!")
a = 3
b = 2
if a < b:
    print("a меньше, чем b")
    print("a точно меньше, them b")

print("Вне блока if")
c = 3
d = 4
if c >= d:
    print("c либо больше, чем d, либо равняется d")
    print("said")
else:
    print("c menshe, them d")
print("without block if")
e = 7
f = 8
if e < f:
    print("e less, then d")
names = ['Andrew', 'Lena', 'Olha', 'Karina']
print(names[-3], names[-2], names[-1])
# Version 1
a = []
for i in range(101, 169):
    if i % 2 == 1:
        a.append(i)
print(a)
# Version 2
b = []
for i in range(1, 99):
    if i % 2 == 1:
        b.append(i)
print(b)
# Version 3
x = list(range(1001, 1090, 2))
print(x)
# Дан одномерный массив числовых значений, насчитывающий N элементов
# Определить имеются ли в массиве два подряд идущих нуля.
from random import randint

a = [randint(0, 10) for i in range(int(input('n=0')))]
for i in range(len(a)):
    if a[i] == 0 and a[i + 1] == 0:
        print('Yes')
# 2) Дан массив чисел. Вместо каждого элемента с нулевым значением
# поставить сумму двух предыдущих элементов массива.
n = input().split()
for i in range(len(n)):
    n[i] = int(n[i])

for i in range(2, len(n)):
    if n[i] == 0:
        n[i] = n[i - 1] + n[i - 2]
print(n)
# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Из элементов исходного массива построить два новых.
# В первый должны входить только положительные элементы,
# а во второй только отрицательные элементы.
a = list(map(int, input().split()))

apos = [i for i in a if i > 0]
aneg = [i for i in a if i < 0]

print(apos)
print(aneg)


# Дан массив числовых значений.
# После каждого отрицательного элемента вставить новый элемент,
# равный квадрату этого отрицательного элемента.
# Все нули исключить.
# Поменять местами первую и вторую половины нового массива.
def otr(mas):
    x = []
    for i in mas:
        x.append(i)
        if i < 0:
            x.append(0)
    return x


# Узнать что такое блок-схема, узнать что такое сортировка пузырьком.
# Составить полную блок схему сортировки пузырьком.
count = 0
while count < 6:
    print(count)
cpunt += 2

# рандомный номер
import random

rand_number = random.randint(1, 100)
x = input()
while x != rand_number:
    print('try once again')
    break
if x == rand_number:
    print('GOOD')
# money back
money = 10
while money > 0:
    # noinspection PyUnresolvedReferences
    print('We have' + str(money) + " dollars")
    money -= 1
while money == 0:
    print('no more money, time to work')
    break
# password programm
password = '123'
password = input()
while password != '123':
    print('pls, try once again!')
    password = input()
print('good job')

import random

# выбор ранломного числа
number = random.randint(1, 6)
guesses = 0
while guesses < 5:
    print('enter a number from 1 to 6:')
    guess = int(input())
    guesses += 1
    if guesses == 1:
        print('u have four times to try')
    if guess == number:
        print('WIN')
        break
    if guesses == 2:
        print('u have three times to try')
    if guess == number:
        print('WIN')
        break
    if guesses == 3:
        print('u have two times to try once again')
    if guess == number:
        print('WIN')
        break
    if guesses == 4:
        print('u have last try to win')
    if guess == number:
        print('WIN')
        break
    if guesses == 5:
        print('LoSE!')
        break
    if guess == number:
        print('WIN')
        break

# weeks
week_days = ["sun", "mon", "tue", "wed", "Thu", "fri", "sat"]
x = (input())
for i in range(len(week_days)):
    print(week_days[i])

# summ of range numbers
numbers = list(range(1, 100))
s = 0
for i in numbers:
    s += i
print(s)
total_sum = 0
for i in range(1, 100):
    if i % 3 == 0:
        total_sum += i
print(total_sum)


# массивы (tuple - картеж) [list] {dict} - key


def hello():
    print('hello')


hello()


def xxx(x: str):
    return 'hello', x


print(xxx('username'))


def summ(x, y):
    return x + y


print(summ(2, 4))


def calc(x, y):
    return x + y


print(calc(2, 19))


# calculator
def calc():
    print('Enter firs number')
    x = int(input())
    if type(x) != int:
        print('enter')
    print('enter second number')
    y = int(input())
    return x + y


print(calc())


nums = [1, 2, 3, 4, 5]


def multiply(x):
    return x * 10


new_nums = list(map(multiply, nums))
    print(new_nums)



numbers = [1,2,3,4,5]
def check(x)


total2 = 0
i1 = 0
while i1 < 5:
    total2 += i1
    i1 += 1

    print(total2)


total2 = 0
i1 = 0
while i1 < 5:
    total2 += i1
    i1 += 1
    print(total2)

# List of numbers SUMM ALL NUMBERS LIKE +0
my_list = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15]
total3 = 0  # SUMM
i2 = 0  # SCHETCHIK
while my_list[i2] > 0:  # пока в этом списке число больше чем ноль мы считаем ---
    total3 += my_list[i2]
    i2 += 1
total4 = 0
for element in my_list:
    if element <= 0:
        break
    total4 += element
    print(total3)
    print(total4)

# summ numbers like summ < then 10
my_list5 = [7, 5, 4, 4, 3, 2, 1, -5, -10, -15]
total5 = 0  # peremennaya acum
i5 = 0  # peremennaya schetchik
while total5 < 10 and my_list5[i5] > 0:
    total5 += my_list5[i5]
    i5 += 1
    print(i5)
    print(total5)


contin = 'k'
while contin == 'k':
    num1 = float(input("Enter u first number"))
    operation = input("enter u operation")
    num2 = float(input("enter u second number"))
    if operation == '+':
        print('Summ of numbers is:' + str(float(num1 + num2)))
    elif operation == '-':
        print('subtraction of numbers is:' + str(float(num1 - num2)))
    elif operation == '*':
        print('calculation is:' + str(float(num1 * num2)))
    elif operation == '/':
        print('calculation is:' + str(float(num1 / num2)))
    else:
        print("Error")
    contin = input("Enter

    import turtle as window

    window.pensize(4)
    window.pencolor('red')

    window.forward(100)
    window.right(90)
    window.forward(100)
    window.right(90)
    window.forward(100)
    window.right(90)
    window.forward(100)

    window.mainloop()

import turtle

t = turtle.Turtle()

for c in ['red', 'red', 'red', 'red']:
    t.color(c)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.up()
    t.forward(200)
    t.exitonclick()
