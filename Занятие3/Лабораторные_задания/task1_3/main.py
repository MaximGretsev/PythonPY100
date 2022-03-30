def get_list_number_divisors(number):
    list_number = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_number.append(i)
    return list_number


if __name__ == "__main__":
    print(get_list_number_divisors(2 ** 16))
