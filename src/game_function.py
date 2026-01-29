import random


# --- CONSTANT ---

KEYBOARD = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",";",":","!","$")
FRUITS = ("apple","banana","kiwi","orange","pineapple")
LIFE_MAX = 3
SCORE_ADD = 1

# Time
FPS = 60
TIME_INIT_LETTERS = 5.0
SPAW_INIT = 1.0
SPEED_RATIO = 0.80
MAX_COMBO = 3
FREEZE_DURATION = 10.0

# Functions

def create_element(element_type,x_pos,y_pos,image_name):
    return {
    "char" : random.choice(KEYBOARD),
    "x_pos" : x_pos,
    "y_pos" : y_pos,
    "time_left" : TIME_INIT_LETTERS,
    "type" : element_type,
    "image_name": image_name}

def spawn_element(elements):
    if random.random() > 0.9 :
        elements.append(create_element("ICECUBE",random.randrange(0,1000,10),random.randrange(0,500,10),"ice_cube"))
    elif random.random() > 0.8 :
        elements.append(create_element("BOMB",random.randrange(0,1000,10),random.randrange(0,500,10),"bomb"))
    else: 
        elements.append(create_element("FRUIT",random.randrange(0,1000,10),random.randrange(0,500,10),random.choice(FRUITS)))
    return 0.0

def update_elements(elements, delta, combo, frozen = False):
    broken_combo = False
    life_lost = 0
    
    for element in elements[:]:
        if frozen == True:
            pass
        else:    
            element["time_left"] -= delta * SPEED_RATIO

        if element["time_left"] <= 0:
            elements.remove(element)
            life_lost += 1
            broken_combo = True

    # Combo broken 
    if broken_combo == True:
        combo = 0
    return life_lost, combo

def slice_element(elements, key, combo, combo_valid):
    icecube_hit = False
    bomb_hit = False
    score = 0

    for element in elements[:]:
        if element["char"] == key:

            if element["type"] == "BOMB":
                bomb_hit = True 
            elif element["type"] == "ICECUBE":
                icecube_hit = True

            elements.remove(element)

            if combo_valid:
                combo = min(combo + 1, MAX_COMBO)
            else :
                combo = 0
        score = 1 + combo
        break
            
    return score, combo, icecube_hit, bomb_hit

def combo_add_score(score, combo):
    return score * (1 + combo)