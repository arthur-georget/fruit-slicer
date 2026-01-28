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

def create_letter(element_type,x_pos,y_pos,image_name,letters):
    letters_already_there = ""
    for letter in letters:
        letters_already_there += letter["char"]
    char_to_return = random.choice(KEYBOARD)
    while char_to_return in letters_already_there: 
        char_to_return = random.choice(KEYBOARD)
    return {
    "char" : char_to_return,
    "x_pos" : x_pos,
    "y_pos" : y_pos,
    "time_left" : TIME_INIT_LETTERS,
    "type" : element_type,
    "image_name": image_name}

def spawn_letter(letters):
    if random.random() > 0.9 :
        letters.append(create_letter("ICECUBE",random.randrange(0,1000,10),random.randrange(0,500,10),"ice_cube",letters))
    elif random.random() > 0.8 :
        letters.append(create_letter("BOMB",random.randrange(0,1000,10),random.randrange(0,500,10),"bomb",letters))
    else: 
        letters.append(create_letter("FRUIT",random.randrange(0,1000,10),random.randrange(0,500,10),random.choice(FRUITS),letters))
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

        # Stand by for test
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

