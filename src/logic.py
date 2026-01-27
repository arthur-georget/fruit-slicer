

import pygame 
import os
import random
from logic_constant import *
from logic_function import *


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# FONT_PATH = os.path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")


# Main program

if __name__ == "__main__":

    pygame.init()
    pygame.display.set_caption('Fruit Slicer')
    window_surface = pygame.display.set_mode((800, 600))

    background = pygame.Surface((800, 600))
    background.fill(pygame.Color('#000000'))

    # main_font = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

    clock = pygame.time.Clock()
    is_running = True



    print("\n \n --- Fruit Slicer TEST TERMINAL  ---\n \n")

    while is_running:
        # BG
        window_surface.blit(background, (0, 0))

        # Frame
        delta = clock.tick(FPS) / 1000
        spawn_timer += delta

        # Spawn Letters
        spawn_delay = SPAW_INIT / SPEED_RATIO
        if spawn_timer >= spawn_delay:
            spawn_timer = spawn_letter(letters)

        # Lives 
        lives -= update_letters(letters, delta)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:
                key = event.unicode.upper()
                score += key_input(letters, key)

        # Stand by test terminal --- A SUPPRIMER PAR LA SUITE ---
        print(f"\rLettres: {[l['char'] for l in letters]} | Score: {score} | Vies: {lives}", end="")
        

        # Lose
        if lives <= 0:
            print("\n Perdu !")
            is_running = False


        
        pygame.display.update()
    pygame.quit()
