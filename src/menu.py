from pygame import mouse, event, display, QUIT, MOUSEBUTTONDOWN, SYSTEM_CURSOR_HAND
from src.button_functions import draw_text, draw_button_pic
from src.assets_management import blit_rect, blit_display, blit_arrow, play_sound
from src.data_management import *
from src.game import game
from src.options import options_menu
from src.constants import WHITE, arrow_left_png, arrow_right_png, menu_background, button_background, button_background_hover, score_background
from src.menu_button import *
#-------#
# MUSIC
#-------#
#pygame.mixer.music.load()
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play(-1)

# Menu
def menu(window_surface,custom_fonts_tuple,clock):

    # Music
    play_sound("game_music", looping=True)

    
    #----------#
    # Variables
    #----------#
    difficulty_index = get_json_data(SETTINGS_PATH)["difficulty"]
    
    while True:
        blit_display(window_surface, window_surface, menu_background, disp= True)
        mouse_pos = mouse.get_pos()
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

        for events in event.get():
            if events.type == QUIT:
                return None
            if events.type == MOUSEBUTTONDOWN:

                set_json_data(SETTINGS_PATH,"difficulty",difficulty_index)

                # Play Button
                if play_button.collidepoint(events.pos):
                    play_sound("button_clicked")
                    game(window_surface, custom_fonts_tuple, clock)
                # Options Button
                elif options_button.collidepoint(events.pos):
                    play_sound("button_clicked")
                    options_menu(window_surface, custom_fonts_tuple, clock)
                elif difficulty_button.collidepoint(events.pos):
                    play_sound("button_clicked")
                    pass
                    
                # Left Arrow
                elif left_arrow_rect.collidepoint(events.pos):
                    play_sound("button_clicked")
                    difficulty_index -= 1
                    if difficulty_index < 0:
                        difficulty_index = len(difficulties) - 1

                # Right Arrow
                elif right_arrow_rect.collidepoint(events.pos):
                    play_sound("button_clicked")
                    difficulty_index += 1
                    if difficulty_index >= len(difficulties):
                        difficulty_index = 0
                        

                # Exit
                elif exit_button.collidepoint(events.pos):
                    play_sound("button_clicked")
                    mouse.set_cursor(SYSTEM_CURSOR_HAND)
                    return None
        clock.tick(60)
        display.update()