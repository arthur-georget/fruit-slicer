import pygame 
import os
from src.game import game
from src.menu import menu

# Variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_PATH = os.path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.display.set_caption('Fruit Slicer')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    main_font = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

    clock = pygame.time.Clock()


    is_running = True

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        window_surface.blit(background, (0, 0))

        # menu(window_surface,main_font,clock)
        game(window_surface, clock)

        pygame.display.update()
    pygame.quit()