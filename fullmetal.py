import os
import sys
from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load

from modules.quickstart import quickstart

# jinja evironment search path
env = Environment(loader=FileSystemLoader(searchpath='./'))

# markdown_text = "## Lmao Kekw"
# print(markdown(markdown_text))

def main():
    # load config file
    with open('./config.json') as config_file:
        config = load(config_file)

    # TODO remove debug symbol
    print('debug symbol: ', config)

    if "quickstart" in sys.argv:
        quickstart(config)


if __name__ == "__main__":
    main()
