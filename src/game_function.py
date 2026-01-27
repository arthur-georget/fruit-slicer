import random


# --- CONSTANT ---

KEYBOARD = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",";",":","!","$"]

LIFE_MAX = 3
SCORE_ADD = 1

# Time
FPS = 60
TIME_INIT_LETTERS = 2.0
SPAW_INIT = 1.0
SPEED_RATIO = 0.80
MAX_COMBO = 6






# Functions

def create_letter():
    return {
    "char" : random.choice(KEYBOARD),
    "time_left" : TIME_INIT_LETTERS }

def spawn_letter(letters):
    letters.append(create_letter())
    return 0.0

def update_letters(letters, delta, combo):
    broken_combo = False
    lost_life = 0
    
    # Try list letters
    for letter in letters[:]:
        letter["time_left"] -= delta * SPEED_RATIO
        if letter["time_left"] <= 0:
            letters.remove(letter)
            lost_life += 1
            broken_combo = True

    # Combo borken 
    if broken_combo == True:
        combo = 0
    return lost_life, combo

def key_input(letters, key, combo):

    hit = False
    score = 0

    for letter in letters[:]:
        if letter["char"] == key:
            letters.remove(letter)
            hit = True
            break

    if hit == True:
        combo = min(combo, MAX_COMBO)
        combo += 1
        score = combo_add_score(1, combo)
    else:
        combo = 0
        score = 0
    return score, combo

def combo_add_score(score, combo):
    return score * (1 + combo)