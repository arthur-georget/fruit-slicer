import pygame
from src.button import *
from pathlib import Path
from src.assets_management import load_image, blit_image

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
RED = (180, 30, 30)
GREEN = (0, 255, 78)
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
    GREEN,     # easy
    YELLOW,   # medium
    PURPLE,   # hard 
    RED,   # god_like
]

# Menu
def menu(window_surface,custom_fonts_tuple,clock):

    #----------#
    # Variables
    #----------#
    difficulty_index = 0
    
    while True:
        window_surface.blit(menu_background, (0, 0))
        mouse_pos = pygame.mouse.get_pos()
        ##Score
        # Button Play
        play_image = (button_background_hover if play_button.collidepoint(mouse_pos)else button_background)
        blit_image(window_surface, play_button,play_image, fill= True)
        draw_text("PLAY", 36, WHITE, play_button.center, window_surface,custom_fonts_tuple[0]) 

        # Button Options
        options_image = (button_background_hover if options_button.collidepoint(mouse_pos)else button_background)
        blit_image(window_surface,options_button,options_image, fill = True)
        draw_text("OPTIONS", 36, WHITE, options_button.center, window_surface,custom_fonts_tuple[0])

        # Button Exit
        exit_img =  (button_background_hover_scale_exit if exit_button.collidepoint(mouse_pos)else button_background_scale_exit)
        window_surface.blit(exit_img, exit_button)
        draw_text("EXIT", 36, WHITE, exit_button.center, window_surface,custom_fonts_tuple[0])

        # Difficulty swap
        blit_image(window_surface, difficulty_button, button_background_hover, fill= True)
        draw_text(difficulties[difficulty_index],36, difficulty_color[difficulty_index], difficulty_button.center, window_surface,custom_fonts_tuple[0])
        # Arrow blit
        window_surface.blit(arrow_left_png, left_arrow_rect)
        window_surface.blit(arrow_right_png, right_arrow_rect)
        
        # Score
        draw_button_pic(10, 10, 341, 512, score_background, window_surface)
        draw_text("Votre score : 1250", 36, (255, 255, 255), your_score_center, window_surface, custom_fonts_tuple[0])
        for score_text, center in zip(top_scores, top_scores_centers):
            draw_text(score_text, 32, (255, 255, 255), center, window_surface, custom_fonts_tuple[0])

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
        clock.tick(60)
        pygame.display.update()