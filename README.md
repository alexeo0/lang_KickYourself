Язык программирования на основе Brainfuck, где команды произносятся вслух.


Как запустить

1. Установить библиотеку:

```
pip install openai-whisper
```

2. Запустить main.py
3. Ввести имя аудиофайла который лежит в той же папке
4. Ввести инпут если нужен, или нажать Enter


Как записать программу

Команды разделяются фразой "ya kaka"


Команды

I'm an idiot - прибавляет 1 к текущей ячейке
I'm little puppy for you - вычитает 1 из текущей ячейки
I like eating poop - выводит символ текущей ячейки
I like losing in everything - читает символ из инпута в текущую ячейку
I'm would do that you say - переходит к следующей ячейке
I'm your slave - переходит к предыдущей ячейке
I'm the worst person in the world - если текущая ячейка равна 0, прыгает вперёд за парный I'm stupid makaka
I'm stupid makaka - если текущая ячейка не равна 0, прыгает назад за парный I'm the worst person in the world
ya dibil - сбрасывает все ячейки в 0


|Память

Всего 30000 ячеек. Каждая хранит число от 0 до 255. При выходе за границы числа оно оборачивается (255 + 1 = 0).


Пример

Программа выводит букву A (код 65):

Нужно произнести "I'm an idiot" 65 раз с "ya kaka" между каждой командой, потом "ya kaka I like e


Пример 2
```I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm would do that you say ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm like eating poop ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm would do that you say ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm your slave ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm like eating poop ya kaka I'm would do that you say ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm like eating poop ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm little puppy for you ya kaka I'm like eating poop ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm an idiot ya kaka I'm like eating poop```
—→ Hello world
