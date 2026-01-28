

import pygame
from src.game_function import *

# Main program


def game(window_surface, clock):


    is_running = True

    # Variables
    letters = []
    spawn_timer = 0.0
    lives = LIFE_MAX
    score = 0
    combo = 0
    frozen = False
    freeze_timer = 0.0
    combo_timer = 0.0
    game_timer = 0.0
    timmer_running = True


    print("\n \n --- Fruit Slicer TEST TERMINAL  ---\n \n")

    

    while is_running:

        # Frame
        delta = clock.tick(FPS) / 1000
        if not frozen:
            spawn_timer += delta

        # Timer
        if timmer_running:
            game_timer += delta
            return game_timer
        
        


        # Combo
        combo_timer -= delta
        if combo_timer < 0:
            combo_timer = 0
        combo_valid = combo_timer > 0

        # Freeze
        freeze_timer -= delta 
        if freeze_timer < 0:
            freeze_timer = 0
        frozen = freeze_timer > 0
        if frozen:
            print(f"FROZEN") # debug en stand by

        # Spawn Letters
        spawn_delay = SPAW_INIT / SPEED_RATIO
        if spawn_timer >= spawn_delay:
            spawn_timer = spawn_letter(letters)

        # Lives 
        lost_life, combo = update_letters(letters, delta, combo, frozen)
        lives -= lost_life


        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:
                key = event.unicode.upper()
                score_add, combo, icecube_hit, bomb_hit = slice_element(letters, key, combo, combo_valid)
                score += score_add
                if icecube_hit:
                    freeze_timer = FREEZE_DURATION
                    print("Glacon touché") # debug en stand by
                elif bomb_hit:
                    lives = lost_life * 3
                    print("\n BOOOOOOOM !") # debug en stand by
                if score_add > 0:
                    combo_timer = 1.0 # timer combo ( 1seconde atm )

        # Stand by test terminal --- A SUPPRIMER PAR LA SUITE ---
        print(f"\rLettres: {[l['char'] for l in letters]} | Score: {score} | Vies: {lives}", end="")

        # Lose
        if lives <= 0:
            print("\n Perdu !")
            is_running = False


        

        
        pygame.display.update()
    pygame.quit()
