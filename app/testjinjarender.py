import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('layout'))
template = env.get_template('404.html')

with open('test-render1.html', 'w') as f:
    f.write(template.render())
    f.close()