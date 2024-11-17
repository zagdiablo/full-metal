import os
import shutil
from definitions import ROOT_DIR

themes_folder_path = os.path.join(ROOT_DIR+'/themes')
src_folder_path = os.path.join(ROOT_DIR+'/src')


def quickstart(config):
    theme = config['theme']
    theme_location = ''

    # Check if theme is/are installed correctly
    print(f'checking theme: {theme}...')
    dirs = [x[0] for x in os.walk(themes_folder_path)]
    for dir in dirs:
        if theme in dir:
            print(f'theme {theme} found! copying theme into src folder...')
            theme_location = dir
            break
        else:
            continue
        print(f'theme {theme} not found in the themes folder, make sure it\'s installed correctly.')
        quit()

    # Check if src folder exists
    if not os.path.exists(src_folder_path):
        print('src folder not found, creating src folder...')
        os.makedirs(src_folder_path)

    # Copy theme template into src directory
    print('copying theme into src for editing...')
    try:
        shutil.copytree(theme_location, src_folder_path, dirs_exist_ok=True)
    except FileNotFoundError as file_not_found:
        print(f'Error: ', file_not_found)
        print('quick start failed.')

    print('quick start complete.')
