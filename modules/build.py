import os
from definitions import ROOT_DIR

build_folder_path = os.path.join(ROOT_DIR+'/build')

def build(config, env):
    # Render default template
    # TODO render all site
    # for now, the only thing that rendred is index.html
    print('rendering site...')
    index_template = env.get_template('index.html')
    with open(f'{build_folder_path}/index.html', 'w') as output_file:
        output_file.write(
            index_template.render(
                title=config['site_title'],
                about=config['about']
            )
        )

    print('build complete, run "fullmetal serve" to preview your site.')
