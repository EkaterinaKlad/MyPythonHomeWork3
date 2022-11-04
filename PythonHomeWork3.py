
# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [int(input()), int(input()), int(input()), int(input()), int(input())]
# print(list)
# sum = 0

# for i in range(1, len(list), 2):
#     list.append(sum)
#     sum = sum + list[i]
    
# print(f'Сумма элементов списка, стоящих на нечетных позициях, равна {sum}')


# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# numbers = [2, 3, 4, 5, 6]
# list = []
# l = int(len(numbers)/2)
# if len(numbers) % 2 == 0:
#     for i in range(0, l, 1):
#         list.append(numbers[i]*numbers[len(numbers)-i-1])

# if len(numbers) % 2 == 1:
#     for i in range(0, l+1, 1):
#         list.append(numbers[i]*numbers[len(numbers)-i-1])

# print(list)

# numbers = [2, 3, 5, 6]
# list = []
# l = int(len(numbers)/2)
# if len(numbers) % 2 == 0:
#     for i in range(0, l, 1):
#         list.append(numbers[i]*numbers[len(numbers)-i-1])

# if len(numbers) % 2 == 1:
#     for i in range(0, l+1, 1):
#         list.append(numbers[i]*numbers[len(numbers)-i-1])

# print(list)


# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# numbers = [1.1, 1.2, 3.1, 5, 10.01]
# list = []
# for i in numbers:
#     list.append(round((i-int(i)),2))
# print(list)
# min = 1
# max = 0
# for i in list:
#     if (i <= min, i != 0):
#         min = i
#     if i >= max:
#         max = i  
# print(f'Максимальное значение дробной части элементов: {max}')
# print(f'Минимальное значение дробной части элементов: {min}')
# print(max - min)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input('Введите число: '))
# digit = ''
# while number > 0:
#     digit = str(number % 2) + digit
#     number = number // 2
# print(digit)


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

num = int(input('Введите число: '))
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for num in range(1, num+1):
    list.append(fib(num))
    
print(list)




