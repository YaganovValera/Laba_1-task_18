<h1 align="center">Laba_1_task_18 </h1>
<h2 align="center">Лабараторная работа №1, вариант 18 </h2>

---
> Task: Write a program that reads text from a file, displays it on the screen, removing unnecessary spaces in each even sentence.
> 
> Задание: Написать программу, которая читая текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении. 

---
#### __Stages of the program__ \ _Этапы работы программы_:

1. __With the help of punctuation marks that stand at the end of the sentence, we determine the parity of the sentence.__ \ _С помощью знаков препинания, которые стоят в конце предложения, определяем четность предложения._
```python
    parity_of_the_sentence = False  
    if line_txt[index_symbol_txt] in ['.', '?', '!']:                     
        parity_of_the_sentence = not parity_of_the_sentence
```
2. __If the sentence is even, then we start editing this sentence.__ \ _Если предложение четное, то начинаем редактировать это предложение_:
   1. __If the sentence is from the red line, then we leave spaces for the paragraph.__ \
_Если предложение с красной строки, то пробелы для абзаца оставляем_: 
   ```python
    if index_symbol_txt < 3:                                       
        if paragraph and line_txt[index_symbol_txt] == ' ':
            print(line_txt[index_symbol_txt], end='')
            continue
        else:
            paragraph = False
    ```
   2. __We remove consecutive spaces.__ \ _Удаляем подряд идущие пробелы._
    ```python
    if line_txt[index_symbol_txt] == ' ' and line_txt[index_symbol_txt+1] == ' ':
        continue
   ```
   3. __We remove spaces before punctuation marks.__ \ _Удаляем пробелы перед знаками препинания._
   ```python
    punctuation_marks = ['.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»']
    if line_txt[index_symbol_txt] == ' ' and line_txt[index_symbol_txt + 1] in punctuation_marks:
        continue
    ```
3. __If the sentence is odd, then just output the sentence.__ \ _Если предложение нечетное, то просто выводим предложение._

---
> The disadvantage of the program: if an even sentence is a title that is located in the center, then the program removes the necessary spaces.
>
> Недостаток программы: если четное предложение - это заголовок, который расположен в центре, то программа удаляет нужные пробелы.




