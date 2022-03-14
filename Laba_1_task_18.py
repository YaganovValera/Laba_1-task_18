""" Option 18./ Вариант 18.
   A program that reads text from a file displays it on the screen, removing unnecessary spaces in each even sentence.
   Программа, которая читает текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении.
   Выполнил: Яганов Валерий ИСТбд-11
"""
try:
    file_name = "test.txt"
    with open(file_name, "r", encoding="utf8") as file:
        punctuation_marks = ('.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»')  # знаки препинания
        parity_of_the_sentence = False                                                 # controls parity \ контролирует четность
        for line_txt in file:
            for index_symbol_txt in range(0, len(line_txt)):
                if line_txt[index_symbol_txt] in ('.', '?', '!'):                      # Finding the end of the sentence\ находим конец предложения
                    parity_of_the_sentence = not parity_of_the_sentence                # Determine the parity of the sentence \ определяем четность
                if parity_of_the_sentence:                                             # processing an even sentence \ обработка четного предложения
                    if line_txt[index_symbol_txt] == ' ' and line_txt[index_symbol_txt+1] == ' ':
                        continue
                    if line_txt[index_symbol_txt] == ' ' \
                            and line_txt[index_symbol_txt + 1] in punctuation_marks:
                        continue
                print(line_txt[index_symbol_txt], end='')
            #print()                                           # end of paragraph (switching to a new line)\ завершает абзац (переход на новую строку)
except FileNotFoundError:
    print("\nФайл не обнаружен.\nДобавьте файл в директорию или переименуйте существующий файл.")