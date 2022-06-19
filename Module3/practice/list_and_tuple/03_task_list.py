# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -10 до 10.
# Вывести на экран сумму всех элементов.

import random
numbers = []
n = int(input("n: "))
sum_numbers = 0

for i in range(n):
    x = random.randint(-10, 10)
    numbers.append(x)
print(numbers)

for j in numbers:
    sum_numbers += j
print(sum_numbers)
