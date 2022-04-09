if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    new_list_even: list = [num for num in list_ if num % 2 == 0]
    new_list_not_even: list = [num for num in list_ if num % 2 == 1]

    len_even, len_not_even = len(new_list_even), len(new_list_not_even)

    if len_not_even > len_even:
        print("Нечетные ")
    elif len_even > len_not_even:
        print("Четные ")
    else:
        print("Адинакава")
