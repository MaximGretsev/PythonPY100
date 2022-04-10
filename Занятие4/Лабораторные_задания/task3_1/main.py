def get_count_char(str_: str) -> dict:

    str_ = str_.lower()  # TODO для начала нужно перевести текст в нижний регистр и не забыть что возвращается копия
    char_dict = {}  # словарь для подсчета количества символов

    for char in str_:
        if char.isalpha():  # TODO с помощью метода строк isalpha будем проверять, является ли символ буквой
            if char in char_dict:  # TODO проверяем есть ли уже символ среди ключей
                char_dict[char] += 1  # TODO если есть, то увеличиваем значение на 1
            else:
                char_dict[char] = 1  # TODO в противном случае создаем новый элемент в словаре
    return char_dict


def frequency_chars(char_dict: dict) -> dict:
    total_count = sum(char_dict.values())  # TODO найти сумму всех значений словаря

    return {char: round(value / total_count, 3) for char, value in char_dict.items()}  # TODO с помощью dict comprehension возвращаем словарь с процентными соотношениями значений

# Тут я тоже половинку украл, потому что не совсем понятно описано, чего сделать-то надо было.

if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    chars_counter = get_count_char(main_str)
    print(frequency_chars(chars_counter))
