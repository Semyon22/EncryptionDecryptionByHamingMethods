alphabet='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def read_from_file(file_path):
    """
    функция считывания сообщения с файла
    :param file_path:
    :return:
    """
    f=open(file_path,'r',encoding='utf-8')
    try:
        word=f.readline().strip()
    finally:
        f.close()
    return word
def get_shift_from_file(file_path):
    """
    функция считывания сдвига из файла
    :param file_path:
    :return:
    """
    f = open(file_path, 'r')
    try:
        word = int(f.readline().strip())
    finally:
        f.close()
    return word

def get_coded_message(file_path_word,file_path_shift):

    word=read_from_file(file_path_word)
    shift=get_shift_from_file(file_path_shift)
    new_s=''
    shift = shift % 33
    for i in range(0,len(word)):

        new_s+=chr(ord(word[i])+shift)
    f = open("caesar_result", 'w',encoding='utf-8')
    try:
        f.write(new_s)
    finally:
        f.close()
    return new_s
def get_encoded_message(file_path_word,file_path_shift):
    word = read_from_file(file_path_word)
    shift = get_shift_from_file(file_path_shift)
    shift=shift % 33
    encoded_message=''
    for i in range(0,len(word)):
        encoded_message+=chr(ord(word[i])-shift)
    f = open("caesar_encoding", 'w', encoding='utf-8')
    try:
        f.write(encoded_message)
    finally:
        f.close()
    return encoded_message

print(get_coded_message("caesar_word",'shift'))
print(get_encoded_message("caesar_result","shift"))
# for i in range(0,len(alphabet)):
#     print(f"{alphabet[i]} = {ord(alphabet[i])}")