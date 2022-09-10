'''Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
округлённую до трёх знаков после точки.
Пример:
Для n = 6 -> 14.072'''

num = int(input('Введите число: '))

def spisokPos(n):
    tls = []
    for i in range(1, n+1):
        tls.append(round((1 + 1 / i) ** i, 3))
    return tls


def smm(ls):
    sm=0
    for i in range(len(ls)):
        sm += ls[i]
    return sm

res = spisokPos(num)
print(f'{res}  Сумма = {smm(res)}')


n = int(input('Enter number: '))

def sequence(n):
    return[round((1 + 1 / x)**x, 3) for x in range(1, n + 1)]

print(sequence(n))
print(round(sum(sequence(n)), 3))
