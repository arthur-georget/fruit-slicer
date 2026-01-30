from src.assets_management import load_image
from pygame import Rect, transform 

def draw_text(text, size, color, center, window_surface,custom_font):
    text_surface = custom_font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    window_surface.blit(text_surface, text_rect)

def draw_button_pic(x, y, width, height, image, window):
    rect = Rect(x, y, width, height)
    image = transform.scale(image, (width, height))
    window.blit(image, rect)
    return rect
