import os
import shutil
import json
from definitions import ROOT_DIR

themes_folder_path = os.path.join(ROOT_DIR+'/themes')
src_folder_path = os.path.join(ROOT_DIR+'/src')

author = ''
site_title = ''
email = ''
about = """
Congratulations! You successfuly forged a full-metal static site.\n
please edit yor "About" in config.json file (or manually edit the html file in src folder for more control).
you can change theme, or change any site settings on the config.json file.
"""

def quickstart(config, env):
    theme = config['theme']
    theme_location = ''

    site_title = input('[+] Please enter your website title: ')
    author = input('[+] Please enter your name: ')
    email = input(f'[+] Input your email if you want [{author}@{site_title}.com]: ')

    # Write basic info into config.json
    config_data = [config, {
        "author" : author,
        "site_title" : site_title,
        "email" : email,
        "about" : about,
    }]
    with open('./config.json', 'w') as config_file:
        json.dump(config_data, config_file, indent=4)

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
        quit()

    print('quick start complete.')
