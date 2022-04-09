def is_exist_fruit(cart_dict: dict, fruit_key: str) -> bool:
    # if fruit_key in cart_dict:  # TODO записать с помощью inline if
    return True if fruit_key in cart_dict else False


if __name__ == "__main__":
    cart: dict = {
        "apple": 80,
        "orange": 65,
        "banana": 40
    }

    exist_fruit: str = "apple"
    missing_fruit: str = "pineapple"

    print(is_exist_fruit(cart, exist_fruit))
    print(is_exist_fruit(cart, missing_fruit))
