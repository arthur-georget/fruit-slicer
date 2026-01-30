from pygame import transform
from src.assets_management import load_image
#------#
# SIZES
#------#
WIDTH = 1300
HEIGHT = 731
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70
center_x = WIDTH // 2
center_y = HEIGHT // 2
#-------#
# COLORS
#-------#
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

arrow_left_png = load_image( "arrow_left")
arrow_right_png = load_image( "arrow_right")
menu_background = load_image( "menu_background")
button_background = load_image( "button_background_hover")
button_background_hover = load_image( "button_background_hover_2")
score_background = load_image("scores_board")

## Arrow Difficulty
arrow_left_png = transform.scale(arrow_left_png, (60, 60))
arrow_right_png = transform.scale(arrow_right_png, (60, 60))
## Arrow rect
left_arrow_rect = arrow_left_png.get_rect()
right_arrow_rect = arrow_right_png.get_rect()
left_arrow_rect.topleft = (center_x - ((BUTTON_WIDTH/2)+ 50), center_y + 208)
right_arrow_rect.topright = (center_x + ((BUTTON_WIDTH/2)+ 55) - 12, center_y + 208)