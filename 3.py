# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

from re import I


# n = int(input('Введите число: '))
# sum = 0
# for i in range(1, n+1):
#     a = (1 + 1/i)**i
#     sum += a
#     print(f"Сумма равна: {sum}")

n = int(input('Введите число: '))


def sequence(n):
    return [round((1+1/x)**x, 2) for x in range(1, n+1)]


print(sequence(n))
print('Сумма последовательности равна ', round(sum(sequence(n)), 2))
