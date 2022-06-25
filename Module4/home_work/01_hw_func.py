# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    def lucky_ticket(ticket_number):
    sum_left = 0
    sum_right = 0
    for i in range(6):
        if i < 3:
            sum_right += ticket_number // 10 ** i % 10
        else:
            sum_left += ticket_number // 10 ** i % 10
    if sum_left == sum_right:
        return "счастливый"
    return "не счастливый"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print(lucky_ticket(18578451))
print(lucky_ticket(000000))


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
