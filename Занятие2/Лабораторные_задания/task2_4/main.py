if __name__ == "__main__":
    phrase = "Hello,world"
    initial_offset = 5  # TODO чему равно начальное смещение?
    for index, value in enumerate(phrase, start=initial_offset): # TODO как использовать начальное смещение в команде enumerate?
        print(" " * initial_offset, value)
        initial_offset += 1