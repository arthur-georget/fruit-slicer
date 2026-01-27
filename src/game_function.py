# Functions
from logic_constant import *
import random

def create_letter():
    return {
    "char" : random.choice(KEYBOARD),
    "time_left" : TIME_INIT_LETTERS }

def spawn_letter(letters, spwan_timer):
    letters.append(create_letter())
    return 0.0

def update_letters(letters, delta):
    lost_life = 0
    for letter in letters[:]:
        letter["time_left"] -= delta * SPEED_RATIO
        if letter["time_left"] <= 0:
            letters.remove(letter)
            lost_life += 1
    return lost_life

def key_input(letters, key):
    score = 0
    for letter in letters[:]:
        if letter["char"] == key:
            letters.remove(letter)
            score += 1
            break
    return score
