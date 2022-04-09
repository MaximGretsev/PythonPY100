def is_palindrome(str_: str):
    lw_str = ''.join(str_.lower().split())  # TODO привести строку к единому регистру и избавиться от пробелов
    print(lw_str)
    if lw_str == lw_str[::-1]:  # TODO проверка палиндрома
        print("Строка палиндром")
        print(lw_str)
    else:
        print("Строка не палиндром")
        print(lw_str)


if __name__ == "__main__":
    is_palindrome("Кит на море не романтик")
    is_palindrome("Прочая строка")
