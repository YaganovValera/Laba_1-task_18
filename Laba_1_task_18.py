""" Option 18./ Вариант 18.
   A program that reads text from a file displays it on the screen, removing unnecessary spaces in each even sentence.
   Программа, которая читает текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении.
   Выполнил: Яганов Валерий ИСТбд-11
"""
import time
import os.path

start_0 = time.time()                                                                        # Запуск таймера

try:
    file_name = "test_7.txt"                                                               # название файла
    with open(file_name, "r", encoding="utf8") as file:

        digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        punctuation_marks = ('.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»', '…') # знаки препинания
        parity_of_the_sentence = False                                                     # контролирует четность предложения
        number_of_elements = 1                                                             # количество считываемых элементов
        flag_correct_element = True                                                        # флаг отвечающий за корректность элементов (следит за лишними пробелами)

        paragraph = False                                                                  # флаг отвечающий за абзац в четном предложение
        max_space_in_paragraph = 3                                                         # максимальное кол-во пробелов в абзаце
        space_counter_in_a_paragraph = 0                                                   # счетчик пробелов в абзаце

        float_number = True                                                                # Отвечает за числа с плавающей точкой
        flag_float_number = False                                                          # Отвечает за то, чтобы программа не считала точку в числах концом предложения

        elements_1 = file.read(number_of_elements)                                         # первый элемент из файла
        elements_2 = file.read(number_of_elements)                                         # элемент идущий за element_1

        if not elements_1:                                                                 # если файл пустой
            print(f"\nФайл {file_name} в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        start_1 = time.time()
        while elements_1:                                                                  # Проверка на наличие элементов в файле
            if elements_1 == '.' and elements_2 in digits and float_number:                # если это число с плавающей точкой то точку не считаем концом предложения
                flag_float_number = True

            if elements_1 in ('.', '?', '!', '…') and not flag_float_number:               # находим конец предложения
                parity_of_the_sentence = not parity_of_the_sentence                        # изменяем четность предложения на нечетность, и наоборот
                if elements_2 == '\n' and parity_of_the_sentence:                          # Если следующие предложение четное и переходит на новою строку, то рассматриваем на наличие абзаца в нем
                    paragraph = True
            if parity_of_the_sentence and not (elements_1 in ('.', '?', '!', '…', '\n')):  # обработка четного предложения, без учета знаков препинания (для того чтобы не сбить проверку на абзац)
                if not (paragraph and elements_1 == ' ' and space_counter_in_a_paragraph < max_space_in_paragraph):     # Если начало предложения не является абзацем, то обрабатываем его
                    if elements_1 == ' ' and elements_2 == ' ':                            # Пропускаем повторяющие пробелы
                        flag_correct_element = False
                    if elements_1 == ' ' and (elements_2 in punctuation_marks):            # Пропускаем пробелы перед знаками препинания
                        flag_correct_element = False
                    paragraph = False                                                      # Сбрасываем проверку на абзац
                    space_counter_in_a_paragraph = 0                                       # Сбрасываем проверку на абзац
                else:
                    space_counter_in_a_paragraph += 1                                      # Счет пробелов в абзаце
            if flag_correct_element:                                                       # проверка на необходимость пробела и других элементов
                print(elements_1, end='')

            flag_float_number = False
            float_number = False

            if elements_1 in digits and elements_2 == '.':                                 # проверка на число с плавающей точкой
                float_number = True

            elements_1 = elements_2
            elements_2 = file.read(number_of_elements)
            flag_correct_element = True
            flag_float_number = False
        result_1 = time.time() - start_1

    print("\n\n Размер файла с текстом: {:>.4f} MB".format(os.path.getsize(file_name)/1024/1024))

except FileNotFoundError:
    print("\nФайл не обнаружен.\nДобавьте файл в директорию или переименуйте существующий файл.")


result_0 = time.time() - start_0                                                            # Отключение таймера
print(" Время работы всей программы: {:>.10f} sec.".format(result_0))
print(" Время работы кода, который отвечает за обработку и вывод предложений из файла: {:>.10f} sec.".format(result_1))