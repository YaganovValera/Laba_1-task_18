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
    if elements_1 in ('.', '?', '!', '…'):                       
        parity_of_the_sentence = not parity_of_the_sentence                
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
3. __If the sentence is odd, then just output the sentence.__ \ _Если предложение нечетное, то просто выводим предложение._

---
> The disadvantage of the program: if an even sentence is a header that is located in the center, or a red line, then the program removes the necessary spaces.
>
> Недостаток программы: если четное предложение - это заголовок, который расположен в центре, или красная строка, то программа удаляет нужные пробелы.




