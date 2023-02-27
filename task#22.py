# | Задача 22: Даны два неупорядоченных набора целых
# чисел (может быть, с повторениями). Выдать без повторений
# в порядке возрастания все те числа, которые встречаются в
# обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого
# множества. m - кол-во элементов второго множества. Затем
# пользователь вводит сами элементы множеств. | 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12 |
# | --- | --- |
def inputSet(x: int, collection: str):
    output = set()
    for i in range(x):
        item = int(input(f'Input element [{i}] for list {collection}  : '))
        output.add(item)
    return output


n = int(input('Input lenght of list A: '))
A = inputSet(x=n, collection='A')

print('-' * 20)

m = int(input('Input lenght of list B: '))
B = inputSet(m, 'B')

print(f'\nA = {A}\nB = {B}\n' + '-' * 20)

result = list(A.intersection(B))
result.sort()

print(f'In both lists equal elements are : {result}')
