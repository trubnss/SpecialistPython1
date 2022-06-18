## "Кратные пяти из диапазона"

### Задание

Даны два целые числа a и b.

Выведите на экран все целые **кратные 5** от a до b включительно.

### Формат входных данных

Даны два целые числа. **Не гарантируется**, что a < b. \
Если a > b, то выводим все числа из диапазона [b, a].

### Формат выходных данных

Выведите все числа, требуемые по условию задачи.

### Решение задачи

```python
a = int(input("a: "))
b = int(input("b: "))

first_number = int(input("Ввести первое число: "))
second_number = int(input("Ввести второе число: "))

if first_number <= second_number:
    while first_number <= second_number:
        if first_number % 5 == 0 and first_number != 0:
            print(first_number)
        first_number +=1
else:
    while first_number >= second_number:
        if first_number % 5 == 0 and first_number != 0:
            print(first_number)
        first_number -=1
```
