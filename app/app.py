from jinja2 import Environment, FileSystemLoader
import MDParsing
import MDListing
import os

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

# render article while construct index pages list
# demo: section = {sectionname: architecture, cards: False, posts:[{}, {}, ]}, sections = [section1, section2, ]
architcture = {'sectionname': 'Architecture And Urban Design', 'cards': True, 'posts':[]}
workpieces = {'sectionname': 'Work Pieces', 'cards': True, 'posts':[]}
code = {'sectionname': 'Coding', 'cards': False, 'posts':[]}
digest = {'sectionname': 'Digest', 'cards': False, 'posts':[]}
tabs = {'sectionname': '', 'cards': True, 'posts':[]}

template_article = env.get_template('article-dev.html')
for post in MDPathInstance.mdlist:
    MDPostInstance = MDParsing.MDPost(post)
    MDPostInstance.htmlParsing()
    MDPostInstance.soupParsing()
    MDPostInstance.modifyHTagAnchor()
    MDPostInstance.modifyIMGPath()
    MDPostInstance.modifyTableHead()
    destpth = MDListing.MDPath.convertPath(post, desp)
    MDPostInstance.setYAMLDictAttr('url', destpth)
    MDPostInstance.setYAMLDictAttr('abstract', 'This is an urban design project for envisioning the future of the U.S. Space & Rocket Center at Huntsville, AL.<br>The entry point of the project is the hydrological characteristics of the site. The site is modified as a dynamic plan for both flooding and dry seasons. The master plan integrates the site as part of Singing River Trail of the city, and expands the campus along four parallel corridors - mountain bike trail, riverfront walk, central boulevard and service drive. Each corridor addresses various modes of travel and forms part of the phasing plan for the future.')
    pthls = destpth.split(os.path.sep)
    if pthls[1] == '00projects':
        if pthls[2] == 'workpieces':
            workpieces['posts'].append(MDPostInstance.YAMLDict)
        else:
            architcture['posts'].append(MDPostInstance.YAMLDict)
    elif pthls[1] == '01blog':
        if pthls[2] == '00coding':
            code['posts'].append(MDPostInstance.YAMLDict)
        else:
            digest['posts'].append(MDPostInstance.YAMLDict)
    else:
        tabs['posts'].append(MDPostInstance.YAMLDict)
    with open(destpth, 'w') as f:
        f.write(template_article.render(headerimg=MDPostInstance.YAMLDict['head image'],
                                posthtml=MDPostInstance.soup,
                                title=MDPostInstance.YAMLDict['title'],
                                posttitle=MDPostInstance.YAMLDict['title'],
                                tochtml=MDPostInstance.tochtml))

architcture['posts'] = sorted(architcture['posts'], key=lambda x: x['modify date'], reverse=True)
workpieces['posts'] = sorted(workpieces['posts'], key=lambda x: x['modify date'], reverse=True)
code['posts'] = sorted(code['posts'], key=lambda x: x['modify date'], reverse=True)
digest['posts'] = sorted(digest['posts'], key=lambda x: x['modify date'], reverse=True)
tabs['posts'] = sorted(tabs['posts'], key=lambda x: x['modify date'], reverse=True)

architcture['posts'].insert(2, {'title': 'Equity in the Access to Medical Resources During COVID-19',
                                'url': '/equity-during-covid/',
                                'tags': ['Big Data', 'Visualization', 'New York City', 'D3', 'Python'],
                                'head image': '/assets/img/00architecture/10-mitbiddata/00covercover.jpg'})


# TODO: integrate 2 layouts in articles.html, with different class name and id name
# TODO: integrate js and css
# TODO: audit tag info for each card, make them clickable

# render design page
template = env.get_template('articles.html')
with open('design-dev.html', 'w') as f:
    f.write(template.render(sections=[architcture, workpieces],
                            titlename='Design',
                            headerimg='/assets/img/covers/architecturecover.jpg'))