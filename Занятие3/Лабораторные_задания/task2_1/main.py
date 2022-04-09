def task(str1: str, str2: str, k: int):
    if str1[0:k] == str2[0:k]:
        print("ДА")
    else:
        print("НЕТ")


if __name__ == "__main__":
    task("abc", "abcde", 3)
    task("abcba", "abcde", 5)
