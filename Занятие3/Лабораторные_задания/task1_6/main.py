months = 10
procent = 0.03


def life_money(spend):
    in_month = spend * procent
    salary_in_month = in_month + spend
    salary = salary_in_month * (months - 1)
    return salary


if __name__ == "__main__":
    print(life_money(2000))

# TODO Потыкать дома. Блин ничерта не понятно.