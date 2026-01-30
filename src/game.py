import pygame
from src.game_function import *
from src.assets_management import *



def game(window_surface, custom_fonts_tuple, clock):

    

    elements = []
    assigned_chars = ""
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

    is_running = True

    while is_running:
        
        ################################## RENDERING ######################################

        window_surface.blit(game_background_image, (0,0))

        # Blit elements in screen
        for element in elements:
            char_to_blit = custom_fonts_tuple[0].render(element["char"], True, (255,255,255))
            char_shadow_to_blit = custom_fonts_tuple[0].render(element["char"], True, (55,55,55))
            if frozen:
                element_image = transform.scale(images[element["image_name"]]["iced"], (100, 100))
                element_rect = element_image.get_rect()
                element_rect.center = (element["x_pos"], element["y_pos"])
            else:
                element["velocity"].y += .05
                element_image = transform.scale(images[element["image_name"]]["normal"], (100, 100))
                element_rect = element_image.get_rect()
                element_rect.center = (element["x_pos"], element["y_pos"])
                element_rect.center += element["velocity"]
                element["x_pos"] += element["velocity"].x
                element["y_pos"] += element["velocity"].y

            window_surface.blit(element_image,element_rect)
            window_surface.blit(char_shadow_to_blit,(element["x_pos"]+52,element["y_pos"]+2))
            window_surface.blit(char_to_blit,(element["x_pos"]+50,element["y_pos"]))
            
        
        score_to_blit = custom_fonts_tuple[0].render(f"Score: {score}", True, (255,255,255))
        score_shadow_to_blit = custom_fonts_tuple[0].render(f"Score: {score}", True, (55,55,55))
        lives_to_blit = custom_fonts_tuple[0].render(f"Vies: {lives}", True, (255,255,255))
        lives_shadow_to_blit = custom_fonts_tuple[0].render(f"Vies: {lives}", True, (55,55,55))
        window_surface.blit(score_shadow_to_blit,(1152,102))
        window_surface.blit(score_to_blit,(1150,100))
        window_surface.blit(lives_shadow_to_blit,(1152,200))
        window_surface.blit(lives_to_blit,(1150,200))
        

        ################################## LOGIC ######################################

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
        spawn_delay =  SPAWN_INIT / (SPEED_RATIO * random.randrange(1,20,1)/10)
        if spawn_timer >= spawn_delay:
            spawn_timer, assigned_chars = spawn_element(elements,assigned_chars)
        
        # Lives 
        life_lost, combo, assigned_chars = update_elements(elements, assigned_chars, combo)
        lives -= life_lost

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            # Pause
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    result = game_pause(window_surface, custom_fonts_tuple)
                    
                    if result == 0:
                        pass
                    elif result == 1:
                        return

                # Game
                else:
                    key = event.unicode.upper()
                    score_add, combo, icecube_hit, bomb_hit, assigned_chars = slice_element(elements, assigned_chars, key, combo, combo_valid)
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
            print("\n Game Over !")
            play_again = game_over_popup(window_surface, custom_fonts_tuple)
            if play_again:
                elements = []
                assigned_chars = ""
                spawn_timer = 0.0
                lives = LIFE_MAX
                score = 0
                combo = 0
                frozen = False
                freeze_timer = 0.0
                combo_timer = 0.0
                game_timer = 0.0
                timmer_running = True
            else:
                is_running = False

        pygame.display.update()
pygame.quit()
