

import pygame
from src.game_function import *


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# FONT_PATH = os.path.join(BASE_DIR, "assets", "fonts", "LiberationSans-Regular.ttf")


# Main program


def game(window_surface, clock):

    # main_font = pygame.font.Font(FONT_PATH, 30), pygame.font.Font(FONT_PATH, 50)

    is_running = True

    # Variables
    letters = []
    spawn_timer = 0.0
    lives = LIFE_MAX
    score = 0
    combo = 0
    frozen = False


    print("\n \n --- Fruit Slicer TEST TERMINAL  ---\n \n")

    while is_running:

        # Frame
        delta = clock.tick(FPS) / 1000
        spawn_timer += delta

        # Spawn Letters
        spawn_delay = SPAW_INIT / SPEED_RATIO
        if spawn_timer >= spawn_delay:
            spawn_timer = spawn_letter(letters)

        # Lives 
        lost_life, combo = update_letters(letters, delta, combo, frozen=True)
        lives -= lost_life


        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:
                key = event.unicode.upper()
                score_add, combo = slice_element(letters, key, combo)
                score += score_add

        # Stand by test terminal --- A SUPPRIMER PAR LA SUITE ---
        print(f"\rLettres: {[l['char'] for l in letters]} | Score: {score} | Vies: {lives}", end="")
        

        # Lose
        if lives <= 0:
            print("\n Perdu !")
            is_running = False


        
        pygame.display.update()
    pygame.quit()
