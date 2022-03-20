<h1 align="center">Laba_1_task_18 </h1>
<h2 align="center">Лабараторная работа №1, вариант 18 </h2>

---
> __Task__: Write a program that reads text from a file, displays it on the screen, removing unnecessary spaces in each even sentence.
> 
> __Задание__: Написать программу, которая читая текст  из файла, выводит его на экран, убирая лишние пробелы в каждом четном предложении. 

---
#### __Stages of the program__ \ _Этапы работы программы_:

1. __With the help of punctuation marks that stand at the end of the sentence, we determine the parity of the sentence.__ \ _С помощью знаков препинания, которые стоят в конце предложения, определяем четность предложения._
```python
    parity_of_the_sentence = False  
    if elements_1 in ('.', '?', '!', '…') and not flag_float_number:                       
        parity_of_the_sentence = not parity_of_the_sentence                
``` 
1.1 Однако, если после знака препинания идет абзац и предложение четное, то проверяем его на абзац: 
```python
    if elements_2 == '\n' and parity_of_the_sentence:                         
        paragraph = True
```
2. __If the sentence is even, then we start editing this sentence.__ \ _Если предложение четное, то начинаем редактировать это предложение_:
   1. __Skip consecutive spaces__ \ _Пропускаем подряд идущие пробелы._
       ```python
        if elements_1 == ' ' and elements_2 == ' ':                 
            flag_correct_space = False
      ```
   2. __Skip spaces before punctuation marks.__ \ _Пропускаем пробелы перед знаками препинания._
      ```python
       punctuation_marks = ('.', '!', ',', '?', ':', ';', ')', '(', '\'', '\"', '»', '…')
       if elements_1 == ' ' and elements_2 in punctuation_marks:          
           flag_correct_space = False
       ```
   3. __Also, if there is not an integer in an even sentence, and it is written through a dot, then this dot will not be considered the end of the sentence.__ \ _Также если в четном предложение есть не целое число, и оно записано через точку, то эта точка не будет считаться концом предложения._
     ```python
    if elements_1 in digits and elements_2 == '.':                                 # проверка на число с плавающей точкой
        float_number = True
    if elements_1 == '.' and elements_2 in digits and float_number:                # если это число с плавающей точкой то точку не считаем концом предложения
        flag_float_number = True
     ```
3. __If the sentence is odd, then just output the sentence.__ \ _Если предложение нечетное, то просто выводим предложение._

---
> The disadvantage of the program: if an even sentence is a header that is located in the center, or a red line, then the program removes the necessary spaces.
> Also if the dot is used in initials, for example "Ivanov.I" , then the program will consider this point to be the end of the sentence.
>
> Недостаток программы: если четное предложение - это заголовок, который расположен в центре, то программа удаляет нужные пробелы.
> Также если точка используется в инициалах, например "Иванов.И" , то программа будет считать эту точку концом предложения.  




