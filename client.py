import math
import pygame
from settings import *
from stages import Stage
from pygame.locals import *
from game import Game
from drawable import *
import sys

pygame.init()

screen = pygame.display.set_mode((screen_w, screen_h))

font = pygame.font.SysFont(None, 36)


def display_win_dialog(screen, clock, game, stage, page):
    win_dialog_timer = 3000
    win_dialog_start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - win_dialog_start_time < win_dialog_timer:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))

        win_text = "Player {} wins!".format(game.check_for_win(game.board))
        text_surface = font.render(win_text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(
            center=(screen_w // 2, screen_h // 2))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(FPS)

    game = Game()
    stage = Stage(screen, game)
    page = Page()

    return game, stage, page


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game()
    stage = Stage(screen, game)
    page = Page()

    while run:
        screen.fill((0, 0, 0))
        if (
            game.player == 2
            and stage.stage == page.game
            and not game.is_full(game.board)
            and stage.game_mode == "player_vs_AI"
        ):
            if stage.diff_idx == 0:
                pygame.time.delay(1000)
            if stage.diff_idx == 0:
                game.depth = 1
                cord, val = game.minimax_alpha_beta(
                    game.board, game.depth, -math.inf, math.inf, True
                )
            elif stage.diff_idx == 1:
                game.depth = 3
                cord, val = game.minimax_alpha_beta(
                    game.board, game.depth, -math.inf, math.inf, True
                )
            else:
                game.depth = 5
                cord, val = game.minimax_alpha_beta(
                    game.board, game.depth, -math.inf, math.inf, True
                )

            game.mark_position(game.player, game.board, cord[0], cord[1])
            stage.dropSound.play()
            if game.check_for_win(game.board) == 2:

                print("player 2 wins")
                pygame.time.delay(1000)
                game, stage, page = display_win_dialog(
                    screen, clock, game, stage, page)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                x, y = pygame.mouse.get_pos()

                if stage.stage == page.game and not game.is_full(game.board):
                    print(game.player)
                    if game.player == 1:
                        if 140 <= x <= 610 and y <= 430:
                            print("player_1")
                            col = get_column(x)
                            row = game.get_empty_spot_in_col(game.board, col)
                            idx = game.mark_position(
                                game.player, game.board, row, col)

                            print(game.board)
                            if idx == -1:
                                print("bad move1")
                            else:
                                stage.dropSound.play()

                                if game.check_for_win(game.board) == 1:
                                    print("player 1 wins")
                                    game, stage, page = display_win_dialog(
                                        screen, clock, game, stage, page
                                    )
                    elif game.player == 2 and stage.game_mode == "player_vs_player":
                        if 140 <= x <= 610 and y <= 430:
                            print("player_2")
                            col = get_column(x)
                            row = game.get_empty_spot_in_col(game.board, col)
                            idx = game.mark_position(
                                game.player, game.board, row, col)

                            print(game.board)
                            if idx == -1:
                                print("bad move2")
                            else:
                                stage.dropSound.play()
                                if game.check_for_win(game.board) == 2:
                                    print("player 2 wins")
                                    game, stage, page = display_win_dialog(
                                        screen, clock, game, stage, page
                                    )

                    if hint_button_rect.collidepoint(x, y):
                        game.depth = 5
                        cord, val = game.minimax_alpha_beta(
                            game.board, 5, -math.inf, math.inf, True
                        )
                        game.mark_position(
                            game.player, game.board, cord[0], cord[1])
                        stage.dropSound.play()
                        if game.check_for_win(game.board) == 1:
                            print("player 2 wins")
                            game, stage, page = display_win_dialog(
                                screen, clock, game, stage, page
                            )

                if stage.stage == page.option:
                    if wp_surface_rect.collidepoint(x, y):
                        stage.choosed_piece = 1
                        game.player_piece = wp_surface
                        game.computer_piece = bp_surface
                    if player_vs_AI_button_rect.collidepoint(x, y):
                        if stage.game_mode == "player_vs_player":
                            stage.game_mode = "player_vs_AI"
                        else:
                            stage.game_mode = "player_vs_player"

                    if bp_surface_rect.collidepoint(x, y):
                        stage.choosed_piece = 2
                        game.player_piece = bp_surface
                        game.computer_piece = wp_surface

                    if diff_btn_rect.collidepoint(x, y):
                        if stage.diff_idx == 2:
                            stage.diff_idx = 0
                        else:
                            stage.diff_idx += 1
                elif stage.stage == page.menu:
                    if start_button_rect.collidepoint(x, y):
                        stage.stage = page.game
                    if option_button_rect.collidepoint(x, y):
                        stage.stage = page.option
                    if help_button_rect.collidepoint(x, y):

                        explanation_dialog = True
                        while explanation_dialog:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if (
                                    event.type == KEYDOWN
                                    or event.type == MOUSEBUTTONDOWN
                                ):
                                    explanation_dialog = False

                            screen.fill(
                                (255, 255, 255)
                            )  # Fill the screen with white color

                            # Display the explanation text each part in a variable

                            explanation_part1 = "Connect 4 is a classic two-player"
                            explanation_part2 = "game in which the players take turns"
                            explanation_part3 = "dropping colored discs from the top"
                            explanation_part4 = "into a vertically suspended grid."
                            explanation_part5 = "The objective of the game is to connect"
                            explanation_part6 = "four of one's own discs of the same color"

                            # Render each part of the explanation
                            text_surface1 = font.render(
                                explanation_part1, True, (0, 0, 0))
                            text_surface2 = font.render(
                                explanation_part2, True, (0, 0, 0))
                            text_surface3 = font.render(
                                explanation_part3, True, (0, 0, 0))
                            text_surface4 = font.render(
                                explanation_part4, True, (0, 0, 0))
                            text_surface5 = font.render(
                                explanation_part5, True, (0, 0, 0))
                            text_surface6 = font.render(
                                explanation_part6, True, (0, 0, 0))

                            # Get the rectangles for each part
                            text_rect1 = text_surface1.get_rect(
                                center=(screen_w // 2, screen_h // 2 - 100))
                            text_rect2 = text_surface2.get_rect(
                                center=(screen_w // 2, screen_h // 2 - 50))
                            text_rect3 = text_surface3.get_rect(
                                center=(screen_w // 2, screen_h // 2))
                            text_rect4 = text_surface4.get_rect(
                                center=(screen_w // 2, screen_h // 2 + 50))
                            text_rect5 = text_surface5.get_rect(
                                center=(screen_w // 2, screen_h // 2 + 100))
                            text_rect6 = text_surface6.get_rect(
                                center=(screen_w // 2, screen_h // 2 + 150))

                            # Blit each part onto the screen
                            screen.blit(text_surface1, text_rect1)
                            screen.blit(text_surface2, text_rect2)
                            screen.blit(text_surface3, text_rect3)
                            screen.blit(text_surface4, text_rect4)
                            screen.blit(text_surface5, text_rect5)
                            screen.blit(text_surface6, text_rect6)

                            pygame.display.flip()

                        pygame.event.clear()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if stage.stage == page.game:
                        stage.stage = page.menu
                    elif stage.stage == page.option:
                        stage.stage = page.menu
                    else:
                        sys.exit(0)

        x, y = pygame.mouse.get_pos()

        stage.mouse_x_pos = max(140, min(x - wp_surface.get_width() // 2, 550))

        if start_button_rect.collidepoint(x, y):
            stage.start_hovered = True
        else:
            stage.start_hovered = False

        if option_button_rect.collidepoint(x, y):
            stage.option_btn_hovered = True
        else:
            stage.option_btn_hovered = False

        if game.is_full(game.board):
            print("tie")
            pygame.time.delay(2000)

            game = Game()
            stage.game = game

        if stage.stage == page.game:
            stage.game_page()
        elif stage.stage == page.menu:
            stage.menu_page()
        elif stage.stage == page.option:
            stage.option_page()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
