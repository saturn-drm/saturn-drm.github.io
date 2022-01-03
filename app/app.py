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
with open('index.html', 'w') as f:
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

template_article = env.get_template('article.html')
for post in MDPathInstance.mdlist:
    MDPostInstance = MDParsing.MDPost(post)
    MDPostInstance.htmlParsing()
    MDPostInstance.soupParsing()
    MDPostInstance.modifyHTagAnchor()
    MDPostInstance.modifyIMGPath()
    MDPostInstance.modifyTableHead()
    destpth = MDListing.MDPath.convertPath(post, desp)
    MDPostInstance.setYAMLDictAttr('url', destpth)
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
                                'cover image': '/assets/img/00architecture/10-mitbiddata/00covercover.jpg',
                                'abstract': """The project is aimed at telling a story to the public on what's happening in the communities’ access to medical resources during the past period, and revealing some possible blind spots
                                            based on the social and economic context of NYC.<br>The project starts with some background
                                            reports on case and death rate by race during COVID-19. It dealt with data on informational
                                            and physical accessibility by ZCTA codes and visualized the data in the scale of the city.
                                            To conclude, the two new accessibility index were synthesized in an interactive map and
                                            chart with current SVI (social vulnerability index), letting the public check which of the
                                            three index might be related more to the inequity reflected on the death rate for some
                                            districts.<br>The project uses Python in data analysis, and D3 in visualization and
                                            interaction."""})


# TODO: audit tag info for each card, make them clickable

# render design page
template = env.get_template('articles.html')
with open('design.html', 'w') as f:
    f.write(template.render(sections=[architcture, workpieces],
                            titlename='Design',
                            headerimg='/assets/img/covers/architecturecover.jpg'))

# render blog page
template = env.get_template('articles.html')
with open('blog.html', 'w') as f:
    f.write(template.render(sections=[code, digest],
                            titlename='Blog',
                            headerimg='/assets/img/covers/codingcover.jpg'))

# render tabs page
template = env.get_template('articles.html')
with open('tabs.html', 'w') as f:
    f.write(template.render(sections=[tabs],
                            titlename='Tabs',
                            headerimg='/assets/img/covers/literaturecover.jpg'))