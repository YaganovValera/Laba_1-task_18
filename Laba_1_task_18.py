""" Option 18./ Вариант 18.
   A program that reads text from a file displays it on the screen, removing unnecessary spaces in each even sentence.
   Программа, которая читает текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении.
   Выполнил: Яганов Валерий ИСТбд-11
"""
with open('test.txt', encoding="utf8") as file:
    parity_of_the_sentence = False
    for sentence_txt in file:
        for symbol_txt in range(0, len(sentence_txt) - 1):
            if sentence_txt[symbol_txt] in ['.', '?', '!']:                      # Finding the end of the sentence
                parity_of_the_sentence = not parity_of_the_sentence              # Determine the parity of the sentence
            if parity_of_the_sentence:
                if sentence_txt[symbol_txt] == ' ' and sentence_txt[symbol_txt+1] == ' ':
                    continue
                if sentence_txt[symbol_txt] == ' ' \
                        and sentence_txt[symbol_txt + 1] in ['.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»']:
                    continue
            print(sentence_txt[symbol_txt], end='')
        print(sentence_txt[len(sentence_txt)-1], end='')
