from jinja2 import Environment, FileSystemLoader
import MDParsing
import MDListing

# load layout folder
env = Environment(loader=FileSystemLoader(['layout', '.']))

# render 404.html
template = env.get_template('404.html')
with open('404.html', 'w') as f:
    f.write(template.render())
    f.close()

# render home-test.html
template = env.get_template('home.html')
with open('home.html', 'w') as f:
    f.write(template.render())
    f.close()