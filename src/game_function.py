import random
import pygame
from src.assets_management import *

# --- CONSTANT ---

# Keyboard inc
KEYBOARD = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",";",":","!","$"]

# Gameplay
LIFE_MAX = 3
SCORE_ADD = 1

# Time
FPS = 60
TIME_INIT_LETTERS = 5.0
SPAW_INIT = 1.0
SPEED_RATIO = 0.80
MAX_COMBO = 3
FREEZE_DURATION = 10.0

# Color
WHITE = (255, 255, 255)

# Size
WIDTH = 1300
HEIGHT = 731
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# Button load 
PAUSE_BUTTON = load_image("button_background")
PAUSE_BUTTON_HOVER = load_image("button_background_hover_2")
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70

# Font



# Functions
def draw_text(text, size, color, center, window_surface,custom_font):
    #Draw text with color size and window_surface#
    text_surface = custom_font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window_surface.blit(text_surface, text_rect)

def create_letter(element_type):
    return {
    "char" : random.choice(KEYBOARD),
    "time_left" : TIME_INIT_LETTERS,
    "type" : element_type}

def spawn_letter(letters):
    if random.random() > 1.00 :
        letters.append(create_letter("ICECUBE"))
    elif random.random() > 1.00 :
        letters.append(create_letter("BOMB"))
    else: 
        letters.append(create_letter("FRUIT"))
    return 0.0

def update_letters(letters, delta, combo, frozen = False):
    broken_combo = False
    lost_life = 0
    
    # Try list letters
    for letter in letters[:]:
        if frozen == True:
            pass
        else:    
            letter["time_left"] -= delta * SPEED_RATIO

        # Stand by for test
        # print(letter["time_left"]) 

        if letter["time_left"] <= 0:
            letters.remove(letter)
            lost_life += 1
            broken_combo = True

    # Combo borken 
    if broken_combo == True:
        combo = 0
    return lost_life, combo

def slice_element(letters, key, combo, combo_valid):
    combo_hit = False
    icecube_hit = False
    bomb_hit = False
    score = 0
    

    for letter in letters[:]:
        if letter["char"] == key:

            if letter["type"] == "BOMB":
                bomb_hit = True 
            elif letter["type"] == "ICECUBE":
                icecube_hit = True

            letters.remove(letter)

            if combo_valid:
                combo = min(combo + 1, MAX_COMBO)
            else :
                combo = 0
            score = 1 + combo
        break
            
    return score, combo, icecube_hit, bomb_hit

def combo_add_score(score, combo):
    return score * (1 + combo)

def game_pause(window_surface, custom_fonts_tuple):

    while True:
        mouse_pos = pygame.mouse.get_pos()

        overlay = pygame.Surface(window_surface.get_size())
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        window_surface.blit(overlay, (0, 0))


        # Text
        draw_text("PAUSE", 80, WHITE, (CENTER_X, CENTER_Y - 180), window_surface, font)


        # - Buttons -

        # Resume
        resume_button = pygame.Rect(CENTER_X - BUTTON_WIDTH // 2, CENTER_Y - 20,    BUTTON_WIDTH, BUTTON_HEIGHT)
        resum_img = (PAUSE_BUTTON_HOVER if resume_button.collidepoint(mouse_pos) else   PAUSE_BUTTON)
        blit_image(window_surface, resum_img, resume_button.x, resume_button.y, fill=True)
        draw_text("REPRENDRE", 36, WHITE, resume_button.center, window_surface, font)

        # menu
        menu_button = pygame.Rect(CENTER_X - BUTTON_WIDTH // 2, CENTER_Y + 60,  BUTTON_WIDTH, BUTTON_HEIGHT)
        option_img = (PAUSE_BUTTON_HOVER if menu_button.collidepoint(mouse_pos) else    PAUSE_BUTTON)
        blit_image(window_surface, option_img, menu_button.x, menu_button.y, fill=True)
        draw_text("MENU", 36, WHITE, menu_button.center, window_surface, font)


        for event in pygame.event.get():


            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    return 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.collidepoint(event.pos):
                    return 1


        pygame.display.update()

