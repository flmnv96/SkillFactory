from random import randint


def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)


def binary_search(array, element, left, right):
    if array[len(array) - 1] < x:
        return len(array) - 1
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует
    middle = (right + left) // 2  # находимо середину
    if array[middle] < element <= array[middle + 1]:
        return middle  # возвращаем этот индекс
    elif element <= array[middle]:  # если элемент меньше элемента в середине
        return binary_search(array, element, left, middle - 1)  # ищем в левой половине
    else:  # иначе ищем в правой
        return binary_search(array, element, middle + 1, right)  # иначе ищем в правой


print('''Введите от 10 до 30  чисел через пробел.
Если вам лень, введите одно число и нажмите "ENTER", список сформируеться сам''')
# 28 29 54 30 11 93 72 68 36 25 66 22 97 84 37 20 95 28 29 84 91 66 32 42 16 41 20 10 99 99

# a = list(map(float, input().split()))
# num_list = []
num_input = input().split()

try:
    num_list = list(map(float, num_input))

    if len(num_list) < 9:
        x = num_list[0]
        b = randint(10, 30)
        num = []
        for i in range(b):
            num.append(randint(0, 99999) / 100)
    else:
        num = num_list
        x = int(input('Введите число: '))

    qsort(num, 0, len(num) - 1)

    binary_num = binary_search(num, x, 0, len(num) - 1)

    print('Последовательность чисел: ', num)
    print('Число введеммое пользователем: ', x)
    if type(binary_num) == int and binary_num < len(num) - 1:
        print('Номер позиции числа, которое меньше введенного пользователем числа равен: ', binary_num)
    elif binary_num == len(num) - 1:
        print('''Все числа последовательности меньше числа введенного пользователем.
        Номер последнего числа последовательности ''', len(num) - 1)
    else:
        print('Число, которое меньше введенного пользователем числа\nв последовательности не найдено.')

except ValueError:
    print("Вы ввели не чифры, а буквы.\nПопробуйте снова.")
