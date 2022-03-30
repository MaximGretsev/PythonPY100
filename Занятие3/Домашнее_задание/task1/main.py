def input_numbers():
    list_numbers = []
    while True:
        input_num = int(input("Enter new number: "))
        if input_num < 0:
            list_numbers.append(input_num)
            break
        if 3 <= input_num <= 13:
            list_numbers.append(input_num)

    return list_numbers


if __name__ == "__main__":
    numbers = input_numbers()
    print(numbers)
