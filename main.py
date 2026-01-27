import pygame
from src.assets_management import *
from src.menu import menu

# Variables

# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()

    pygame.display.set_caption('Fruits Slicer')
    window_surface = pygame.display.set_mode((1000, 562))

    background = pygame.Surface((1000, 562))
    background.fill(pygame.Color('#000000'))
    blit_image(window_surface, "menu_background", 0,0,centered=False)

    clock = pygame.time.Clock()

    main_fonts = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)
    hello_text = main_fonts[0].render("Hello, Pygame!", True, (255, 255, 255))

    is_running = True

    while is_running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        #menu(window_surface,main_font,clock)

        pygame.display.update()
    pygame.exit()