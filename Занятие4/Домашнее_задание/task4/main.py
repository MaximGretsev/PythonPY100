def is_lucky_number(num: int) -> bool:
    # print(len(str(num)) != 6)
    # return True if (sum(str(num)[::1]) / 2 == sum(str(num)[::-1]) / 2) else False
    if len(str(num)) != 6:
        raise ValueError("Число не шестизначное :(")

    list_digits = [int(digit) for digit in str(num)]
    return True if sum(list_digits[:3]) == sum(list_digits[3:]) else False


if __name__ == "__main__":
    print(is_lucky_number(123321))
    print(is_lucky_number(111111))
    print(is_lucky_number(123456))
    print(is_lucky_number(456243))
