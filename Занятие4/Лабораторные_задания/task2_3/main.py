def task(num: int) -> bool:  # TODO добавить аннотацию типов
    list_ = [int(digit) for digit in str(abs(num))]
    return True if 10 <= sum(list_) <= 99 else False
    # Я своровал код, потому что функцию abs мы вроде не успели пройти. Но я в гугле разобрался.

if __name__ == "__main__":
    print(task(12))
    print(task(555))
    print(task(-12))
    print(task(-149))
