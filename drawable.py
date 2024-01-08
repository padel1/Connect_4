

top_piece_padding = 84
left_piece_padding = 148
vertical_distance = 59
horizontal_distance = 68


def draw_board(screen, board, piece1, piece2):
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row, col] == 1:
                # print(row, col)
                screen.blit(piece1, (left_piece_padding + col * horizontal_distance,
                                     top_piece_padding + row * vertical_distance))

            if board[row, col] == 2:
                screen.blit(piece2, (left_piece_padding + col * horizontal_distance,
                                     top_piece_padding + row * vertical_distance))


def draw_moving_piece(screen, piece, x, y):
    piece_rect = piece.get_rect(topleft=(x, y))
    screen.blit(piece, piece_rect)


def get_column(x):
    if x <= 205:
        return 0
    if x <= 270:
        return 1
    if x <= 340:
        return 2
    if x <= 410:
        return 3
    if x <= 477:
        return 4
    if x <= 545:
        return 5
    return 6
