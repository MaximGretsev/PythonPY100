"""

"""
from conf import SIZE_FIELD, EMPTY_SYMBOL


def init_field(size: int = SIZE_FIELD) -> list[list]:
    return [
        [EMPTY_SYMBOL for _ in range(size)]
        for _ in range(size)
    ]


def is_empty_cell(field: list[list], row_index: int, col_index: int) -> bool:
    return field[row_index][col_index] == EMPTY_SYMBOL


def has_empty_cell(field: list[list]) -> bool:
    for row in field:
        for cell in row:
            if cell == EMPTY_SYMBOL:
                return True
    return False


def is_win(field: list[list]) -> bool:
    """

    :param field:
    :return:
    """
    # Динамическая штука проверки комбинации. Но вот как проверять диагонали?
    win_comb_2 = [
        [(i, j) for j in range(SIZE_FIELD)]
        for i in range(SIZE_FIELD)
    ]

    win_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 2), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for win_comb in win_combinations:
        cell_1_coord, cell_2_coord, cell_3_coord = win_comb
        cell_1 = get_cell(field, cell_1_coord[0], cell_1_coord[1])
        cell_2 = get_cell(field, cell_2_coord[0], cell_2_coord[1])
        cell_3 = get_cell(field, cell_3_coord[0], cell_3_coord[1])

        if cell_1 == cell_2 == cell_3 != EMPTY_SYMBOL:
            return True

    return False


def get_cell(field: list[list], row_index: int, col_index: int):
    return field[row_index][col_index]


def set_cell(field: list[list], row_index: int, col_index: int, player_symbol) -> None:
    field[row_index][col_index] = player_symbol


if __name__ == '__main__':
    test_field = init_field()
    print(test_field)

    assert is_win(test_field) == False