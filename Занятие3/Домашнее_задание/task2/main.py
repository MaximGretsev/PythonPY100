def check_string(str_):
    if not str_:
        return False

    base = set("01")
    for d in set(str_):  # выделяем все уникальные символы из строки
        if d not in base:
            return False
    return True


if __name__ == "__main__":
    print(check_string("1010101010"))
    print(check_string("101021231010103"))
    print(check_string("asdawqe"))
    print(check_string(""))
