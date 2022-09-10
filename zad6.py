'''Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
а программа - определять количество вхождений одной строки в другой.
Пример
-Для "abababb" и "aba" -> 2'''

stroka = "abababb"
search = "aba"
count = 0
i = 0
while i < len(stroka):
    if stroka[i:i + len(search)] == search:
        count += 1
        i += 1
    else:
        i += 1
print(count)