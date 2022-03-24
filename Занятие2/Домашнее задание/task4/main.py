if __name__ == "__main__":
    list_ = []
    for i in range(3, 15):
        list_.append(i * 2)
    print(list_)
    min_index_value = 0
    min_value = list_[min_index_value]
    max_index_value = 0
    max_value = list_[max_index_value]
    for i in range(len(list_)):
        current_value = list_[i]
        if current_value > max_value:
            max_value = current_value
            max_index_value = i
    for i in range(len(list_)):
        current_min = list_[i]
        if current_min < min_value:
            current_min = min_value
            min_index_value = i
    list_[min_index_value], list_[max_index_value] = list_[max_index_value], list_[min_index_value]
    print(list_)
    print(list_[min_index_value])
    print(list_[max_index_value])

    pass
