import pygame
from src.assets_management import *
from src.game import game
from src.menu import menu

# Variables

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption('Fruits Slicer')
    window_surface = pygame.display.set_mode((1300, 731))

    background = pygame.Surface((1300, 731))
    blit_image(window_surface, "menu_background", 0,0,centered=False)

    clock = pygame.time.Clock()

    main_fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)
    menu(window_surface,main_fonts,clock)