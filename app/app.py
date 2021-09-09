from jinja2 import Environment, FileSystemLoader
import MDParsing
import MDListing

# load layout folder
env = Environment(loader=FileSystemLoader(['layout', '.']))

# # render 404.html
# template = env.get_template('404.html')
# with open('404.html', 'w') as f:
#     f.write(template.render())

# # render home-test.html
# template = env.get_template('home.html')
# with open('home.html', 'w') as f:
#     f.write(template.render())

# retrieve all the markdown posts
orip = 'posts'
desp = 'articles'
MDPathInstance = MDListing.MDPath(orip, desp)
MDPathInstance.getFiles()
print(MDPathInstance.pathdict)

# render article demo
## TODO: title under content, toc, title of page, some js in template
fp = 'posts/00projects/2020-01-16-theater-design-wudaokou.md'
MDPostInstance = MDParsing.MDPost(fp)
MDPostInstance.htmlParsing()
MDPostInstance.soupParsing()
MDPostInstance.modifyHTagAnchor()
MDPostInstance.modifyIMGPath()
MDPostInstance.modifyTableHead()
template = env.get_template('article-dev.html')
with open('articles/test.html', 'w') as f:
    f.write(template.render(headerimg='/assets/img/covers/codingcover.jpg', posthtml=MDPostInstance.soup))