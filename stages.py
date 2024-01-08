from settings import *
import pygame
from game import Game
from drawable import *
font = pygame.font.SysFont(None, 36)
class Stage:

    def __init__(self, screen, game) -> None:
        self.stage = "menu"
        self.screen = screen
        self.choosed_piece = 0
        self.start_hovered = False
        self.option_btn_hovered = False
        self.game = game
        self.mouse_x_pos = 100
        self.diff_idx = 0
        self.dropSound = pygame.mixer.Sound(
            "assets/sound/wooden_piece_falling_01.wav")
        self.game_mode = "player_vs_AI"

    def menu_page(self):

        # self.screen.blit(menu_background, (0, 0))
        transparent = pygame.Surface((800, 600), pygame.SRCALPHA)

        shadow_color = (0, 0, 0, 200)
        transparent.fill(shadow_color)
        # transparent.blit(menu_background, (0, 0))
        self.screen.blit(menu_background, (0, 0))
        self.screen.blit(transparent, (0, 0))
        self.screen.blit(logo, (screen_w//2 - logo.get_width()//2, 50))

        if self.start_hovered:
            self.screen.blit(play_btn_hovered, start_button_rect)
        else:
            self.screen.blit(play_btn, start_button_rect)
        if not self.option_btn_hovered:
            self.screen.blit(option_button, option_button_rect)
        else:
            self.screen.blit(option_button, option_button_rect)
        self.screen.blit(help_button, help_button_rect)

    def option_page(self):


        transparent = pygame.Surface((800, 600), pygame.SRCALPHA)

        shadow_color = (0, 0, 0, 180)
        transparent.fill(shadow_color)
        # transparent.blit(menu_background, (0, 0))
        self.screen.blit(option_background, (0, 0))
        self.screen.blit(transparent, (0, 0))

        if self.choosed_piece == 0:
            self.screen.blit(
                wp_surface, (screen_w // 2 -
                             wp_surface.get_width() + 70, screen_h // 2)
            )
            self.screen.blit(
                bp_surface, (screen_w // 2 +
                             bp_surface.get_width() // 2+100, screen_h // 2)
            )
        if self.choosed_piece == 1:
            self.screen.blit(
                wp_clicked_surface,
                (screen_w // 2 - wp_clicked_surface.get_width() +70, screen_h // 2),
            )
            self.screen.blit(
                bp_surface, (screen_w // 2 +
                             bp_surface.get_width() // 2+100, screen_h // 2)
            )
        if self.choosed_piece == 2:
            self.screen.blit(
                wp_surface, (screen_w // 2 -
                             wp_surface.get_width() +70, screen_h // 2)
            )
            self.screen.blit(
                bp_clicked_surface,
                (screen_w // 2 + bp_clicked_surface.get_width() // 2+100, screen_h // 2)
            )
        
        self.screen.blit(diff_arr[self.diff_idx], diff_btn_rect)

        if self.game_mode == "player_vs_player":
            self.screen.blit(player_vs_player_button, player_vs_AI_button_rect)
        else:
            self.screen.blit(player_vs_AI_button, player_vs_AI_button_rect)
        self.screen.blit(levels_text_surface, levels_text_rect)
        self.screen.blit(pieces_text_surface, pieces_text_rect)
        self.screen.blit(MODE_text_surface, MODE_text_rect)
        self.screen.blit(settings_text_surface, settings_text_rect)
    def game_page(self):
        self.screen.blit(game_background, (0, 0))
        draw_board(
            self.screen,
            self.game.board,
            self.game.player_piece,
            self.game.computer_piece,
        )
        if self.game.player == 1:
            draw_moving_piece(
                self.screen, self.game.player_piece, self.mouse_x_pos, 10)
        if self.game.player == 2 and self.game_mode == "player_vs_player":
            draw_moving_piece(
                self.screen, self.game.computer_piece, self.mouse_x_pos, 10)

        self.screen.blit(explain_button, explain_button_rect)

        self.screen.blit(hint_button, hint_button_rect)
