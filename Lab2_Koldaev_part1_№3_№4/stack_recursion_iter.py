import math

#task_stack №3
stack = []
N = 10  # число элементов стека

def Push(open):
    if len(stack) == N:  # проверка переполнения стека
        return 1
    stack.append(open)
    return 0

def Pop():
    if len(stack) == 0:
        return 1
    stack.pop()
    return 0

def balanced(s):
    open, close = "(", ")"
    stack.clear()
    for c in s:
        if c == open:
            br = Push(open)
            if br == 1:
                print("Стек переполнен!\n")
                break
        elif c == close:
            br = Pop()
            if br == 1:
                print("Стек пуст!\n")
                return False

    return len(stack) == 0

def task_stack():
    while True:
        print('Введите строку (для выхода введите пробел): ')
        s = input()
        if s == ' ':
            break
        print(balanced(s))


#task_recursion №4
def recursion1(n):
    if (n <= -1):  # проверка того, что значение отрицательно + выход из программы
        return -1
    if (n == 0):
        return 1
    b = 1/n*recursion1(n-1)*2
    return b

def task_recursion():
    n = 5  # n-й член последовательности
    print(recursion1(n))


#task_recursion №6
# заполнение массива через рекурсию
arr1 = []
def recursion2(n):
    if (n == 0):
        return 1
    b = 1/n*recursion2(n-1)*2
    arr1.append(b)
    return b

def task_array1():
    n = 5
    recursion2(n)
    print(arr1)


#task_iter №6
# Заполнение массива итерационно (через цикл)
def iter(n):
    arr = []
    arr.append(2.0)
    for i in range(n-1):
        arr.append(arr[i]*2/(i+2))
    return arr

def task_array2():
    n = 5
    arr = iter(n)
    print(arr)


task_stack()
task_recursion()
task_array1()
task_array2()

