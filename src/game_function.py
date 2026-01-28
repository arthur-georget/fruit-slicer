import random


# --- CONSTANT ---

KEYBOARD = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",";",":","!","$"]

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

def create_letter(element_type):
    return {
    "char" : random.choice(KEYBOARD),
    "time_left" : TIME_INIT_LETTERS,
    "type" : element_type}

def spawn_letter(letters):
    if random.random() > 1.00 :
        letters.append(create_letter("ICECUBE"))
    elif random.random() > 1.00 :
        letters.append(create_letter("BOMB"))
    else: 
        letters.append(create_letter("FRUIT"))
    return 0.0

def update_letters(letters, delta, combo, frozen = False):
    broken_combo = False
    lost_life = 0
    
    # Try list letters
    for letter in letters[:]:
        if frozen == True:
            pass
        else:    
            letter["time_left"] -= delta * SPEED_RATIO

        # print(letter["time_left"])

        if letter["time_left"] <= 0:
            letters.remove(letter)
            lost_life += 1
            broken_combo = True

    # Combo borken 
    if broken_combo == True:
        combo = 0
    return lost_life, combo

def slice_element(letters, key, combo, combo_valid):
    combo_hit = False
    icecube_hit = False
    bomb_hit = False
    score = 0
    

    for letter in letters[:]:
        if letter["char"] == key:

            if letter["type"] == "BOMB":
                bomb_hit = True 
            elif letter["type"] == "ICECUBE":
                icecube_hit = True

            letters.remove(letter)

            if combo_valid:
                combo = min(combo + 1, MAX_COMBO)
            else :
                combo = 0
        score = 1 + combo
        break
            
    return score, combo, icecube_hit, bomb_hit

def combo_add_score(score, combo):
    return score * (1 + combo)

