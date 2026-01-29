import random
from pygame import math

KEYBOARD = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",";",":","!","$")
FRUITS = ("apple","banana","kiwi","orange","pineapple")
LIFE_MAX = 3
SCORE_ADD = 1

# Time
FPS = 60
TIME_INIT_LETTERS = 5.0
SPAWN_INIT = 1.0
SPEED_RATIO = 0.80
MAX_COMBO = 3
FREEZE_DURATION = 3.0

# Functions

def create_element(element_type,x_pos,y_pos,image_name,assigned_chars):
    char_to_assign = random.choice(KEYBOARD)
    while char_to_assign in assigned_chars:
        char_to_assign = random.choice(KEYBOARD)
    assigned_chars += char_to_assign
    return {
    "char" : char_to_assign,
    "x_pos" : x_pos,
    "y_pos" : y_pos,
    "velocity" : math.Vector2(0,0),
    "time_left" : TIME_INIT_LETTERS,
    "type" : element_type,
    "sliced": False,
    "image_name": image_name}, assigned_chars

def spawn_element(elements, assigned_chars):
    if random.random() > 0.9 :
        new_element, assigned_chars = create_element("ICECUBE",random.randrange(0,1000,10),-100,"ice_cube", assigned_chars)
        elements.append(new_element)
    elif random.random() > 0.8 :
        new_element, assigned_chars = create_element("BOMB",random.randrange(0,1000,10),-100,"bomb", assigned_chars)
        elements.append(new_element)
    else:
        new_element, assigned_chars = create_element("FRUIT",random.randrange(0,1000,10),-100,random.choice(FRUITS), assigned_chars)
        elements.append(new_element)
    return 0.0, assigned_chars

def update_elements(elements, assigned_chars, delta, combo, frozen = False):
    broken_combo = False
    life_lost = 0
    
    for element in elements[:]:
        if frozen == True:
            pass
        else:    
            element["time_left"] -= delta * SPEED_RATIO

        if element["time_left"] <= 0:
            assigned_chars = assigned_chars.replace(element["char"], '')
            if not (element["type"] == "BOMB" or element["type"] == "ICECUBE"):
                life_lost += 1
                broken_combo = True
            elements.remove(element)

    # Combo broken 
    if broken_combo == True:
        combo = 0
    return life_lost, combo, assigned_chars

def slice_element(elements, assigned_chars, key, combo, combo_valid):
    icecube_hit = False
    bomb_hit = False
    score = 0

    for element in elements:
        if element["char"] == key:
            if not element["type"] == "FRUIT":
                if element["type"] == "BOMB":
                    bomb_hit = True
                elif element["type"] == "ICECUBE":
                    icecube_hit = True
                assigned_chars = assigned_chars.replace(element["char"], '')
                elements.remove(element)
                break
            assigned_chars = assigned_chars.replace(element["char"], '')
            elements.remove(element)

            if combo_valid:
                combo = min(combo + 1, MAX_COMBO)
            else :
                combo = 0
            score = 1 + combo
        
    return score, combo, icecube_hit, bomb_hit, assigned_chars

def combo_add_score(score, combo):
    return score * (1 + combo)