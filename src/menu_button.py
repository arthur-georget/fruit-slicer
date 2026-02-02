from pygame import Rect, transform
from src.constants import arrow_left_png, arrow_right_png, center_x, center_y, GREEN, YELLOW,PURPLE, RED, BUTTON_WIDTH, BUTTON_HEIGHT

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

## Arrow Difficulty
arrow_left_png = transform.scale(arrow_left_png, (60, 60))
arrow_right_png = transform.scale(arrow_right_png, (60, 60))
## Arrow rect
left_arrow_rect = arrow_left_png.get_rect()
right_arrow_rect = arrow_right_png.get_rect()
left_arrow_rect.topleft = (center_x - ((BUTTON_WIDTH/2)+ 50), center_y + 208)
right_arrow_rect.topright = (center_x + ((BUTTON_WIDTH/2)+ 58), center_y + 208)

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

# Score Test
#current_score = 40 
your_score_center = (180, 200)
top_scores_centers = [
    (110, 275),  
    (110, 320),  
    (110, 365),  
]
top_scores = ["1. 3000", "2. 2750", "3. 2600"]


