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
MDPathInstance = MDListing.MDPath(orip)
MDPathInstance.getFiles()

# render article
template_article = env.get_template('article-dev.html')
for post in MDPathInstance.mdlist:
    MDPostInstance = MDParsing.MDPost(post)
    MDPostInstance.htmlParsing()
    MDPostInstance.soupParsing()
    MDPostInstance.modifyHTagAnchor()
    MDPostInstance.modifyIMGPath()
    MDPostInstance.modifyTableHead()
    with open(MDListing.MDPath.convertPath(post, desp), 'w') as f:
        f.write(template_article.render(headerimg=MDPostInstance.YAMLDict['head image'],
                                posthtml=MDPostInstance.soup,
                                title=MDPostInstance.YAMLDict['title'],
                                posttitle=MDPostInstance.YAMLDict['title'],
                                tochtml=MDPostInstance.tochtml))

"""
pass to articles:
    a dictionary for a post;
    a list of dictionaries for all the posts in the same folder;
    a dictionary with 2 keys, section name and list of post dictionaries
    a list of those dictionaries
"""