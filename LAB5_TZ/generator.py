import math
import numpy as np


def read_param_from_file(file_path):
    """
    в файле указывается параметры через пробел в следущем порядке:
    a-ненулевой множитель, Xo-начальное значение, c-приращение, N-модуль равный мощности алфавита
    :param file_path:Путь до файла с параметрами
    :return: result массив параметров
    """
    result = []

    try:


        with open("param") as f:
            for line in f:
                result.append(int(line.strip()))
    finally:
        f.close()


    return result


def write_to_file(filename, result):
    f = open(filename, 'w')
    try:
        f.write(result)
    finally:
        f.close()
    return None


def egcd(a, b):
    """
    функцию egcd, рекурсивно находит НОД чисел a и b, используя
    расширенный алгоритм Евклида.
     Функция возвращает кортеж из трех значений: НОД, x, y.
    :param a:значение
    :param b: модуль
    :return: НОД, x, y
    """
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def modinv(a, m):
    """
    находит обратный элемент по модулю m для числа a.
    Если НОД не равен 1, то возникает исключение ValueError.
    :param a:
    :param m:
    :return:
    """
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        raise ValueError('Обратного элемента не существует')
    else:
        return x % m


def get_elem(a, x, c, n):
    """
    функция получения одного элемента последовательности
    :param a: множитель отличный от нуля
    :param x: начальное или предыдущее значение выборки
    :param c: приращение
    :param n: модуль равный мощности алфавита
    :return: переменная типа int , которая является элементов последовательности
    """
    if x >= 1:
        return (a * modinv(x, n) + c) % n
    else:
        if x == 0:
            return c


def get_sequence(a, x, c, n,N):
    """

    :param a: множитель отличный от нуля
    :param x: начальное или предыдущее значение выборки
    :param c: приращение
    :param n: модуль равный мощности алфавита
    :param N: Количество элементов выборки
    :return:
    """
    result = []
    result.append(get_elem(a, x, c, n))
    while len(result) != N:
        result.append(get_elem(a, result[len(result) - 1], c, n))

    return result


def get_period(seq):
    start_symb = seq[0]
    start_pos = 0
    end_pos = seq[1:].index(start_symb)
    return end_pos - start_pos



def get_estimation(result, n):
    """
    функция осуществляющая оценку по критерию хи квадрат пирсона
    :param result: начальная
    :param n:модуль элемента
    :return:
    """
    s_kr_table = [3.841, 5.991, 7.815, 9.488, 11.070, 12.592, 14.067, 15.507, 16.919, 18.307, 19.675, 21.026, 22.362,
                  23.685, 24.996, 26.296]  # массив критических значений при альфа равное 0,05
    if n < 10:
        k = n
    else:
        k = int(round(5 * math.log10(n)))  # количество интервалов
    h = int(round(n / k))  # шаг
    arr = [[0, 0, 0] for _ in range(k)]
    arr[0][0] = 0
    arr[0][1] = h
    prev = h
    # определение интеравалов
    for i in range(1, len(arr)):
        arr[i][0] = prev
        arr[i][1] = prev + h
        prev = arr[i][1]
        # подсчитываем количество чисел попавших в интервал
    for number in result:
        for i in range(0, len(arr)):
            if arr[i][0] <= number and number < arr[i][1]:
                arr[i][2] += 1
                # print(arr[i][0] , arr[i][1])
                break
            else:
                if i == len(arr)-1 and  arr[i][0] <= number and number <= arr[i][1]:
                    arr[i][2] += 1
                    break
    # print(arr)
    # вычисляем статистику критерия
    p = 1 / k  # вероятность попадания в интервал так-как распределение равномерное принимаем за 1/k
    sum = 0
    n = len(result)
    for i in range(0, k):
        sum += pow(((arr[i][2] / n) - p), 2) / p
    s = n * sum
    # print('s=', s)
    if s > s_kr_table[k - 1]:
        return (False,s)
    else:
        return (True,s)
def start_generate(file_path):
    param = read_param_from_file('param')
    result = get_sequence(param[0], param[1], param[2], param[3],param[4])
    period = get_period(result)
    s,check=get_estimation(result,param[3])
    message=f"Количество элементов в последовательности: {param[4]}\n"+f"Параметры генератора:\na = {param[0]} ; x = {param[1]} ; c = {param[2]}  ; n = {param[3]} \n"+f"Последовательность:\n{result}\n"+f"Период последовательности:\n{period}\n"+f"Результат проверки по критерию хи квадрат Пирсона:\n{s}\n"+f"Статистика критерия равна:\n{check}\n"
    write_to_file('result',message)
    return (result,message)

