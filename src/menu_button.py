from pygame import Rect, transform

from src.constants import center_x, center_y, BUTTON_WIDTH, BUTTON_HEIGHT

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



# Score Test
#current_score = 40 
your_score_center = (180, 200)
top_scores_centers = [
    (110, 275),  
    (110, 320),  
    (110, 365),  
]
top_scores = ["1. 3000", "2. 2750", "3. 2600"]


