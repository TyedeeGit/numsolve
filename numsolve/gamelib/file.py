import os

WORKING_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../', 'numsolve/'))
SETTINGS_DIR = os.path.join(WORKING_DIR, 'settings/')
SAVES_DIR = os.path.join(WORKING_DIR, 'saves/')

def get_settings_file(game: str):
    return os.path.join(SETTINGS_DIR, f'{game}.json')

def get_save_file(game: str, name: str):
    return os.path.join(SAVES_DIR, f'{game}/{name}.json')
