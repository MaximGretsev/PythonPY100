def main():
    n = 1  # первое натуральное число
    current_sum = 0  # текущая сумма
    max_sum = 500  # максимальная сумма
    count_numbers = 0
    sum_ = 0
    while True:
        sqrt_sum = (current_sum + (n ** 2))
        if sqrt_sum > max_sum:
            break
        if sqrt_sum < max_sum:
            current_sum += n ** 2
            n += 1
    return n, current_sum


if __name__ == "__main__":
    count_numbers, sum_ = main() # множественная распаковка из функции.
    print(count_numbers, sum_) # передается n в count_numbers и current_sum в sum_
