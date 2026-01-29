

import pygame
from src.game_function import *
from src.assets_management import *



# window_surface Size
HEIGHT = 731
WIDTH = 1300  

#Center window_surface
center_x = WIDTH // 2
center_y = HEIGHT // 2

#-------#
# MUSIC
#-------#
#pygame.mixer.music.load()
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(-1)

#-------#
# COLORS
#-------#
#Remove or change file after test
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
BLUE = (50, 100, 200)
LIGHT_BLUE = (0, 123, 255, 255)
RED = (180, 30, 30)
LIGHT_RED = (255, 0, 46, 255)
GREEN = (0, 255, 78)
DARK_GREEN = (0, 185, 78, 255)
YELLOW = (255, 255, 0, 255)
PURPLE = (200, 50, 50)

# Button size
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70



# Main program
def game(window_surface, custom_fonts_tuple, clock):

    
    #-----------------
    # Variables
    #-----------------

    pause = False
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
    game_background_image = load_image("game_background")

    print("\n \n --- Fruit Slicer TEST TERMINAL  ---\n \n")


    is_running = True

    #-----------------a
    # LOOP GAME
    #-----------------

    while is_running:
        
        window_surface.blit(game_background_image, (0,0))
        # Frame
        delta = clock.tick(FPS) / 1000
        if not frozen:
            spawn_timer += delta

        # Timer
        if timmer_running:
            game_timer += delta

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

            # Pause
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result = game_pause(window_surface, custom_fonts_tuple[0])
                    
                    if result == 0:
                        pass
                    elif result == 1:
                        return

            # Game
            elif event.type == pygame.KEYDOWN and not pause:
                key = event.unicode.upper()
                score_add, combo, icecube_hit, bomb_hit = slice_element(letters, key, combo,combo_valid)
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
