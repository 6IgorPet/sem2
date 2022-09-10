'''Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на позициях a и b.
Значения N, a и b вводит пользователь с клавиатуры.'''

n = int(input('Введите число: '))
spisok = list(range(-n, n+1))
print(spisok)
a = int(input('Введите номер позиции первого числа: '))
b = int(input('Введите номер позиции первого числа: '))
print(f'Произведение {spisok[a-1]} и {spisok[b-1]} = {spisok[a-1] * spisok[b-1]} ')
import for_dz
new_a = for_dz.a-1
new_b = for_dz.b-1
print(f'Произведение {spisok[new_a]} и {spisok[new_b]} = {spisok[new_a] * spisok[new_b]} ')
