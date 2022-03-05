<h1 align="center">Laba_1_task_18 </h1>
<h2 align="center">Лабараторная работа №1, вариант 18 </h2>

---
> Task: Write a program that reads text from a file, displays it on the screen, removing unnecessary spaces in each even sentence.
> 
> Задание: Написать программу, которая читая текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении. 

---
#### Этапы работы программы:

1. С помощью знаков препинания, которые стоят в конце предложения, определяем четность предложения.
```python
    parity_of_the_sentence = False  
    if line_txt[index_symbol_txt] in ['.', '?', '!']:                     
        parity_of_the_sentence = not parity_of_the_sentence
```
2. Если предложение четное, то начинаем редактировать это предложение:
   1. Если предложение с красной строки, то пробелы для абзаца оставляем: 
   ```python
    if index_symbol_txt < 3:                                       
        if paragraph and line_txt[index_symbol_txt] == ' ':
            print(line_txt[index_symbol_txt], end='')
            continue
        else:
            paragraph = False
    ```
   2. Удаляем подряд идущие пробелы. 
    ```python
    if line_txt[index_symbol_txt] == ' ' and line_txt[index_symbol_txt+1] == ' ':
        continue
   ```
   3. Удаляем пробелы перед знаками препинания.
   ```python
    punctuation_marks = ['.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»']
    if line_txt[index_symbol_txt] == ' ' and line_txt[index_symbol_txt + 1] in punctuation_marks:
        continue
    ```
3. Если предложение нечетное, то просто выводим предложение.

---
##### Недостаток программы: Если четное предложение является заголовком, который расположен по центру, то программа выводит его с красной строки.



