# -*- coding: UTF-8 -*-
# Copyright 2025 (c) Alex's GlowCity Studio.

import sys
import os
import platform
import random
import time
import datetime


def clear_output():
    system = platform.system()
    if system == "Linux":
        print("\033[H\033[J", end="")
    elif system == "Windows":
        print("Windows SUCK")
        os.system("cls")


# ONE OR TWO PLAYERS
# PLEASE ENTER NUMBER OF PLAYERS
# 修正后的 BOARD_TEMPLATE，每行左对齐
BOARD_TEMPLATE = """\
*               |                |
                |                |
        1       |        2       |        3
                |                |
                |                |
----------------+----------------+----------------
                |                |
                |                |
        4       |        5       |        6
                |                |
                |                |
----------------+----------------+----------------
                |                |
                |                |
        7       |        8       |        9
                |                |
                |                |
"""

# 起始索引
# (行, 列): (行索引, 列索引) 重新计算索引
BOARD_POSITIONS = {
    (0, 0): (2, 8),
    (0, 1): (2, 25),
    (0, 2): (2, 42),
    (1, 0): (8, 8),
    (1, 1): (8, 25),
    (1, 2): (8, 42),
    (2, 0): (14, 8),
    (2, 1): (14, 25),
    (2, 2): (14, 42),
}

# 坐标映射
MOVE_MAP = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


def print_centered_board(board_lines):
    for line in board_lines:
        print(line)


def set_board(board):
    template_lines = BOARD_TEMPLATE.strip().split("\n")
    current_board_lines = [list(line) for line in template_lines]

    for r in range(3):
        for c in range(3):
            player_char = board[r][c]
            template_row_idx, template_col_idx = BOARD_POSITIONS[(r, c)]

            # 空白格
            if player_char != " ":
                current_board_lines[template_row_idx][template_col_idx] = player_char
            else:
                # (r, c) 占位符
                num_placeholder = None
                for num, (map_r, map_c) in MOVE_MAP.items():
                    if map_r == r and map_c == c:
                        num_placeholder = str(num)
                        break
                if num_placeholder:
                    current_board_lines[template_row_idx][template_col_idx] = (
                        num_placeholder
                    )
                else:
                    # 回退占用符
                    current_board_lines[template_row_idx][template_col_idx] = " "

    final_board_display = ["".join(line) for line in current_board_lines]
    print_centered_board(final_board_display)


def check_win(board, player):
    # 行列
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    # 对角
    if all(board[i][i] == player for i in range(3)) or all(
        board[i][2 - i] == player for i in range(3)
    ):
        return True
    return False


def check_draw(board):
    return all(cell != " " for row in board for cell in row)


def get_valid_move(board):
    while True:
        try:
            move_input = int(input("ENTER YOUR MOVE: "))
            if 1 <= move_input <= 9:
                row, col = MOVE_MAP[move_input]
                if board[row][col] == " ":
                    return row, col
                else:
                    print("POSITION ALREADY TAKEN")
            else:
                print("INVALID MOVE")
        except ValueError:
            print("错误: 非法参数 (请输入数字)")
        except KeyboardInterrupt:
            sys.exit("QUIT GAME")


def minimax(board, depth, is_maximizing_player, wopr_char, opponent_char):
    if check_win(board, wopr_char):
        return 1
    if check_win(board, opponent_char):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing_player:
        best_score = -float("inf")
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = wopr_char
                    score = minimax(board, depth + 1, False, wopr_char, opponent_char)
                    board[r][c] = " "
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = opponent_char
                    score = minimax(board, depth + 1, True, wopr_char, opponent_char)
                    board[r][c] = " "
                    best_score = min(best_score, score)
        return best_score


def find_best_move(board, wopr_char, opponent_char):
    best_score = -float("inf")
    best_moves = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = wopr_char
                score = minimax(board, 0, False, wopr_char, opponent_char)
                board[r][c] = " "

                if score > best_score:
                    best_score = score
                    best_moves = [(r, c)]
                elif score == best_score:
                    best_moves.append((r, c))

    if best_moves:
        return random.choice(best_moves)
    return None


def main():
    print("ONE OR TWO PLAYERS?")

    gamemode = ""
    while gamemode not in ["ONE", "TWO", "ZERO"]:
        gamemode = input("PLEASE LIST NUMBER OF PLAYERS: ").upper()

    human = ""
    wopr = ""
    wopr_x = ""
    wopr_o = ""

    x_wins = 0
    o_wins = 0
    draws = 0

    if gamemode == "TWO":
        player_choice = ""
        while player_choice not in ["X", "O"]:
            player_choice = input("X OR O? ").upper()
        human = player_choice
        wopr = "O" if human == "X" else "X"
        time.sleep(1.0)
    elif gamemode == "ZERO":
        wopr_x = "X"
        wopr_o = "O"
        time.sleep(1.0)

    num_games = 1
    if gamemode == "ZERO":
        num_games = 10

    # 棋盘状态
    for game_count in range(num_games):
        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = "X"

        while True:
            clear_output()
            set_board(board)
            print(f"PLAYER({current_player})")

            row, col = None, None

            if gamemode == "ONE":
                row, col = get_valid_move(board)
            elif gamemode == "TWO":
                if current_player == human:
                    row, col = get_valid_move(board)
                else:
                    time.sleep(0.5)
                    row, col = find_best_move(board, wopr, human)
                    if row is None:
                        break
            elif gamemode == "ZERO":
                time.sleep(0.5)
                if current_player == "X":
                    row, col = find_best_move(board, wopr_x, wopr_o)
                else:
                    row, col = find_best_move(board, wopr_o, wopr_x)
                if row is None:
                    break

            board[row][col] = current_player

            if check_win(board, current_player):
                clear_output()
                set_board(board)
                print(f"{current_player} WINS!")
                if gamemode == "ZERO":
                    if current_player == "X":
                        x_wins += 1
                    else:
                        o_wins += 1
                    time.sleep(1)
                break

            if check_draw(board):
                time.sleep(0.5)
                clear_output()
                set_board(board)
                print("STALEMATE.")
                if gamemode == "ZERO":
                    draws += 1
                    time.sleep(1)
                else:
                    print("WANT TO PLAY AGAIN?")
                break

            current_player = "O" if current_player == "X" else "X"

        if gamemode == "ZERO" and game_count < num_games - 1:
            time.sleep(1)

    if gamemode == "ZERO":
        clear_output()
        time.sleep(2)
        print("A STRANGE GAME.")
        print("THE ONLY WINNING MOVE IS NOT TO PLAY.")


if __name__ == "__main__":
    main()
