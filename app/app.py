from jinja2 import Environment, FileSystemLoader
import MDParsing
import MDListing

# load layout folder
env = Environment(loader=FileSystemLoader(['layout', '.']))

# render 404.html
template = env.get_template('404.html')
with open('404.html', 'w') as f:
    f.write(template.render())

# render home-test.html
## TODO: some js, and maybe use for statement in the main page
template = env.get_template('home.html')
with open('home.html', 'w') as f:
    f.write(template.render())

# retrieve all the markdown posts
orip = 'posts'
desp = 'articles'
MDPathInstance = MDListing.MDPath(orip, desp)
MDPathInstance.getFiles()

# render article demo
fp = 'posts/00projects/2020-01-16-theater-design-wudaokou.md'
MDPostInstance = MDParsing.MDPost(fp)
MDPostInstance.htmlParsing()
MDPostInstance.soupParsing()
MDPostInstance.modifyHTagAnchor()
MDPostInstance.modifyIMGPath()
MDPostInstance.modifyTableHead()
template = env.get_template('article-dev.html')
with open('articles/test.html', 'w') as f:
    f.write(template.render(headerimg=MDPostInstance.YAMLDict['head image'],
                            posthtml=MDPostInstance.soup,
                            title=MDPostInstance.YAMLDict['title'],
                            posttitle=MDPostInstance.YAMLDict['title'],
                            tochtml=MDPostInstance.tochtml))