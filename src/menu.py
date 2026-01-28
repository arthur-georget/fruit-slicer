import pygame

from pathlib import Path
from src.assets_management import load_image
from src.game import *

#---------------
# CONSTANTS
#---------------

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

#------------#
# DIFFICULTY
#------------#

difficulties = [
    "EASY",
    "MEDIUM",
    "HARD",
    "G0D LIK3"]

difficulty_color = [
    GREEN,     # easy = green
    YELLOW,   # medium = yellow
    PURPLE,   # hard = purple
    RED,   # god_like = red
]

# Button size
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70

#popup_img = load_image("modules/graphic/assets/score_background.png").convert_alpha()
#popup_rect = popup_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def draw_text(text, size, color, center, window_surface,custom_font):
    #Draw text with color size and window_surface#
    text_surface = custom_font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window_surface.blit(text_surface, text_rect)


# Needed to draw score box
def draw_button_pic(x, y, width, height, image, window):
    """Draw Button size, position and screen"""
    rect = pygame.Rect(x, y, width, height)
    image = pygame.transform.scale(image, (width, height))
    window.blit(image, rect)
    return rect

# Menu
def menu(window_surface,custom_fonts_tuple,clock):

    #----------#
    # Variables
    #----------#
    # Arrow Difficulty
    arrow_left_png = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "arrow_left.png").convert_alpha()
    arrow_right_png = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "arrow_right.png").convert_alpha()
    arrow_left_png = pygame.transform.scale(arrow_left_png, (60, 60))
    arrow_right_png = pygame.transform.scale(arrow_right_png, (60, 60))

    ## Background
    menu_background = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "menu_background.png").convert()
    menu_background = pygame.transform.scale(menu_background,(1300, 731))
    running = True
    difficulty_index = 0
    #Load
    arrow_left_png = load_image( "arrow_left")
    arrow_right_png = load_image( "arrow_right")
    menu_background = load_image( "menu_background")
    button_background = load_image( "button_background_hover")
    button_background_hover = load_image( "button_background_hover_2")
    score_background = load_image("scores_board")
    

    # Play button
    play_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 110),(BUTTON_WIDTH,BUTTON_HEIGHT))

    # Options button
    options_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 280),(BUTTON_WIDTH,BUTTON_HEIGHT)) 
    
    # Exit button
    exit_button = pygame.Rect((center_x - (BUTTON_WIDTH/2)+ BUTTON_WIDTH + 390, center_y + 280),(BUTTON_WIDTH / 3,BUTTON_HEIGHT))
    
    # Difficulty rect
    difficulty_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 200),(BUTTON_WIDTH,BUTTON_HEIGHT))

    # Score Test
    #current_score = 40 
    your_score_center = (180, 200)
    top_scores_centers = [
        (110, 275),  
        (110, 320),  
        (110, 365),  
    ]
    top_scores = ["1. 3000", "2. 2750", "3. 2600"]
    #draw_text(f"Your Score : {current_score}", 28, WHITE, score.center, window_surface,custom_fonts_tuple[0])

    #-------------------------------------------------------------------------------------------------------------------------------#
    # 
    #                                                        IN/OUT
    #
    #-------------------------------------------------------------------------------------------------------------------------------#




    while running:
        #window_surface.blit(menu_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play Button
                if play_button.collidepoint(event.pos):
                    game(window_surface, clock)
                # Options Button
                elif options_button.collidepoint(event.pos):
                    pass
                    
                # Left Arrow
                elif left_arrow_rect.collidepoint(event.pos):
                    difficulty_index -= 1
                    if difficulty_index < 0:
                        difficulty_index = len(difficulties) - 1

                # Right Arrow
                elif right_arrow_rect.collidepoint(event.pos):
                    difficulty_index += 1
                    if difficulty_index >= len(difficulties):
                        difficulty_index = 0
                        

                # Exit
                elif exit_button.collidepoint(event.pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return None
        
        mouse_pos = pygame.mouse.get_pos()

        # Button Play
        play_image = (button_background_hover_scale if play_button.collidepoint(mouse_pos)else button_background_scale)
        window_surface.blit(play_image,play_button)
        draw_text("PLAY", 36, WHITE, play_button.center, window_surface,custom_fonts_tuple[0]) 

        # Button Options
        options_image = (button_background_hover_scale if options_button.collidepoint(mouse_pos)else button_background_scale)
        window_surface.blit(options_image, options_button)
        draw_text("OPTIONS", 36, WHITE, options_button.center, window_surface,custom_fonts_tuple[0])

        # Button Exit
        exit_img =  (button_background_hover_scale_exit if exit_button.collidepoint(mouse_pos)else button_background_scale_exit)
        window_surface.blit(exit_img, exit_button)
        draw_text("EXIT", 36, WHITE, exit_button.center, window_surface,custom_fonts_tuple[0])

        # Difficulty swap
        window_surface.blit(button_background_scale, difficulty_button)
        draw_text(difficulties[difficulty_index],36, difficulty_color[difficulty_index], difficulty_button.center, window_surface,custom_fonts_tuple[0])
        # Arrow blit
        window_surface.blit(arrow_left_png, left_arrow_rect)
        window_surface.blit(arrow_right_png, right_arrow_rect)
        
        # Score
        draw_button_pic(10, 10, 341, 512, score_background, window_surface)
        draw_text("Votre score : 1250", 36, (255, 255, 255), your_score_center, window_surface, custom_fonts_tuple[0])
        for score_text, center in zip(top_scores, top_scores_centers):
            draw_text(score_text, 32, (255, 255, 255), center, window_surface, custom_fonts_tuple[0])

        clock.tick(60)
        pygame.display.update()
