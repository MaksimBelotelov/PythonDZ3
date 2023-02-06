# Задача 18: Требуется найти в массиве A[1..N] самый 
# близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N 
# – количество элементов в массиве. В последующих строках 
# записаны N целых чисел Ai. Последняя строка содержит 
# число X

n=int(input('Введите количество элементов: '))
array=[]

for i in range(n):
    array.append(int(input(f'Введите элемент {i}: ')))

print(array)

x=int(input('Введите число X: '))
difference=abs(array[0]-x)
nearest=array[0]

for i in array:
    if abs(x-i)<difference:
        difference=abs(x-i)
        nearest=i

print(f'Ближайшее число к {x} в массиве: {nearest}.')