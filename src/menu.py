import pygame
from src.button import *
from pathlib import Path
from src.assets_management import blit_rect, blit_display, blit_arrow, play_sound
from src.game import game



# Menu
def menu(window_surface,custom_fonts_tuple,clock):

    # Music
    play_sound("game_music", looping=True)

    
    #----------#
    # Variables
    #----------#
    difficulty_index = 0
    
    while True:
        blit_display(window_surface, window_surface, menu_background, disp= True)
        mouse_pos = pygame.mouse.get_pos()
        ##Score
        # Button Play
        play_image = (button_background_hover if play_button.collidepoint(mouse_pos)else button_background)
        blit_rect(window_surface, play_button,play_image, rect= True)
        draw_text("PLAY", 36, WHITE, play_button.center, window_surface,custom_fonts_tuple[0]) 

        # Button Options
        options_image = (button_background_hover if options_button.collidepoint(mouse_pos)else button_background)
        blit_rect(window_surface,options_button,options_image, rect= True)
        draw_text("OPTIONS", 36, WHITE, options_button.center, window_surface,custom_fonts_tuple[0])

        # Button Exit
        exit_img =  (button_background_hover if exit_button.collidepoint(mouse_pos)else button_background)
        blit_rect(window_surface,exit_button,exit_img, rect= True)
        draw_text("EXIT", 36, WHITE, exit_button.center, window_surface,custom_fonts_tuple[0])

        # Difficulty button and swap
        blit_rect(window_surface, difficulty_button, button_background_hover, rect= True)
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
                    play_sound("button_clicked")
                    game(window_surface, custom_fonts_tuple, clock)
                # Options Button
                elif options_button.collidepoint(event.pos):
                    play_sound("button_clicked")
                    pass
                elif difficulty_button.collidepoint(event.pos):
                    play_sound("button_clicked")
                    pass
                    
                # Left Arrow
                elif left_arrow_rect.collidepoint(event.pos):
                    play_sound("button_clicked")
                    difficulty_index -= 1
                    if difficulty_index < 0:
                        difficulty_index = len(difficulties) - 1

                # Right Arrow
                elif right_arrow_rect.collidepoint(event.pos):
                    play_sound("button_clicked")
                    difficulty_index += 1
                    if difficulty_index >= len(difficulties):
                        difficulty_index = 0
                        

                # Exit
                elif exit_button.collidepoint(event.pos):
                    play_sound("button_clicked")
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    return None
        clock.tick(60)
        pygame.display.update()