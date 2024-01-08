import random
import numpy as np
from settings import *
from drawable import *
import copy
import math

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4


class Game:
    def __init__(self) -> None:
        self.board = np.zeros((6, 7), dtype="int")
        self.player = 1
        self.both_starts = False
        self.player_piece = wp_surface
        self.computer_piece = bp_surface
        self.depth = 4
        # self.best_move = None

    def move(self, x, y):
        self.board[x, y] = self.player

    def change_turn(self):
        self.player = 1 if self.player == 2 else 2

    def is_full(self, board):
        return not 0 in board

    def check_for_win(self, board):
        for y in range(len(board)):
            for x in range(len(board[0]) - 3):
                if (
                    board[y][x]
                    == board[y][x + 1]
                    == board[y][x + 2]
                    == board[y][x + 3]
                    != 0
                ):
                    return board[y][x]

        # Vertical
        for x in range(len(board[0])):
            for y in range(len(board) - 3):
                if (
                    board[y][x]
                    == board[y + 1][x]
                    == board[y + 2][x]
                    == board[y + 3][x]
                    != 0
                ):
                    return board[y][x]

        # Diagonal \
        for x in range(len(board[0]) - 3):
            for y in range(len(board) - 3):
                if (
                    board[y][x]
                    == board[y + 1][x + 1]
                    == board[y + 2][x + 2]
                    == board[y + 3][x + 3]
                    != 0
                ):
                    return board[y][x]

        # Diagonal /
        for y in range(len(board) - 3):
            for x in range(3, len(board[0]) - 1):
                if (
                    board[y][x]
                    == board[y + 1][x - 1]
                    == board[y + 2][x - 2]
                    == board[y + 3][x - 3]
                    != 0
                ):
                    return board[y][x]

        return 0

    def get_empty_spot_in_col(self, board, col):
        for i in range(len(board)):
            if board[i][col] != 0:
                return i - 1
        if board[-1, col] == 0:
            return i
        else:
            return -1

    def get_empty_spot(self, board):
        empty_spot = []
        for col in range(len(board[0])):
            idx = self.get_empty_spot_in_col(board, col)
            if idx != -1:
                empty_spot.append((idx, col))
        return empty_spot

    def mark_position(self, player, board, row, col):
        if row == -1:
            return -1
        board[row, col] = player
        self.change_turn()
        return 1

    def random_move(self, board, player):
        spotes = self.get_empty_spot(board)
        random = np.random.randint(0, len(spotes))
        row, col = spotes[random]
        self.mark_position(player, board, row, col)

    def evaluate_window(self, window, piece):
        score = 0
        opp_piece = 1
        if piece == 1:
            opp_piece = 2

        if window.count(piece) == 4:
            score += 100
        elif window.count(piece) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(piece) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opp_piece) == 3 and window.count(0) == 1:
            score -= 5

        return score

    # try to improve this function
    @staticmethod
    def count_sequence(board, player, length):
        # Function will count the amount of connected pieces
        # that are a certain length for a certain player.
        def vertical(row, col):
            count = 0
            for rowIndex in range(row, 6):
                if board[rowIndex][col] == board[row][col]:
                    count += 1
                else:
                    break
            if count >= length:
                return 1
            else:
                return 0

        def horizontal(row, col):
            count = 0
            for colIndex in range(col, 7):
                if board[row][colIndex] == board[row][col]:
                    count += 1
                else:
                    break
            if count >= length:
                return 1
            else:
                return 0

        def negative_diagonal(row, col):
            count = 0
            col_index = col
            for rowIndex in range(row, -1, -1):
                if col_index > 6:
                    break
                elif board[rowIndex][col_index] == board[row][col]:
                    count += 1
                else:
                    break
                col_index += 1
            if count >= length:
                return 1
            else:
                return 0

        def positive_diagonal(row, col):
            count = 0
            col_index = col
            for rowIndex in range(row, 6):
                if col_index > 6:
                    break
                elif board[rowIndex][col_index] == board[row][col]:
                    count += 1
                else:
                    break
                col_index += 1
            if count >= length:
                return 1
            else:
                return 0

        total_count = 0

        for row in range(6):
            for col in range(7):
                if board[row][col] == player:
                    total_count += vertical(row, col)
                    total_count += horizontal(row, col)
                    total_count += (positive_diagonal(row, col) +
                                    negative_diagonal(row, col))

        return total_count

    def utility_value(self, board, player):
        # This function is used to evaluate the current score of a board.
        if player == 2:
            opponent = 1
        else:
            opponent = 2

        player_fours = self.count_sequence(board, player, 4)
        player_threes = self.count_sequence(board, player, 3)
        player_twos = self.count_sequence(board, player, 2)
        player_score = player_fours * 9999 + player_threes * 99 + player_twos * 9

        opponent_fours = self.count_sequence(board, opponent, 4)
        opponent_threes = self.count_sequence(board, opponent, 3)
        opponent_twos = self.count_sequence(board, opponent, 2)
        opponent_score = opponent_fours * 9999 + \
            opponent_threes * 99 + opponent_twos * 9

        if opponent_fours > 0:
            return float('-inf')
        else:
            return player_score - opponent_score

    def score_position(self, board, piece):
        score = 0

        # Score center column
        center_array = [int(i) for i in list(board[:, COLUMN_COUNT // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(ROW_COUNT):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c: c + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score Vertical
        for c in range(COLUMN_COUNT):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(ROW_COUNT - 3):
                window = col_array[r: r + WINDOW_LENGTH]
                score += self.evaluate_window(window, piece)

        # Score posiive sloped diagonal
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + 3 - i][c + i]
                          for i in range(WINDOW_LENGTH)]
                score += self.evaluate_window(window, piece)

        return score

    def minimax_alpha_beta(self, board, depth, alpha, beta, is_maximize):
        state = self.check_for_win(board)

        if state == 1:
            return None, -9999999
        if state == 2:
            return None, 9999999

        if depth == 0:
            if self.depth % 2 == 0:
                x = self.score_position(board, 2)
                # x = self.utility_value(board, 2)
                return None, x
            else:
                x = self.score_position(board, 2)
                # x = self.utility_value(board, 2)
                return None, x

        if self.is_full(board):
            return None, 0

        if is_maximize:
            max_val = -math.inf

            squares = self.get_empty_spot(board)
            best_node = random.choice(squares)

            for i, j in squares:
                tmp_board = copy.deepcopy(board)
                tmp_board[i, j] = 2
                val = self.minimax_alpha_beta(
                    tmp_board, depth - 1, alpha, beta, not is_maximize
                )[1]

                if val > max_val:
                    max_val = val
                    best_node = (i, j)

                alpha = max(alpha, val)
                if beta <= alpha:
                    break

            return best_node, max_val
        else:
            min_val = math.inf

            squares = self.get_empty_spot(board)
            best_node = random.choice(squares)
            for i, j in squares:
                tmp_board = copy.deepcopy(board)
                tmp_board[i, j] = 1

                val = self.minimax_alpha_beta(
                    tmp_board, depth - 1, alpha, beta, not is_maximize
                )[1]
                if val < min_val:
                    min_val = val
                    best_node = (i, j)
                    self.best_move = best_node
                beta = min(beta, val)
                if beta <= alpha:
                    break

            return best_node, min_val
