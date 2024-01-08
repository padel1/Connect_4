import pygame

screen_w = 800
screen_h = 600

pygame.init()
pygame.font.init()

FPS = 60


class Page:
    menu = "menu"
    option = "option"
    game = "game"


menu_background = pygame.image.load(
    r"assets\img\bgcbon.jpg")
option_background = pygame.image.load(r"assets/img/menu_background.jpg")
menu_background = pygame.transform.scale(menu_background, (800, 600))
option_background = pygame.transform.scale(option_background, (800, 600))


# Blit menu_background onto the transparent surface (with the drop shadow)

logo = pygame.image.load("assets/img/logo.png")
logo = pygame.transform.scale(logo, (350, 140))

# menu objects (like logo, buttons, ...)
button_font = pygame.font.SysFont("comicsanse", 25)


start_surface = pygame.image.load("assets/img/startButton.png")
start_hover_surface = pygame.image.load("assets/img/startButton(hover).png")

# white piece button for menu


wp_surface = pygame.image.load("assets/img/menu white piece.png")
wp_surface = pygame.transform.smoothscale(wp_surface, (50, 50))

wp_surface_rect = wp_surface.get_rect(
    topleft=(screen_w // 2 - wp_surface.get_width(), screen_h // 2)
)


wp_clicked_surface = pygame.image.load(
    "assets/img/menu white piece(clicked).png")
wp_clicked_surface = pygame.transform.smoothscale(wp_clicked_surface, (50, 50))

# black piece button for menu
bp_surface = pygame.image.load("assets/img/menu black piece.png")
bp_surface = pygame.transform.smoothscale(bp_surface, (50, 50))
bp_clicked_surface = pygame.image.load(
    "assets/img/menu black piece(clicked).png")
bp_clicked_surface = pygame.transform.smoothscale(bp_clicked_surface, (50, 50))
bp_surface_rect = wp_surface.get_rect(
    topleft=(screen_w // 2 + bp_surface.get_width() // 2, screen_h // 2)
)


game_background = pygame.image.load("assets/img/connect four board 2.png")
game_background = pygame.transform.scale(game_background, (800, 750))

start_button = pygame.image.load("assets\img\start_btn.png")
start_button = pygame.transform.scale(start_button, (250, 70))


start_button_shadow = pygame.image.load("assets\img\hover_start_btn.png")
start_button_shadow = pygame.transform.scale(start_button_shadow, (250, 70))


play_btn = pygame.image.load("assets\img\play_btn.png")
play_btn = pygame.transform.scale(play_btn, (200, 200))

play_btn_hovered = pygame.image.load("assets\img\play_hovered.png")
play_btn_hovered = pygame.transform.scale(play_btn_hovered, (200, 200))


start_button_rect = play_btn.get_rect(
    topleft=(screen_w // 2, screen_h//2 - 100)
)

option_button = pygame.image.load(r"assets\img\settings.png")
option_button = pygame.transform.scale(option_button, (60, 60))

help_button = pygame.image.load(r"assets\img\help.png")
help_button = pygame.transform.scale(help_button, (50, 50))
# option_button_shadow = pygame.image.load(r"assets\img\hover_option_btn.png")
# option_button_shadow = pygame.transform.scale(option_button_shadow, (250, 70))


option_button_rect = option_button.get_rect(
    topleft=(screen_w // 2-60, screen_h//2 - 60)
)
help_button_rect = help_button.get_rect(
    topleft=(screen_w // 2-55, screen_h//2+10)
)


player_vs_AI_button = pygame.transform.scale(
    pygame.image.load("assets\img\pvi.png"), (100, 100))
player_vs_player_button = pygame.transform.scale(
    pygame.image.load("assets\img\pvp.png"), (100, 100))
player_vs_AI_button_rect = player_vs_AI_button.get_rect(
    center=(screen_w / 2, 425))
# player_vs_player_button_rect = player_vs_AI_button.get_rect(center=(screen_w /2, 425))

easy_btn = pygame.image.load(r"assets\img\easy.png")
easy_btn = pygame.transform.scale(easy_btn, (200, 60))

med_btn = pygame.image.load(r"assets\img\medium.png")
med_btn = pygame.transform.scale(med_btn, (200, 60))

hard_btn = pygame.image.load(r"assets\img\hard.png")
hard_btn = pygame.transform.scale(hard_btn, (200, 60))

diff_arr = [easy_btn, med_btn, hard_btn]

diff_btn_rect = option_button.get_rect(
    topleft=(screen_w // 2 - hard_btn.get_width() // 2, 200)
)

explain_button = pygame.transform.scale(
    pygame.image.load("assets/img/explanation.png"), (50, 50))
hint_button = pygame.transform.scale(
    pygame.image.load("assets\img\hint_btn.png"), (50, 50))
explain_button_rect = explain_button.get_rect(topleft=(screen_w - 60, 10))
hint_button_rect = hint_button.get_rect(topleft=(screen_w - 60, 80))
