# Напишите ваше решение
PERCENT = 0.13

salary = int(input('Сколько вы получаете?: '))
value = salary * PERCENT
offer = salary - value
print(value, offer)