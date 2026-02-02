from pygame import Rect, transform
from src.constants import center_x, center_y, BUTTON_WIDTH, arrow_left_png, arrow_right_png
# Rects
back_button = Rect(50, 50, 200, 80)

language_button = Rect(center_x - (410/2), 250, 410, 80)
options_button = Rect(center_x - (200/2), 110, 200, 80)


arrow_left_png = transform.scale(arrow_left_png, (60, 60))
arrow_right_png = transform.scale(arrow_right_png, (60, 60))
left_arrow_lang = arrow_left_png.get_rect()
right_arrow_lang = arrow_right_png.get_rect()
left_arrow_lang.topleft = (center_x - ((BUTTON_WIDTH/2)+ 50), 258)
right_arrow_lang.topright = (center_x + ((BUTTON_WIDTH/2)+ 58), 258)
# Music ON/OFF
music_toggle_button = Rect(center_x - (410/2), 340, 410, 60)

# SFX ON/OFF
sfx_toggle_button = Rect(center_x - (410/2), 410, 410, 60)

# Sliders fruités
music_slider = Rect(center_x - (410/2), 560, 410, 20)
sfx_slider = Rect(center_x - (410/2), 680, 410, 20)