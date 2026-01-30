from pygame import mouse, display, MOUSEBUTTONDOWN, QUIT, event
from src.button_functions import *
from src.constants import WHITE, menu_background, button_background, button_background_hover, arrow_left_png, arrow_right_png
from src.assets_management import blit_rect, blit_display, draw_fruity_slider
from src.settings import save_settings, load_settings
from src.translation import load_translation
from src.constants import left_arrow_rect, right_arrow_rect, difficulties
from src.options_button import *

def options_menu(window_surface, custom_fonts_tuple, clock):
    settings = load_settings()
    T = load_translation()

    languages = ["FR", "EN", "ES"]
    language_index = languages.index(settings["language"])

    

    while True:
        blit_display(window_surface, window_surface, menu_background, disp=True)
        mouse_pos = mouse.get_pos()

        # Title
        draw_text(T["options"], 48, WHITE,
                  (window_surface.get_width()//2, 150),
                  window_surface, custom_fonts_tuple[0])

        # Language selector
        blit_rect(window_surface, language_button, button_background_hover, rect=True)
        draw_text(f"{T['language']} : {languages[language_index]}", 36, WHITE,
                  language_button.center, window_surface, custom_fonts_tuple[0])

        window_surface.blit(arrow_left_png, left_arrow_lang)
        window_surface.blit(arrow_right_png, right_arrow_lang)

        # Music toggle
        blit_rect(window_surface, music_toggle_button, button_background_hover, rect=True)
        music_state = "ON" if settings["music_enabled"] else "OFF"
        draw_text(f"Musique : {music_state}", 32, WHITE,
                  music_toggle_button.center, window_surface, custom_fonts_tuple[0])

        # SFX toggle
        blit_rect(window_surface, sfx_toggle_button, button_background_hover, rect=True)
        sfx_state = "ON" if settings["sfx_enabled"] else "OFF"
        draw_text(f"Sons : {sfx_state}", 32, WHITE,
                  sfx_toggle_button.center, window_surface, custom_fonts_tuple[0])

        # Sliders fruités
        draw_text("Volume Musique", 28, WHITE, (300, 510),
                  window_surface, custom_fonts_tuple[0])
        draw_fruity_slider(window_surface, music_slider, settings["music_volume"])

        draw_text("Volume Effets", 28, WHITE, (300, 570),
                  window_surface, custom_fonts_tuple[0])
        draw_fruity_slider(window_surface, sfx_slider, settings["sfx_volume"])

        # Back button
        back_img = button_background_hover if back_button.collidepoint(mouse_pos) else button_background
        blit_rect(window_surface, back_button, back_img, rect=True)
        draw_text(T["back"], 36, WHITE, back_button.center, window_surface, custom_fonts_tuple[0])

        # Events
        for events in event.get():
            if events.type == QUIT:
                return None

            if events.type == MOUSEBUTTONDOWN:

                # Back
                if back_button.collidepoint(events.pos):
                    save_settings(settings)
                    return

                # Change language
                # Left Arrow
                elif left_arrow_rect.collidepoint(events.pos):
                    language_index -= 1
                    if language_index < 0:
                        language_index = len(difficulties) - 1

                # Right Arrow
                elif right_arrow_rect.collidepoint(events.pos):
                    language_index += 1
                    if language_index >= len(difficulties):
                        language_index = 0
                

                # Toggle music
                if music_toggle_button.collidepoint(events.pos):
                    settings["music_enabled"] = not settings["music_enabled"]
                    save_settings(settings)

                # Toggle SFX
                if sfx_toggle_button.collidepoint(events.pos):
                    settings["sfx_enabled"] = not settings["sfx_enabled"]
                    save_settings(settings)

                # Music slider
                if music_slider.collidepoint(events.pos):
                    rel_x = events.pos[0] - music_slider.x
                    settings["music_volume"] = max(0, min(1, rel_x / music_slider.width))
                    save_settings(settings)

                # SFX slider
                if sfx_slider.collidepoint(events.pos):
                    rel_x = events.pos[0] - sfx_slider.x
                    settings["sfx_volume"] = max(0, min(1, rel_x / sfx_slider.width))
                    save_settings(settings)

        display.update()
        clock.tick(60)
