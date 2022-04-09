if __name__ == "__main__":
    number: int = 123456789

    list_digits: list = [int(item) for item in list(str(number))]
    print(list_digits)

    print(sum(list_digits))  # TODO найти сумму цифр числа

    print(sum([item for item in list_digits if item % 2 == 0]))  # TODO найти сумму всех четных чисел

    print(len(list_digits))  # TODO найти количество цифр

    print(min(list_digits))  # TODO найти минимальную цифру

    print([item for item in list_digits if item % 2 != 0])  # TODO все цифры стоящие на нечетных местах
    # print((list_digits[::2]))
    print(list_digits[0] - list_digits[-1])  # TODO найти разность между первой и последней цифрой
