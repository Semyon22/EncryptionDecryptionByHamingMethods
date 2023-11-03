G = [[0, 1, 1],#порождающая матрица
     [1, 0, 1],
     [1, 1, 0],
     [1, 1, 1]
     ]

Ht = [#матрица проверки
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1],
]


# print(arr)
def get_code_word(s):
    """
    ф-ция возвращающая кодовое слово с добавлением трёх проверочных бит в конец
    :param s:кодовое слово состоящие из 4-x бит
    :return new_s: кодовое слово состоящие из 4-x бит + 3-x проверочных бит
    """

    new_s = s
    # массив для хранения кодового слова
    arr = [0] * 4
    # перевод строки в массив
    for i in range(0, 4):
        arr[i] = int(s[i])
    for k in range(0, 3):
        # инициализация буфферного массива
        buf_arr = [0] * 4
        # умножение вектор строки(кодового слова) на вектор столбец порождающей матрицы
        for i in range(0, 4):
            buf_arr[i] = arr[i] * G[i][k]
        # реализация симметрической разности для вектор строки из 4 элементов
        while len(buf_arr) != 1:
            if buf_arr[0] == buf_arr[1]:
                buf_arr.pop(0)
                buf_arr.pop(0)
                buf_arr.insert(0, 0)
            else:
                buf_arr.pop(0)
                buf_arr.pop(0)
                buf_arr.insert(0, 1)
        # запись в массив результата проверочных битов
        new_s += str(buf_arr[0])

    return new_s


def checking_for_transmission_integrity(s):
    """
    Функция проверки переданного сообщения на целостность + исправление ошибок + перевод закодированного слова в десятичную запись
    :param s: принимает одно кодовое слово
    :return: возвращает декодированное число от -15 до 15
    """
    multiply_mas = [0] * 7
    result = [0] * 3  # массив синдрома
    for k in range(0, 3):
        for i in range(0, 7):
            multiply_mas[i] = int(s[i]) * Ht[i][k]
        result[k] = sum(multiply_mas) % 2
    print(result)


    def fix_error(exept_position):
        """
        функция исправляет одиночную ошибку в кодовом слове
        :param exept_position: номер позиций где произошла ошибка
        :return: new_s слово с исправленной ошибкой
        """
        buf_mas = [0] * 7
        for i in range(0, len(s)):
            buf_mas[i] = s[i]
        if buf_mas[exept_position - 1] == '0':
            buf_mas[exept_position - 1] = '1'
        else:
            buf_mas[exept_position - 1] = '0'
        new_s = ''.join(buf_mas)
        error_message = f"исправлена ошибка в позиций номер {exept_position} \n cлово с ошибкой {s} \n исходное слово {new_s}"

        test = open('haming_error_message', 'a')
        test.write(error_message+'\n')
        test.close()
        return new_s

    def find_error(result):
        """
        функция находит номер позиций в которой совершена ошибка при помощи вектора синдрома
        :param result:
        :return:
        """
        counter = 1
        for elem in Ht:
            if elem == result:
                print(f"ошибка в позиций номер {counter}")
                new_s = fix_error(counter)
                return new_s
            counter += 1

    if (sum(result) != 0):
        try:
            new_s = find_error(result)
            number = int(new_s[:4],2)
            return number
        except:
            pass
    else:
        number = int(s[:4], 2)
        return number


def read_from_file(file_path):
    """
    функция считывает числа  из файла и переводит их в двоичную запись с добавлением незначащих нулей до длины 4
    :param filename:Путь до файла где лежит слово которое нужно закодировать
    :return: arr массив с переданными двоичными числами
    """
    flag = 1
    f = open(file_path, 'r')
    try:
        word = f.readline().strip()
    finally:
        f.close()

    arr = word.split(" ")
    for i in range(0, len(arr)):
        arr[i] = int(arr[i])
    for i in range(0, len(arr)):
        if (arr[i] <= 15 and arr[i]>=-15):
            arr[i] = bin(arr[i])
        else:
            flag = 0
            print("В входных данных было замечено число больше 15 или меньше -15.Повторите ввод")
            break
    if (flag):
        for i in range(0, len(arr)):
            if arr[i][0] == '-':
                arr[i] = '-' + arr[i][3:]
                if (len(arr[i]) != 5):
                    new_s = '-'
                    count = 5 - len(arr[i])
                    while (count != 0):
                        new_s += '0'
                        count -= 1
                    new_s = new_s + arr[i][1:]
                    arr[i] = new_s


            else:
                arr[i] = arr[i][2:]
                if (len(arr[i]) != 4):
                    new_s = ''
                    count = 4 - len(arr[i])
                    while (count != 0):
                        new_s += '0'
                        count -= 1
                    new_s = new_s + arr[i]
                    arr[i] = new_s

        return arr
    else:
        return None

def writing_to_file(filename,data):
   """
   функция записи в файл
   :param filename:названия файла в который будет происходить запись, если его нет он создастся
   :param data: массив с закодированными словами
   :return:
   """
   result = ''
   if isinstance(data[0], str):

       for i in range(0,len(data)):
           result+=data[i]
   else:
       for i in range(0,len(data)):
           result+=str(data[i])+' '
   f = open(filename,'w')
   try:
      f.write(result)
   finally:
      f.close()
   return None

def get_coded_message(file_path):
    """
    функция кодирует последовательность слов добавляя к ним три проверочных бита
    :param file_path:путь до файла с последовательностью подлежащей кодированию
    :return: arr массив кодовых слов
    """
    arr = read_from_file(file_path)
    for i in range(0, len(arr)):
        if arr[i][0] != '-':
            code_word = get_code_word(arr[i])
            arr[i] = code_word+" "
        else:
            new_s = arr[i][1:]
            code_word = get_code_word(new_s)
            arr[i] = "-" + code_word+' '
    writing_to_file('haming_coded_word', arr)
    return arr

def get_encoded_message(file_path):
    """
    функция декодеровки сообщения методом хэминга
    :param file_path: путь до файла с закодированной последовтельность
    :return:
    """
    f = open(file_path, 'r')
    try:
        word = f.readline().strip()
    finally:
        f.close()
    arr=word.split()
    for i in range(0, len(arr)):
        if arr[i][0] != '-':
            arr[i] = checking_for_transmission_integrity(arr[i])
        else:
            new_s = arr[i][1:]
            arr[i] = checking_for_transmission_integrity(new_s)
            arr[i] = arr[i] * -1
    writing_to_file("haming_encod_message",arr)
    return arr

