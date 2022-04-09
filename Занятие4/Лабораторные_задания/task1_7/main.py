if __name__ == "__main__":
    list_: list = [4, -1, 10, -1, 4, -3, -6, 8, 6, 9]
    compare: float = sum(list_) / len(list_)
    # new_list: list = [list_[i] - compare for i in range(len(list_))]  # TODO Заполните список с помощью list
    #  comprehension
    new_list: list = [new_num - compare for new_num in list_]
    print(new_list)
