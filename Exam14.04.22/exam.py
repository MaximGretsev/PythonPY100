# n = 5

# Записать логическое выражение, которое определяет, принадлежит ли число А интервалу от -137 до -51 или интервалу от 123 до 55.
# Записать логические выражения, которые имеют значение «истина» только при выполнении указанных условий - неверно, что x>0 и x<5.
# Дано натуральное число. Определить, является ли оно четным, или оканчивается цифрой 3.

# 1.5
# ___________
# int_a: int = int(input('Enter number: '))
# print(((-137) <= int_a <= (-51)) or (123 >= int_a >= 55))


# 1.15
# ___________
# bool_val: int = int(input('Enter your number: '))
# if not 0 < bool_val < 5:
#     print("True")
# else:
#     print("False")


# 1.25
# ___________
# nature: int = int(input('Enter number: '))
# print(nature % 2 == 0 or nature % 10 == 3)


# 2.5
"""
Дано трехзначное число. Определить:
а) является ли сумма его цифр двузначным числом;
б) является ли произведение его цифр трехзначным числом.
"""

# num: int = int(input("Enter your number. Format XXX: "))
#
# result: list = [int(item) for item in str(num)]
# if 9 < sum(result) < 99:
#     print("Сумма чисел - двухзначная")
# else:
#     print("Сумма чисел не двухзначная")
#
# count: int = 1
# for i in result:
#     count *= i
# print(count)
#
# if not 99 < count < 1000:
#     print("Произведение цифр не трехзначное")
# else:
#     print("Произведение цифр - трехзначное")

# 3.5
import random

"""
Мастям игральных карт условно присвоены следующие порядковые номера: 
масти "пики" — 1, масти "трефы" — 2, масти "бубны" — 3, масти "червы" — 4. По заданному номеру масти m (1   < = m <= 4) 
определить название соответствующей масти. """

# card: int = int(input("Введите номер от 1 до 4: "))
# card_dict: dict = {1: "Пики", 2: "Трефы", 3: "Бубны", 4: "Червы"}
# if card in card_dict:
#     print(f'Вы выбрали карту {card_dict[card]}')


# 4.5

"""
Найти количество и произведение отрицательных элементов, а также сумму нечетных элементов. 
"""
# arr_num: list = [-1, 2, 3, 5, -4, -3, 2, 1, -2, 10]
# negative_num: list = [item for item in arr_num if item < 0]
# sum_odd: list = [item for item in arr_num if item % 2 != 0]
# print(negative_num, len(negative_num))
# print(sum_odd, sum(sum_odd))


# 5 Все.
"""
5. 1
Гипотеза Сиракуз гласит, что любое натуральное число сводимо к единице при следующих действиях над ним: 
а) если число четное, то разделить его пополам, б) если нечетное - умножить на 3, прибавить 1 и результат разделить на 2. 
Над вновь полученным числом вновь повторить действия a) или б) в зависимости от его четности. 
Рано или поздно число станет равным 1. 
"""
# n: int = int(input("Введите число для проверки Гипотезы :) : "))
# while n > 1:
#     if n % 2 == 0:
#         n = n // 2
#     elif n % 2 != 0:
#         n = ((n * 3) + 1) // 2
#     print(n)

"""
5.2
Начав тренировки, спортсмен в первый день пробежал n км. 
Каждый день он увеличивал дневную норму на y% нормы предыдущего дня. Какой суммарный путь пробежит спортсмен за x дней? 
"""

# run: int = 10
# day_norm: float = 1.1
# count_day: int = int(input("Сколько дней бегает спортсмен?: "))
# count = 1
# for i in range(1, count_day + 1):
#     count = (run * day_norm)
#     print(count)
#     print(f"Day {i}")


"""
5.3 
Определить, сколько в введенном пользователем числе четных цифр, а сколько нечетных.	
"""
# user_num: int = int(input("Введите число: "))
#
# even: list = [int(item) for item in str(user_num)]
# even_count: int = 0
# odd_count: int = 0
# for i in even:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#
# print(f'Четных цифр {even_count}, а нечетных рооовно вот столько: {odd_count}')


"""
Написать программу в виде оператора цикла с параметром, обеспечивающий вывод на экран "столбиком" всех 
целых чисел от 10 до 30. Оформить этот фрагмент в виде:
а. оператора цикла с предусловием
б. оператора цикла с постусловием. 
"""

# С постусловием цикл

# start = 10
# while True:
#     print(start)
#     start += 1
#     if start > 30:
#         break

# С предусловием

# start = 10
# while start <= 30:
#     print(start)
#     start += 1


"""
В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64. Дано натуральное число n. 
Как наименьшим количеством таких денежных купюр можно выплатить сумму n (указать количество каждой из используемых 
для выплаты купюр)? Предполагается, что имеется достаточно большое количество купюр всех достоинств.
"""
bill: [1, 2, 4, 8, 16, 32, 64]