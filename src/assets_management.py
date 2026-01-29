from os import path,pardir
from pygame import image,mixer,transform,display

BASE_DIR = path.dirname(path.abspath(__file__))
FONT_PATH = path.join(BASE_DIR, pardir, "assets", "fonts", "LiberationSans-Regular.ttf")
IMAGES_PATH = path.join(BASE_DIR, pardir, "assets", "images")
SOUNDS_PATH = path.join(BASE_DIR, pardir, "assets", "sounds")

images = (  
            {
                "name": "logo",
                "path": path.join(IMAGES_PATH, "logo.png")
            },
            {
                "name": "menu_background",
                "path": path.join(IMAGES_PATH, "menu_background.png")
            },
            {
                "name": "button_background",
                "path": path.join(IMAGES_PATH, "button_background.png")
            },
            {
                "name": "button_background_hover",
                "path": path.join(IMAGES_PATH, "button_background_hover.png")
            },
            {
                "name": "button_background_hover_2",
                "path": path.join(IMAGES_PATH, "button_background_hover_2.png")
            },
            {
                "name": "game_background",
                "path": path.join(IMAGES_PATH, "game_background.png")
            },
            {
                "name": "option_background",
                "path": path.join(IMAGES_PATH, "option_background.png")
            },
            {
                "name": "arrow_left",
                "path": path.join(IMAGES_PATH, "arrow_left.png")
            },
            {
                "name": "arrow_right",
                "path": path.join(IMAGES_PATH, "arrow_right.png")
            },
            {
                "name": "scores_board",
                "path": path.join(IMAGES_PATH, "scores_board.png")
            },
            {
                "name": "apple",
                "path": path.join(IMAGES_PATH, "apple.png")
            },
            {
                "name": "sliced_apple",
                "path": path.join(IMAGES_PATH, "sliced_apple.png")
            },
            {
                "name": "iced_apple",
                "path": path.join(IMAGES_PATH, "iced_apple.png")
            },
            {
                "name": "banana",
                "path": path.join(IMAGES_PATH, "banana.png")
            },
            {
                "name": "sliced_banana",
                "path": path.join(IMAGES_PATH, "sliced_banana.png")
            },
            {
                "name": "iced_banana",
                "path": path.join(IMAGES_PATH, "iced_banana.png")
            },
            {
                "name": "kiwi",
                "path": path.join(IMAGES_PATH, "kiwi.png")
            },
            {
                "name": "sliced_kiwi",
                "path": path.join(IMAGES_PATH, "sliced_kiwi.png")
            },
            {
                "name": "iced_kiwi",
                "path": path.join(IMAGES_PATH, "iced_kiwi.png")
            },
            {
                "name": "orange",
                "path": path.join(IMAGES_PATH, "orange.png")
            },
            {
                "name": "sliced_orange",
                "path": path.join(IMAGES_PATH, "sliced_orange.png")
            },
            {
                "name": "iced_orange",
                "path": path.join(IMAGES_PATH, "iced_orange.png")
            },
            {
                "name": "pineapple",
                "path": path.join(IMAGES_PATH, "pineapple.png")
            },
            {
                "name": "sliced_pineapple",
                "path": path.join(IMAGES_PATH, "sliced_pineapple.png")
            },
            {
                "name": "iced_pineapple",
                "path": path.join(IMAGES_PATH, "iced_pineapple.png")
            },
            {
                "name": "ice_cube",
                "path": path.join(IMAGES_PATH, "ice_cube.png")
            },
            {
                "name": "sliced_ice_cube",
                "path": path.join(IMAGES_PATH, "sliced_ice_cube.png")
            },
            {
                "name": "bomb",
                "path": path.join(IMAGES_PATH, "bomb.png")
            },
            {
                "name": "iced_bomb",
                "path": path.join(IMAGES_PATH, "iced_bomb.png")
            },
            {
                "name": "sliced_bomb",
                "path": path.join(IMAGES_PATH, "sliced_bomb.png")
            }
         )

sounds = (
            {
                "name": "menu_music",
                "path": path.join(SOUNDS_PATH, "menu_music.wav")
            },
            {
                "name": "game_music",
                "path": path.join(SOUNDS_PATH, "game_music.wav")
            },
            {
                "name": "button_clicked",
                "path": path.join(SOUNDS_PATH, "button_clicked.wav")
            },
            {
                "name": "validation",
                "path": path.join(SOUNDS_PATH, "validation.wav")
            },
            {
                "name": "cancelation",
                "path": path.join(SOUNDS_PATH, "cancelation.wav")
            },
            {
                "name": "element_throwed",
                "path": path.join(SOUNDS_PATH, "element_throwed.wav")
            },
            {
                "name": "fruit_sliced",
                "path": path.join(SOUNDS_PATH, "fruit_sliced.wav")
            },
            {
                "name": "ice_sliced",
                "path": path.join(SOUNDS_PATH, "ice_sliced.wav")
            },
            {
                "name": "bomb_sliced",
                "path": path.join(SOUNDS_PATH, "bomb_sliced.wav")
            },
            {
                "name": "fruit_missed",
                "path": path.join(SOUNDS_PATH, "fruit_missed.wav")
            },
            {
                "name": "game_won",
                "path": path.join(SOUNDS_PATH, "game_won.wav")
            },
            {
                "name": "game_over",
                "path": path.join(SOUNDS_PATH, "game_over.wav")
            }
         )

def load_image(image_name):

    '''
    load image in pygame surface using user friendly name.
    - image names:
        - logo
        - menu_background
        - button_background
        - game_background
        - option_background
        - arrow_left
        - arrow_right
        - scores_board
        - button_background_hover
        - button_background_hover_2
        - apple, sliced_apple, iced_apple
        - banana, sliced_banana, iced_banana
        - kiwi, sliced_kiwi, iced_kiwi
        - orange, sliced_orange, iced_orange
        - pineapple, sliced_orange, iced_orange
        - bomb, iced_bomb
        - ice_cube, sliced_ice_cube
    - states returned:
        0. image loaded successfully
        1. unknown image name
        2. image not found, there's likely a problem in the path
        3. unhandled error
    ### PARAMETER
        image_name: str
    ### RETURN
        image_loaded: pygame.Surface
        or
        error_index: int
    '''

    try:
        for image_available in images:
            if image_available["name"] == image_name:
                try:
                    image_loaded = image.load(image_available["path"])
                except:
                    print("load_image(): image not found, there's likely a problem in the path")
                    return 2 
                return image_loaded
        print("load_image(): unknown image name")
        return 1             
    except:
        print("load_image(): unhandled error")
        return 3
    
def blit_display(window_screen, surface, image_loaded, x_pos=0, y_pos=0, disp=False):

    '''
    blit image loaded on provided surface, easy fill or center the image with 
    center_vertically, center_horizontally or fill bool parameters.
    - states:
        0. image successfully blitted
        1. error when trying to blit
        2. error when trying to scale

    ### PARAMETER
        surface: pygame.Surface
        image_loaded: str
        x_pos: int horizontal distance from surface left side
        y_pos: int vertical distance from surface top side
        disp: bool default:False define entity type
    ### RETURN
        state: int
    '''
        
    try:
        try:
            if disp:
                w, h = display.get_window_size()
                image_loaded = transform.scale(image_loaded,(w,h))
        except:
            print(f"blit_image(): error when trying to scale display{image_loaded}")
            return 2
        window_screen.blit(image_loaded,(0,0))
        return 0
    except:
        print(f"blit_image(): error when trying to blit display{image_loaded}")
        return 1

def blit_rect(window_screen, surface, image_loaded, x_pos=0, y_pos=0,rect = False):

    '''
    blit image loaded on provided surface, easy fill or center the image with 
    center_vertically, center_horizontally or fill bool parameters.
    - states:
        0. image successfully blitted
        1. error when trying to blit
        2. error when trying to scale

    ### PARAMETER
        surface: pygame.Surface
        image_loaded: str
        x_pos: int horizontal distance from surface left side
        y_pos: int vertical distance from surface top side
        rect: bool default:False define entity type
    ### RETURN
        state: int
    '''
        
    try:
        try:
            if rect:
                image_loaded = transform.scale(image_loaded,(surface.width, surface.height))
        except:
            print(f"blit_image(): error when trying to scale {image_loaded}")
            return 2
        window_screen.blit(image_loaded, surface)
        return 0
    except:
        print(f"blit_image(): error when trying to blit {image_loaded}")
        return 1

def blit_arrow(window_screen, surface, image_loaded, x_pos=0, y_pos=0, arrow= False):

    '''
    blit image loaded on provided surface, easy fill or center the image with 
    center_vertically, center_horizontally or fill bool parameters.
    - states:
        0. image successfully blitted
        1. error when trying to blit
        2. error when trying to scale

    ### PARAMETER
        surface: pygame.Surface
        image_loaded: str
        x_pos: int horizontal distance from surface left side
        y_pos: int vertical distance from surface top side
        arrow: bool default:False define entity type
    ### RETURN
        state: int
    '''
        
    try:
        try:
            if arrow:
                image_loaded = transform.scale(image_loaded,(60,60))
        except:
            print(f"blit_image(): error when trying to scale {image_loaded}")
            return 2
        #window_screen.blit(image_loaded,surface)
        return 0
    except:
        print(f"blit_image(): error when trying to blit {image_loaded}")
        return 1


def play_sound(sound_name, looping=False):

    '''
    draw sound in pygame using friendly name.
    - sound names:
        - menu_music
        - game_music
        - button_clicked
        - validation
        - cancelation
        - element_throwed
        - fruit_sliced
        - ice_sliced
        - bomb_sliced
        - fruit_missed
        - game_won
        - game_over
    - states returned:
        0. sound played successfully
        1. unknown sound name
        2. sound not found, there's likely a problem in the path
        3. unhandled error
    ### PARAMETER
        sound_name: str
    ### RETURN
        state: int
    '''

    try:
        for sound in sounds:
            if sound["name"] == sound_name:
                try:
                    sound_loaded = mixer.Sound(sound["path"])
                except:
                    print("play_sound(): sound not found, there's likely a problem in the path")
                    return 2
                if looping == False:
                    sound_loaded.play()
                else:
                    sound_loaded.play(-1)
                return 0
        print("play_sound(): unknown sound name")
        return 1             
    except:
        print("play_sound(): unhandled error in play_sound()")
        return 3