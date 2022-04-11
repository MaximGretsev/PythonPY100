if __name__ == "__main__":
    # матрица или таблица это список строк,
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for row_index in range(len(matrix)-1, -1, -1):  # TODO Как получить количество строк?
        for col_index in range(len(matrix[row_index])-1, -1, -1):  # TODO как получить количество столбцов?
            print(matrix[row_index][col_index], end="\t")
        print()
