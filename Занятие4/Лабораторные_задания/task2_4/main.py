def digit_sum(num: int) -> bool:
    if len(str(num)) == 4:  # TODO не забыть проерить, что число дожно быть четырехзначное
        return True if sum([int(item) for item in list(str(num))]) % 7 == 0 else False


if __name__ == "__main__":
    print(digit_sum(1234))
    print(digit_sum(7777))
