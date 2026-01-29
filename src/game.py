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

def draw_text(text, size, color, center, window_surface,custom_font):
    #Draw text with color size and window_surface#
    text_surface = custom_font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window_surface.blit(text_surface, text_rect)

# Main program
def game(window_surface, custom_fonts_tuple, clock):

    
    #-----------------
    # Variables
    #-----------------

    elements = []
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

    images = {
                "apple": {"normal": load_image("apple"), "iced": load_image("iced_apple"), "sliced": load_image("sliced_apple")},
                "banana": {"normal": load_image("banana"), "iced": load_image("iced_banana"), "sliced": load_image("sliced_banana")},
                "kiwi": {"normal": load_image("kiwi"), "iced": load_image("iced_kiwi"), "sliced": load_image("sliced_kiwi")},
                "orange": {"normal": load_image("orange"), "iced": load_image("iced_orange"), "sliced": load_image("sliced_orange")},
                "pineapple": {"normal": load_image("pineapple"), "iced": load_image("iced_pineapple"), "sliced": load_image("sliced_pineapple")},
                "bomb": {"normal": load_image("bomb"), "iced": load_image("iced_bomb"), "sliced": load_image("sliced_bomb")},
                "ice_cube": {"normal": load_image("ice_cube"), "iced": load_image("ice_cube"), "sliced": load_image("sliced_ice_cube")}
            }

    print("\n \n --- Fruit Slicer TEST TERMINAL  ---\n \n")


    is_running = True

    #-----------------
    # LOOP GAME
    #-----------------

    while is_running:
        
        ########### DISPLAY ######################################

        window_surface.blit(game_background_image, (0,0))

        # Blit elements in screen
        for element in elements:
            char_to_blit = custom_fonts_tuple[0].render(element["char"], True, (255,255,255))
            time_left_to_blit = custom_fonts_tuple[0].render(str(int(element["time_left"])), True, (255,255,255))
            if frozen:
                image_to_blit = transform.scale(images[element["image_name"]]["iced"], (100, 100))
            else:
                image_to_blit = transform.scale(images[element["image_name"]]["normal"], (100, 100))
            window_surface.blit(image_to_blit,(element["x_pos"],element["y_pos"]))
            window_surface.blit(char_to_blit,(element["x_pos"],element["y_pos"]))
            window_surface.blit(time_left_to_blit,(element["x_pos"],element["y_pos"]+40))
        
        score_to_blit = custom_fonts_tuple[0].render(f"Score: {score}", True, (255,255,255))
        lives_to_blit = custom_fonts_tuple[0].render(f"Vies: {lives}", True, (255,255,255))
        window_surface.blit(score_to_blit,(0,100))
        window_surface.blit(lives_to_blit,(0,200))

        ############ LOGIC #######################################

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

        # Spawn Fruits, bombs and icecubes
        spawn_delay = SPAW_INIT / SPEED_RATIO
        if spawn_timer >= spawn_delay:
            spawn_timer = spawn_element(elements)
        
        # Lives 
        life_lost, combo = update_elements(elements, delta, combo, frozen)
        lives -= life_lost

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            elif event.type == pygame.KEYDOWN:
                key = event.unicode.upper()
                elements, score_add, combo, icecube_hit, bomb_hit = slice_element(elements, key, combo, combo_valid)
                score += score_add
                if icecube_hit:
                    freeze_timer = FREEZE_DURATION
                    print("Glacon touché")
                elif bomb_hit:
                    lives = life_lost * 3
                    print("\n BOOOOOOOM !")
                if score_add > 0:
                    combo_timer = 1.0

        # Game Over
        if lives <= 0:
            print("\n Perdu !")
            is_running = False

        pygame.display.update()
pygame.quit()
