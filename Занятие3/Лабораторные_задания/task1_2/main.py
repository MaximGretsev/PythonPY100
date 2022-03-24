def factorial(n):# TODO запишите здесь функцию factorial
    count = 1
    for i in range(1, n + 1):
        count *= i
    return count


if __name__ == "__main__":
    print(factorial(5))# TODO распечатать результат выполнения функции factorial от числа 5
