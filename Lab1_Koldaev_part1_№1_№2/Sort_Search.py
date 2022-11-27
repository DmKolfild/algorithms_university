import random
import time
import matplotlib.pyplot as plt
import math

def getRandomArray(n):
    array=[]
    for i in range(n):
        array.append(random.randint(0,1000))
    return array


def merge_sort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    # рекуретный вызов функции для дальнейшего разбиения массива
    L = merge_sort(A[:len(A) // 2])
    R = merge_sort(A[len(A) // 2:])
    n = m = k = 0
    C = [0] * (len(L) + len(R))  # хранение отсортированных частей исходного массива
    while n < len(L) and m < len(R):
        if L[n] <= R[m]:
            C[k] = L[n]
            n += 1
        else:
            C[k] = R[m]
            m += 1
        k += 1
    while n < len(L):
        C[k] = L[n]
        n += 1
        k += 1
    while m < len(R):
        C[k] = R[m]
        m += 1
        k += 1
    for i in range(len(A)):
        A[i] = C[i]
    return A

def InterpolationSearch(lys, val):
    low = 0
    high = (len(lys) - 1)
    while low <= high and val >= lys[low] and val <= lys[high]:
        index = low + int(((float(high - low) / ( lys[high] - lys[low])) * ( val - lys[low])))
        if lys[index] == val:
            return index
        if lys[index] < val:
            low = index + 1;
        else:
            high = index - 1;
    return -1

def main():
    array_elements = [800, 3000, 7000, 15000, 20000, 25000, 30000, 40000, 45000]  # число элементов для алгоритмов
    array_time = []  # массив времени выполнения сортировки для различного числа элементов
    array_time_search = []  # массив времени выполнения поиска для различного числа элементов
    quantity_sort = 10  # число выполнения алгоритма для получения адекватного времени
    search_values = 343  # искомый элемент массива

    for i in range(len(array_elements)):
        sum_time = 0  # сумарное время сортировки для нескольких запусков
        sum_time_search = 0  # сумарное время поиска для нескольких запусков
        array = getRandomArray(array_elements[i])  # генерация случайного массива
        for j in range(quantity_sort):
            #task1
            start_time = time.time()
            array = merge_sort(array)  # сортировка массива
            end_time = time.time()
            sum_time += (end_time - start_time)
            #task2
            start_time = time.time()
            # выполнения поиска несколько раз для получения адекватного значения времени
            for q in range(10000):
                InterpolationSearch(array, search_values)  # поиск искомого элемента
            end_time = time.time()
            sum_time_search += (end_time - start_time)
        array_time.append(sum_time)
        array_time_search.append(sum_time_search)

    print("-— %s elements —-" % array_elements)
    print("-— %s time —-" % array_time)

    print("-— %s elements —-" % array_elements)
    print("-— %s time —-" % array_time_search)

    # график сложности, полученный на практике для сортировки
    plt.figure(0)
    plt.plot(array_elements, array_time)
    plt.title('sort_prac')

    # график сложности теоретический для сортировки
    for i in range(len(array_elements)):
        array_time[i] = array_elements[i]*math.log2(array_elements[i])

    plt.figure(1)
    plt.plot(array_elements, array_time)
    plt.title('sort_analitic')

    # график сложности, полученный на практике для поиска
    plt.figure(2)
    plt.plot(array_elements, array_time_search)
    plt.title('poisk_prac')
    for i in range(len(array_elements)):
        array_time_search[i] = math.log2(math.log2(array_elements[i]))

    # график сложности теоретический для поиска
    plt.figure(3)
    plt.plot(array_elements, array_time_search)
    plt.title('poisk_analitic')


    plt.show()
main()