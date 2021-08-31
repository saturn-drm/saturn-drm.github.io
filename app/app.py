from jinja2 import Environment, FileSystemLoader

# load layout folder
env = Environment(loader=FileSystemLoader('layout'))

# render 404.html
template = env.get_template('404.html')
with open('404.html', 'w') as f:
    f.write(template.render())
    f.close()