from models import init_field, is_win, has_empty_cell, EMPTY_SYMBOL, is_empty_cell, SIZE_FIELD, set_cell
from conf import FIRST_PLAYER, SECOND_PLAYER


def main():
    field = init_field()
    print_field(field)

    current_player, next_player = FIRST_PLAYER, SECOND_PLAYER
    dict_players_step = {
        FIRST_PLAYER: player_step,
        SECOND_PLAYER: enemy_step
    }

    while True:
        current_player_step_func = dict_players_step[current_player]
        current_player_step_func(field, current_player)
        print_field(field)
        if is_win(field):
            print_win_message(current_player)
            break
        if not has_empty_cell(field):
            print_draw_message()
            break

        current_player, next_player = next_player, current_player

    # Тут меняется ход игрока. Т.е. игроки меняются местами.
    # В словаре находятся вызовы функций для хода каждого игрока.


def print_win_message(player_symbol: str) -> None:
    print(f"Выиграл игрок {player_symbol}!")


def print_draw_message():
    print("Ничья, брат")


def player_step(field, player_symbol: str):
    while True:
        try:
            coord = int(input("Введите номер ячейки для хода: "))
        except ValueError:
            print("Вы ввели не целое число :( ")
            continue

        if not 1 <= coord <= 9:
            print("Введите число в диапазоне от 1 до 9")
            continue

        x = (coord - 1) // SIZE_FIELD
        y = (coord - 1) % SIZE_FIELD
        if not is_empty_cell(field, x, y):
            print("Ячейка занята!")
            continue

        set_cell(field, row_index=x, col_index=y, player_symbol=player_symbol)
        break


def enemy_step(field, player_symbol: str):
    player_step(field, player_symbol)


def print_field(field: list[list]) -> None:
    start_num = 1
    for i in range(len(field)):
        for j in range(len(field[i])):
            print_symbol = start_num if field[i][j] == EMPTY_SYMBOL else field[i][j]
            start_num += 1
            print(print_symbol, "|",  end="\t")
        print()
    print("-" * 11)


if __name__ == "__main__":
    main()
