def get_max_length_word(str_words):
    words_list_without_empty_string = []
    for word in str_words.split(" "):
        if word:
            words_list_without_empty_string.append(word)

    max_len = 0  # пусть изначально длина самого длинного слова равна 0
    for word in words_list_without_empty_string:
        current_word_len = len(word)
        if current_word_len > max_len:
            max_len = current_word_len

    max_len_words = []
    for word in words_list_without_empty_string:
        if len(word) == max_len:
            max_len_words.append(word)

    return max_len_words


if __name__ == "__main__":
    print(get_max_length_word("раз два три"))
    print(get_max_length_word("раз два три четыре"))
