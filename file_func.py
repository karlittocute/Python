def add_new_line(name_file,new_text):
    """
    Функия добавляет строку в конец файла.
    Принимает 2 аргумента: имя файла и содержание новой строки.
    Если такого файла нет, функция его создает.
    """
    if not type(name_file) == str :
        print("Ошибка в имени файла: Неверный тип данных")
        return None
    if not type(new_text) == str:
        print("Ошибка в вводимом тексте: Неверный тип данных")
        return None
    file = open(name_file, 'a')
    file.write("\n"+new_text)
    file.close()

def read_file(name_file):
    """
    Функция выводит на экран содержание файла.
    Принимает имя файла.
    """
    if not type(name_file) == str :
        print("Ошибка в имени файла: Неверный тип данных")
        return None
    file = open(name_file, 'r')
    text = file.read()
    print(text)
    file.close()

def read_line(name_file, number):
    """
    Функция выводин на экран заданную строчку из файла.
    Первый аргумент это имя файла.
    Второй - номер строки.
    """
    if not type(name_file) == str :
        print("Ошибка в имени файла: Неверный тип данных")
        return None
    if not type(number) == int :
        print("Ошибка в номере строки: Неверный тип данных")
        return None
    file = open(name_file, 'r')
    text = file.readlines()
    if number > len(text):
        print("Ошибка в номере строки: В файле всего ",len(text), " строк.")
        print("Вы указали ", number)
        return None
    print(text[number-1])
    file.close()

def change_line(name_file, number, new_text):
    """
    Функция меняет заданную строчку файла на новую.
    Первый аргумент это имя файла.
    Второй - номер строки.
    Третий - новая строка.
    """
    if not type(name_file) == str :
        print("Ошибка в имени файла: Неверный тип данных")
        return None
    if not type(number) == int :
        print("Ошибка в номере строки: Неверный тип данных")
        return None
    if not type(new_text) == str:
        print("Ошибка в вводимом тексте: Неверный тип данных")
        return None
    file = open(name_file, 'r+')
    text = file.readlines()
    if number > len(text):
        print("Ошибка в номере строки: В файле всего " , len(text) , " строк.")
        print("Вы указали " ,number)
        return None
    text[number-1] = new_text + "\n"
    file.seek(0)        # Переходим в начало файла
    for i in text:
        file.write(i)   # Заново перезаписываем файл
    print("Файл успешно изменен")
    file.close()

def delete_line(name_file, number):
    """
    Функция удаляет заданную строчку файла.
    Первый аргумент это имя файла.
    Второй - номер строки.
    """
    if not type(name_file) == str :
        print("Ошибка в имени файла: Неверный тип данных")
        return None
    if not type(number) == int :
        print("Ошибка в номере строки: Неверный тип данных")
        return None
    file = open(name_file, 'r+')
    text = file.readlines()
    if number > len(text):
        print("Ошибка в номере строки: В файле всего " , len(text) , " строк.")
        print("Вы указали " ,number)
        return None
    text[number-1] = ""
    file.seek(0)        # Переходим в начало файла
    for i in text:
        file.write(i)   # Заново перезаписываем файл
    print("Файл успешно изменен")
    file.close()
    
delete_line("file.txt",3)
read_file("file.txt")
