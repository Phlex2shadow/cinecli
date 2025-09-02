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


def set_board(board):
    for i, row in enumerate(board):
        print(" " + " ┃ ".join(row))
        if i < 2:
            print("━━━╋━━━╋━━━")


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
            row = int(input("X: ")) - 1
            col = int(input("Y: ")) - 1
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("错误: 落点位置已被占用")
            else:
                print("错误: 数值超出范围")
        except ValueError:
            print("错误: 非法参数")
        except KeyboardInterrupt:
            sys.exit("对局终止")


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
                print(f"{current_player} 方获胜")
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
        time.sleep(1)
        print("A STRANGE GAME.")
        print("THE ONLY WINNING MOVE IS NOT TO PLAY.")


if __name__ == "__main__":
    main()
