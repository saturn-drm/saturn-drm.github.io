import os
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('test.html')

title = 'Zihan Mei'
content = '<h1 style="color:red;text-align:center;">Test Content 以及中文</h1><h2 style="text-align:center;">rendered from jinja2 template, customed title, content, and footer.</h2>'
# with open('components/footer.html', 'r') as f:
#     footer = f.read()
#     f.close()

with open('test-render.html', 'w') as f:
    f.write(template.render(title=title, content=content))
    f.close()