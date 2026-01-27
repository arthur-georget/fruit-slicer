import pygame
from pathlib import Path

#---------------
# CONSTANTS
#---------------

# window_surface Size
HEIGHT = 562
WIDTH = 1000  
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

#background_score = pygame.image.load("modules/graphic/assets/background_score.png").convert_alpha()
#background_button = pygame.image.load("modules/graphic/assets/background_button.png").convert_alpha()
#popup_img = pygame.image.load("modules/graphic/assets/background_score.png").convert_alpha()
#popup_rect = popup_img.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def draw_text(text, size, color, center, window_surface,SMALL_FONT):
    #Draw text with color size and window_surface#
    text_surface = SMALL_FONT.render(text, True, color)
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
def menu(window_surface,SMALL_FONT,clock):

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
    menu_background = pygame.transform.scale(menu_background,(1000, 562))
    running = True
    difficulty_index = 0
    draw_text(difficulties[difficulty_index],40,BLACK,(center_x, center_y + 145),window_surface,SMALL_FONT)
    #confirm_button = pygame.Rect(center_x, center_y)
    # Arrow rect
    left_arrow_rect = arrow_left_png.get_rect()
    right_arrow_rect = arrow_right_png.get_rect()
    left_arrow_rect.topleft = (center_x - ((BUTTON_WIDTH/2)+50), center_y + 48)
    right_arrow_rect.topleft = (center_x + ((BUTTON_WIDTH/2)) - 12, center_y + 48)


    while running:
        window_surface.blit(menu_background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Play Button
                if button_difficulty.collidepoint(event.pos):
                    pass
                # Options Button
                #elif options_button.collidepoint(event.pos):
                #    pass
                    
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



        button_difficulty = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 120),(BUTTON_WIDTH,BUTTON_HEIGHT))

        
        #TEST
        pygame.draw.rect(window_surface, BLUE, button_difficulty,width=0, border_radius=20)
        mouse_pos = pygame.mouse.get_pos()
        play_image = (RED if button_difficulty.collidepoint(mouse_pos)else RED)

        # -- Buttons Play / Diffuculty / Word / Exit --

        button_background = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "button_background_hover.png").convert_alpha()
        button_background_hover = pygame.image.load(Path(__file__).parent.parent / "assets" / "images" / "button_background_hover_2.png").convert_alpha()
        button_background_scale = pygame.transform.scale(button_background, (BUTTON_WIDTH, BUTTON_HEIGHT))
        button_background_hover_scale = pygame.transform.scale(button_background_hover, (BUTTON_WIDTH, BUTTON_HEIGHT))
        
        
        
        # Play button
        play_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y -40),(BUTTON_WIDTH,BUTTON_HEIGHT))
        play_image = (button_background_hover_scale if play_button.collidepoint(mouse_pos)else button_background_scale)
        window_surface.blit(play_image,play_button)
        draw_text("PLAY", 36, WHITE, play_button.center, window_surface,SMALL_FONT) 
        

        # Options button
        options_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 120),(BUTTON_WIDTH,BUTTON_HEIGHT))
        options_image = (button_background_hover_scale if options_button.collidepoint(mouse_pos)else button_background_scale)
        window_surface.blit(options_image, options_button)
        draw_text("OPTIONS", 36, WHITE, options_button.center, window_surface,SMALL_FONT) 
        
        
        
        # Exit button
        exit_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 200),(BUTTON_WIDTH,BUTTON_HEIGHT))
        mouse_pos = pygame.mouse.get_pos()
        exit_img =  (button_background_hover_scale if exit_button.collidepoint(mouse_pos)else button_background_scale)
        window_surface.blit(exit_img, exit_button)
        draw_text("EXIT", 36, WHITE, exit_button.center, window_surface,SMALL_FONT)

        # Arrow blit
        window_surface.blit(arrow_left_png, left_arrow_rect)
        window_surface.blit(arrow_right_png, right_arrow_rect)

        # Difficulty rect
        difficulty_button = pygame.Rect((center_x - (BUTTON_WIDTH/2), center_y + 40),(BUTTON_WIDTH,BUTTON_HEIGHT))

        # Difficulty swap
        window_surface.blit(button_background_scale, difficulty_button)
        draw_text(difficulties[difficulty_index],36, difficulty_color[difficulty_index], difficulty_button.center, window_surface,SMALL_FONT)
        
        # Score Rectangle
        #current_score = 40
        #score = draw_button_pic(40, 40, 300, 100, background_score, window_surface) 
        #draw_text(f"Your Score : {current_score}", 28, WHITE, score.center, window_surface)

        clock.tick(60)
        pygame.display.update()
    pygame.exit()
