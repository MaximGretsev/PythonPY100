def task(num: int) -> bool:
    return True if str(num) == str(num)[::-1] else False


if __name__ == "__main__":
    print(task(123))
    print(task(1111111))
