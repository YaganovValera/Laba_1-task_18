""" Option 18./ Вариант 18.
   A program that reads text from a file displays it on the screen, removing unnecessary spaces in each even sentence.
   Программа, которая читает текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении.
   Выполнил: Яганов Валерий ИСТбд-11
"""
import time

start = time.monotonic()                                                               # Запуск таймера

try:
    file_name = "test_2.txt"                                                             # название файла
    with open(file_name, "r", encoding="utf8") as file:
        punctuation_marks = ('.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»', '…')     # знаки препинания
        parity_of_the_sentence = False                                                  # контролирует четность предложения
        number_of_elements = 1                                                          # количество считываемых элементов
        flag_correct_space = True                                                       # флаг отвечающий за правильность пробела

        elements_1 = file.read(number_of_elements)                                      # первый элемент из файла
        elements_2 = file.read(number_of_elements)                                      # элемент идущий за element_1

        if not elements_1:  # если файл пустой
            print(f"\nФайл {file_name} в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")

        while elements_1:                                                          # Проверка на наличие элементов в файле
            if elements_1 in ('.', '?', '!', '…'):                                 # находим конец предложения
                parity_of_the_sentence = not parity_of_the_sentence                # изменяем четность предложения на нечетность, и наоборот
            if parity_of_the_sentence:                                             # обработка четного предложения
                if elements_1 == ' ' and elements_2 == ' ':                        # Пропускаем повторяющие пробелы
                    flag_correct_space = False
                if elements_1 == ' ' and elements_2 in punctuation_marks:          # Пропускаем пробелы перед знаками препинания
                    flag_correct_space = False
            if flag_correct_space:                                                 # проверка на необходимость пробела
                print(elements_1, end='')
            elements_1 = elements_2
            elements_2 = file.read(number_of_elements)
            flag_correct_space = True

except FileNotFoundError:
    print("\nФайл не обнаружен.\nДобавьте файл в директорию или переименуйте существующий файл.")

result = time.monotonic() - start                                                   # Отключение таймера
print("\n\nВремя работы программы: {:>.10f}".format(result))


