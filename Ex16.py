# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь в 
# первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X.

n=int(input('Введите количество элементов: '))
array=[]

for i in range(n):
    array.append(int(input(f'Введите элемент {i}: ')))

print(array)

x=int(input('Введите число, количество вхождений которого'
    ' необходимо посчитать: '))

cntr=0
for i in array:
    if i==x:
        cntr+=1

print(f'Число {x} встречается в массиве {cntr} раз(а).')