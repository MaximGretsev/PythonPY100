from models import init_field, is_win, has_empty_cell

FIRST_PLAYER = "X"
SECOND_PLAYER = "O"


def main():
    field = init_field()
    print_field(field)

    current_player, next_player = FIRST_PLAYER, SECOND_PLAYER

    while True:
        player_step(field, current_player)
        print_field(field)
        if is_win(field):
            print_win_message(current_player)
            break
        if not has_empty_cell(field):
            print_draw_message()
            break

        enemy_step(field, next_player)
        print_field(field)
        if is_win(field):
            print_win_message(next_player)
            break
        if not has_empty_cell(field):
            print_draw_message()
            break


def print_win_message(player_symbol: str) -> None:
    ...


def print_draw_message():
    ...


def player_step(field, player_symbol: str):
    ...


def enemy_step(field, player_symbol: str):
    player_step(player_symbol)


def print_field(field: list[list]) -> None:
    ...


if __name__ == "__main__":
    main()
