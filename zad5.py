'''Задание 5 Реализуйте алгоритм перемешивания списка.'''
import random


lst = list(range(5, 555, 55))
print(list)

def mix_list(ls):
    new_ls = ls.copy()
    for i in range(len(new_ls)):
        ind_rand = random.randint(0, len(new_ls) - 1)
        temp = new_ls[i]
        new_ls[i] = new_ls[ind_rand]
        new_ls[ind_rand] = temp
    return new_ls


print(mix_list(lst))