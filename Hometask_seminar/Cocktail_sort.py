import random
import time
import matplotlib.pyplot as plt
import math

def getRandomArray(n):
    array=[]
    for i in range(n):
        array.append(random.randint(0,1000))
    return array


def Cocktail_sort(A):
    left = 0
    right = len(A) - 1
    while left <= right:
        flags = 1
        for i in range(left, right, +1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                flags = 0
        right -= 1
        if flags == 1:
            break
        for i in range(right, left, -1):
            if A[i - 1] > A[i]:
                A[i], A[i - 1] = A[i - 1], A[i]
                flags = 0
        left += 1
        if flags == 1:
            break
    return A

def main():
    array_elements = [250, 500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000]  # число элементов для алгоритмов
    array_time_array = [] # массив времени выполнения сортировки для различного числа элементов (рандомный массив)
    array_time_array_sort = []  # массив времени выполнения сортировки для различного числа элементов (отсортированный массив)
    array_time_array_sort_reverse = []  # массив времени выполнения сортировки для различного числа элементов (реверсный массив)
    quantity_sort = 100
    for i in range(len(array_elements)):
        print(i)
        sum_time = 0  # сумарное время сортировки для нескольких запусков (рандомный массив)
        sum_time_sort = 0  # сумарное время сортировки для нескольких запусков (отсортированный массив)
        sum_time_sort_reverse = 0  # сумарное время сортировки для нескольких запусков (реверсный массив)
        array = getRandomArray(array_elements[i])  # генерация случайного массива
        array_sort = sorted(array, reverse=False)  # отсортированный массив
        array_sort_reverse = sorted(array, reverse=True)  # реверсный массив
        for j in range(quantity_sort):
            start_time = time.time()
            array_sort_reverse = Cocktail_sort(array_sort_reverse)
            end_time = time.time()
            sum_time_sort_reverse += (end_time - start_time)

            start_time = time.time()
            array = Cocktail_sort(array)
            end_time = time.time()
            sum_time += (end_time - start_time)

            start_time = time.time()
            array_sort = Cocktail_sort(array_sort)
            end_time = time.time()
            sum_time_sort += (end_time - start_time)

        print(array)
        print(array_sort)
        print(array_sort_reverse)
        array_time_array.append(sum_time)
        array_time_array_sort.append(sum_time_sort)
        array_time_array_sort_reverse.append(sum_time_sort_reverse)

    print("-— %s elements —-" % array_elements)
    print("-— %s time —-" % array_time_array)
    print("-— %s time —-" % array_time_array_sort)
    print("-— %s time —-" % array_time_array_sort_reverse)

    # график сложности, полученный на практике для сортировки (рандомный массив)
    plt.figure(0)
    plt.plot(array_elements, array_time_array)
    plt.title('random')

    # график сложности, полученный на практике для сортировки (отсортированный массив)
    plt.figure(1)
    plt.plot(array_elements, array_time_array_sort)
    plt.title('min_sort')

    # график сложности, полученный на практике для сортировки (реверсный массив)
    plt.figure(2)
    plt.plot(array_elements, array_time_array_sort_reverse)
    plt.title('max_revers')

    # график сложности, полученный на практике для сортировки (все три массива)
    plt.figure(4)
    plt.plot(array_elements, array_time_array)
    plt.plot(array_elements, array_time_array_sort)
    plt.plot(array_elements, array_time_array_sort_reverse)
    plt.title('all_graph')

    # график сложности теоретический для сортировки (в лучшем исходе)
    for i in range(len(array_elements)):
        array_time_array[i] = array_elements[i]
    plt.figure(3)
    plt.plot(array_elements, array_time_array)
    plt.title('sort_analitic')

    # график сложности теоретический для сортировки (в худшем исходе)
    for i in range(len(array_elements)):
        array_time_array[i] = array_elements[i]*array_elements[i]
    plt.figure(3)
    plt.plot(array_elements, array_time_array)

    plt.show()
main()