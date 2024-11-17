import sys
from jinja2 import Environment, FileSystemLoader
from json import load, dump

from modules.quickstart import quickstart
from modules.makepost import makepost

# jinja evironment search path
env = Environment(loader=FileSystemLoader(searchpath='./'))

# TODO delete this
# markdown_text = "## Lmao Kekw"
# print(markdown(markdown_text))

def main():
    # load config file
    try:
        with open('./config.json') as config_file:
            config = load(config_file)
    except FileNotFoundError as err:
        print('Config file is missing, generating new config file with default settings.')
        with open('./config.json', 'w') as config_file:
            dump({'theme':'example-theme'}, config_file, indent=4)
            config = load(config_file)

    # TODO remove debug symbol
    print('debug symbol: ', config)

    if "quickstart" in sys.argv:
        quickstart(config, env)

    if "make-post" in sys.argv:
        makepost(env)



if __name__ == "__main__":
    main()
