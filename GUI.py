from tkinter import *
from tkinter import ttk

import caesar_cipher
import haming_module
from main import *
from haming_module import get_coded_message , get_encoded_message
from caesar_cipher import get_coded_message ,get_encoded_message
from tkinter.messagebox import showerror, showwarning, showinfo
from LAB5_TZ import generator


def code_word():
    """
    Кодировка методом гильберта мура с добавлением бита четности
    :return:
    """
    print(entry1.get())
    print(entry.get())
    #entry путь до файла с ансамблем
    #entry1 путь до файла с кодируемым словом
    try:
        dict_word_code = Use_Gilbert_Moore(entry1.get())

        result = "кодовые слова для всех символов алфавита:" + "\n" + str(dict_word_code) \
                 + "\n" + "средняя длина кодового слова:\n" + str(get_avrg_codeword_len(entry1.get())) + "\n" \
                 + "Избыточность:\n" + str(get_redundancy(entry1.get())) + "\n" + "Неравенство крафта выполнено?\n" \
                 + str(check_crafting_inequality(
            entry1.get())) + "\n" + "Зашифрованная последовательность содержится в файле result.txt"
        word_coding(read_word_from_file(entry.get()), dict_word_code)
        showinfo(title="Параметры полученные при кодировке", message=result)

    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 3) Либо НЕКОРРЕКТНЫЙ файл"
                  )
    finally:
        pass
def encod_word():
    """
    Декодировка метода Гильберта Мура с использованием проверки на ошибку
    :return:
    """
    try:
        result = word_encoding(entry2.get(), entry3.get())
        message1 = "Ваша раскодированная последовательность: " + result[0] + "\nЗаписана в файл encod_word"
        message2 = "Ошибки возникшие в результате передачи данных: \n" + result[1] + "\nЗаписаны в файл errors"
        showinfo(title="раскодированная последовательность", message=message1)
        showinfo(title="Ошибки возникшие в результате передачи данных", message=message2)
    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 3) Либо НЕКОРРЕКТНЫЙ файл\n 4) Либо ввели НЕККОРЕКТНЫЕ данные"
                  )
    finally:
        pass
def haming_code_word():
    """
    Кодировка методом Хэминга
    :return:
    """
    try:
        coded_message = haming_module.get_coded_message(entry.get())

        result = f"Ваша закодированная последовательность{coded_message}\n" \
                 f"Закодированная последовательность записана в файл haming_coded_word \n" \

        showinfo(title="Результат Шифрования Haming", message=result)

    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 3) Либо НЕКОРРЕКТНЫЙ файл \n 4) Либо ввели НЕККОРЕКТНЫЕ данные"
                  )
    finally:
        pass

    #entry путь до файла с кодируемым словом
def haming_encode_word():
    """
    Декодировка методом Хэминга
    :return:
    """
    try:
        encoded_message = haming_module.get_encoded_message(entry3.get())

        result = f"Ваша раскодированная последовательность{encoded_message}\n" \
                 f"Раскодированная последовательность записана в файл haming_encoded_message \n"\
                f"Cообщения об обнаруженых и исправленных ошибках записаны в файл haming_error_message \n"
        showinfo(title="Результат декодировки Haming", message=result)
    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 2) Либо НЕКОРРЕКТНЫЙ файл"
                  )
    finally:
        pass
def caesar_code_word():
    #entry1 cдвиг
    #entry слово
    try:
        coded_message = caesar_cipher.get_coded_message(entry.get(),entry1.get())

        result = f"Ваша закодированная последовательность \n {coded_message}\n" \
                 f"Закодированная последовательность записана в файл caesar_result \n"

        showinfo(title="Результат Шифрования Caesar", message=result)

    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 3) Либо НЕКОРРЕКТНЫЙ файл \n 4) Либо ввели НЕККОРЕКТНЫЕ данные"
                  )
    finally:
        pass
    return NONE
def caesar_encode_word():
    #entry2 файл сдвига
    #entry3 файл с словом
    try:
        encoded_message = caesar_cipher.get_encoded_message(entry3.get(),entry2.get())

        result = f"Ваша раскодированная последовательность:\n {encoded_message}\n" \
                 f"Раскодированная последовательность записана в файл caesar_encoding \n" \

        showinfo(title="Результат декодировки Caesar", message=result)
    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 2) Либо НЕКОРРЕКТНЫЙ файл"
                  )
    finally:
        pass
def generator_Eichenaue():
    print(entry.get())
    try:
        result , message=generator.start_generate(entry.get())
        message+="\nИнформация продублирована в файле result\n"
        showinfo(title="Результат Генерации", message=message)
    except:
        showerror(title="Сообщение об ошибке",
                  message="Вы записали: \n 1) Либо НЕСУЩЕСТВУЮЩИЙ ФАЙЛ \n 2) Либо НИЧЕГО не ввели \n 2) Либо НЕКОРРЕКТНЫЙ файл"
                  )
    finally:
        pass
def check_radiobatton_code():
    """
       Функция отвечающая за то какой метод кодировки/генераций использовать
       :return:
       """
    if r_var.get() == 0:

        if (entry1.get()!="" and entry.get()!=''):
                code_word()
    else:

            if (entry.get()!='' and r_var.get()==1):
                haming_code_word()
            else:
                if (r_var.get() == 2 and entry1.get()!='' and entry.get()!=''):
                    caesar_code_word()
                else:
                    if (r_var.get() == 3 and entry.get()!=''):
                        generator_Eichenaue()

def check_radiobatton_encode():
    """
    Функция отвечающая за то какой метод декодировки использовать
    :return:
    """
    if r_var.get() == 0:
        if (entry2.get() != "" and entry3.get() != ''):
            encod_word()
    else:
        if (entry3.get()!='' and r_var.get()==1):
            haming_encode_word()
        else:
            if (r_var.get()==2 and entry2!='' and entry3!=''):
                caesar_encode_word()
def check_widget_acitivity():
    """
    функция отвечающая за активность форм ввода данных
    :return:
    """
    if r_var.get() == 0:
        entry2.state(['!disabled'])
        entry1.state(['!disabled'])
        entry3.state(['!disabled'])
        btn1.state(['!disabled'])
        lbl1.config(text='введите имя файла с исходным ансамблем:')
        lbl2.config(text='введите имя файла с исходным ансамблем:')
        lbl0.config(text='Зашифровка Последовательности')
        lbl9.config(text='Введите имя файла с кодируемым словом')
        lbl11.config(text='Расшифровка Последовательности')
        lbl.config(text="введите имя файла с закодированным словом:")
        btn.config(text='Зашифровать')
    else:
        if r_var.get()==1:
            entry1.state(['disabled'])
            entry2.state(['disabled'])
            entry3.state(['!disabled'])
            btn1.state(['!disabled'])
            lbl.config(text="введите имя файла с закодированным словом:")
            lbl1.config(text='')
            lbl2.config(text='')
            lbl0.config(text='Зашифровка Последовательности')
            lbl9.config(text='Введите имя файла с кодируемым словом')
            lbl11.config(text='Расшифровка Последовательности')
            btn.config(text='Зашифровать')
        else:
            if r_var.get()==2:
                entry2.state(['!disabled'])
                entry1.state(['!disabled'])
                entry3.state(['!disabled'])
                btn1.state(['!disabled'])
                lbl1.config(text='Введите имя файла в котором содержится сдвиг')
                lbl2.config(text='Введите имя файла в котором содержится сдвиг')
                lbl0.config(text='Зашифровка Последовательности')
                lbl9.config(text='Введите имя файла с кодируемым словом')
                lbl11.config(text='Расшифровка Последовательности')
                lbl.config(text="введите имя файла с закодированным словом:")
                btn.config(text='Зашифровать')
            else:
                if r_var.get()==3:
                    lbl.config(text="")
                    lbl2.config(text='')
                    lbl0.config(text='Генератор псевдослучайной последовательности')
                    lbl1.config(text='')
                    lbl11.config(text='')
                    lbl9.config(text='Введите имя файла в котором содержатся параметры генератора')
                    btn.config(text='Сгенерировать последовательность')
                    entry1.state(['disabled'])
                    entry2.state(['disabled'])

                    entry3.state(['disabled'])
                    btn1.state(['disabled'])

root = Tk()
#радиобаттоны
r_var = IntVar()
r_var.set(0)
r1=Radiobutton(text='метод Гильберта-мура',variable=r_var,value=0,command=check_widget_acitivity)
r2=Radiobutton(text='метод Хэминга',variable=r_var,value=1,command=check_widget_acitivity)
r3=Radiobutton(text='Шифр Цезаря',variable=r_var,value=2,command=check_widget_acitivity)
r4=Radiobutton(text='Генератор Эйхенауэра',variable=r_var,value=3,command=check_widget_acitivity)
r1.grid(column=0,row=0,sticky='s')
r2.grid(column=0,row=0,sticky='e')
r3.grid(column=0,row=0,sticky='w')
r4.grid(column=0,row=1,sticky='w')
#лейблы заголовков
lbl0 = Label(root, text="Зашифровка последовательности", font=("Arial Bold", 15))
lbl0.grid(column=0, row=2)
lbl1 = Label(root, text="введите имя файла с исходным ансамблем:", font=("Arial", 10))
lbl1.grid(column=0, row=3)
# задание размера окна
root.geometry('470x510')
# добавление формы ввода до исходного ансамбля

root.title("Шифрование/Дешифрование методом Гильберта-Мура c использованием помехоустоичевого кодирования")

entry1 = ttk.Entry()
entry1.grid(column=0, row=4,)

lbl9 = Label(root, text="введите имя файла с кодируемым словом:", font=("Arial", 10))
lbl9.grid(column=0, row=5)

entry = ttk.Entry()
entry.grid(column=0, row=6)
btn = ttk.Button(text="Зашифровать", command=check_radiobatton_code)
btn.grid(column=0, row=7)

# элементы интерфейса для дешифровки

lbl11 = Label(root, text="Расшифровка последовательности", font=("Arial Bold", 15))
lbl11.grid(column=0, row=8)

lbl2 = Label(root, text="введите имя файла с исходным ансамблем:", font=("Arial", 10))
lbl2.grid(column=0, row=9)

entry2 = ttk.Entry()
entry2.grid(column=0, row=10)

lbl = Label(root, text="введите имя файла с закодированным словом:", font=("Arial", 10))
lbl.grid(column=0, row=11)

entry3 = ttk.Entry()
entry3.grid(column=0, row=12)
btn1 = ttk.Button(text="Расшифровать", command=check_radiobatton_encode)

btn1.grid(column=0, row=13)

# окно инструкций
lbl3 = Label(root,
            text="ВНИМАНИЕ! Чтобы программа отработала корректно,\n необходимо ввести ансамбль в следующем формате:\n"
                 "P(X1) P(X2) P(X3)... P(Xn)\n"
                 "X1    X2      X3  ...  Xn"
            , font=("Arial", 12)
            )
lbl3.grid(column=0, row=14)
lbl4 = Label(root,
            text="ВНИМАНИЕ! Чтобы программа отработала корректно,\n необходимо ввести слово в 1 строку\n"
                 "пример: word"

            , font=("Arial", 11)
            )
lbl4.grid(column=0, row=15)

root.mainloop()
