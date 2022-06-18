# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

import random
numbers = []
n = int(input("n: "))
y = 0

for i in range(n):
    x = random.randint(-100, 100)
    numbers.append(x)
print(numbers)

for j in numbers:
    if j > 0 and j % 2 == 0:
        y += j
print(y)
