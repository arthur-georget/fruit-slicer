from src.assets_management import load_image
from pygame import Rect, transform 

WIDTH = 1300
HEIGHT = 731
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 70
center_x = WIDTH // 2
center_y = HEIGHT // 2

def draw_text(text, size, color, center, window_surface,custom_font):
    text_surface = custom_font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window_surface.blit(text_surface, text_rect)

def draw_button_pic(x, y, width, height, image, window):
    """Draw Button size, position and screen"""
    rect = Rect(x, y, width, height)
    image = transform.scale(image, (width, height))
    window.blit(image, rect)
    return rect

# Play_button
play_button = Rect((center_x - (BUTTON_WIDTH/2), center_y + 110),(BUTTON_WIDTH,BUTTON_HEIGHT))
# Options button
options_button = Rect((center_x - (BUTTON_WIDTH/2), center_y + 280),(BUTTON_WIDTH,BUTTON_HEIGHT)) 
# Exit button
exit_button = Rect((center_x - (BUTTON_WIDTH/2)+ BUTTON_WIDTH + 390, center_y + 280),(BUTTON_WIDTH / 3,BUTTON_HEIGHT))
# Difficulty rect
difficulty_button = Rect((center_x - (BUTTON_WIDTH/2), center_y + 200),(BUTTON_WIDTH,BUTTON_HEIGHT))

#----------#
# Variables
#----------#
difficulty_index = 0
#Load
arrow_left_png = load_image( "arrow_left")
arrow_right_png = load_image( "arrow_right")
menu_background = load_image( "menu_background")
button_background = load_image( "button_background_hover")
button_background_hover = load_image( "button_background_hover_2")
score_background = load_image("scores_board")

# Score Test
#current_score = 40 
your_score_center = (180, 200)
top_scores_centers = [
    (110, 275),  
    (110, 320),  
    (110, 365),  
]
top_scores = ["1. 3000", "2. 2750", "3. 2600"]

# Scale
## Background
menu_background = transform.scale(menu_background,(1300, 731))
## Arrow Difficulty
arrow_left_png = transform.scale(arrow_left_png, (60, 60))
arrow_right_png = transform.scale(arrow_right_png, (60, 60))
## -- Buttons Play / Difficulty / Options / Exit --
button_background_scale_exit = transform.scale(button_background, (BUTTON_WIDTH / 3, BUTTON_HEIGHT))
button_background_hover_scale_exit = transform.scale(button_background_hover, (BUTTON_WIDTH / 3, BUTTON_HEIGHT))
# Arrow rect
left_arrow_rect = arrow_left_png.get_rect()
right_arrow_rect = arrow_right_png.get_rect()
left_arrow_rect.topleft = (center_x - ((BUTTON_WIDTH/2)+ 50), center_y + 208)
right_arrow_rect.topright = (center_x + ((BUTTON_WIDTH/2)+ 55) - 12, center_y + 208)