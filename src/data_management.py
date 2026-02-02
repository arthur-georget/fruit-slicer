from os import path,pardir
from json import load,loads,dump

default_settings = {
    "language": "FR",
    "music_volume": 0.5,
    "sfx_volume": 0.5,
    "music_enabled": True,
    "sfx_enabled": True,
    "difficulty": 1
}

BASE_DIR = path.dirname(path.abspath(__file__))
SETTINGS_PATH = path.join(BASE_DIR, pardir, "data", "settings.json")
SCORES_PATH = path.join(BASE_DIR, pardir, "data", "scores.json")

def get_json_data(file_path):

    '''
    get json data from file for now you have two default files,
    you can also provide custom file path
    - SETTINGS_PATH
    - SCORES_PATH
    ### PARAM
            file_path: str
    ### RETURN
            content: dict
    '''

    file = open(file_path, "r")
    content = file.read()
    file.close()
    content = loads(content)
    return content

def set_json_data(file_path,label,value):

    '''
    set json data in file
    - SETTINGS_PATH
    - SCORES_PATH
    ### PARAM
            file_path: str
            label: str
            value: any
    ### RETURN
            status: int
    '''

    file = open(file_path, "r")
    content = file.read()
    file.close()
    content = loads(content)
    content[label] = value
    file = open(file_path, "w")
    dump(content,file,indent=2)
    file.close()
    return 0

def load_settings():
    if SETTINGS_PATH != "":
        with open(SETTINGS_PATH, "r", encoding="utf-8") as f:
            return load(f)
    return default_settings.copy()

def save_settings(settings):
    with open(SETTINGS_PATH, "w", encoding="utf-8") as f:
        dump(settings, f, indent=4)