if __name__ == "__main__":
    int_a = int(input("Enter A: "))
    int_b = int(input("Enter B: "))
    summa = ((int_a + int_b) ** 2)
    sqrt_sum = ((int_a ** 2) + (int_b ** 2))
    if summa > sqrt_sum:
        print("Квадрат суммы выше, чем сумма квадратов")
    elif summa == sqrt_sum:
        print("Они идентичны")
    else:
        print("Сумма квадратов больше, чем квадрат суммы")
