from os import path,pardir
from pygame import image,mixer,transform

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

def blit_image(surface, image_name, x_pos, y_pos, centered=False, filling=True):

    '''
    draw image in pygame using friendly name.
    - image names:
        - logo
        - menu_background
        - button_background
        - game_background
        - option_background
        - arrow_left
        - arrow_right
        - scores_board
    - states returned:
        0. image draw successfully
        1. unknown image name
        2. image not found, there's likely a problem in the path
        3. unhandled error
    ### PARAMETER
        surface: pygame.Surface
        image_name: str
        x_pos: int horizontal distance from surface left side
        y_pos: int vertical distance from surface top side
        centered: bool default:False define whether is centered or not around the position provided
        filling: bool default:True define whether the image must fill or not completely the surface
    ### RETURN
        state: int
    '''

    try:
        for image_available in images:
            if image_available["name"] == image_name:
                try:
                    image_loaded = image.load(image_available["path"])
                    if filling:
                        image_loaded = transform.scale(image_loaded,(surface.get_width(),surface.get_height()))
                except:
                    print("blit_image(): image not found, there's likely a problem in the path")
                    return 2
                if centered:
                    x_pos = (x_pos - image_loaded.get_width()/2)
                    y_pos = (y_pos - image_loaded.get_height()/2)
                surface.blit(image_loaded, (x_pos, y_pos))
                return 0
        print("blit_image(): unknown image name")
        return 1             
    except:
        print("blit_image(): unhandled error in blit_image()")
        return 3

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