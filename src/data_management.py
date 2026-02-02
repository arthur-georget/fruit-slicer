from os import path,pardir
from json import loads,dump

BASE_DIR = path.dirname(path.abspath(__file__))
CONFIG_PATH = path.join(BASE_DIR, pardir, "data", "config.json")
SCORES_PATH = path.join(BASE_DIR, pardir, "data", "scores.json")

def get_json_data(file_path):

    '''
    get json data from file for now you have two default files,
    you can also provide custom file path
    - CONFIG_PATH
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
    - CONFIG_PATH
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