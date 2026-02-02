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
BLACK = (0, 0, 0)

arrow_left_png = load_image( "arrow_left")
arrow_right_png = load_image( "arrow_right")
menu_background = load_image( "menu_background")
button_background = load_image( "button_background")
button_background_hover = load_image( "button_background_hover")
score_background = load_image("scores_board")
options_background = load_image("option_background")
