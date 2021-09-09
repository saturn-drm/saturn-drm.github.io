"""
Take in a filapath to a MD post, and parse its content with YAML, toc, and code,
modify part of the content,
and return dictionary of YAML, as well as html content after parsing.
"""

from frontmatter import Frontmatter
import markdown
from bs4 import BeautifulSoup
import re

class MDPost():
    """
    Input:
        filepath, str, the filepath to each MD post
    Attributes:
        filepath, str
        YAML head information, dictionary
        TOC, html soup
        content, html soup
    """
    def __init__(self, filepath):
        """
        Input:
            filepath, str, filepath to the MD post
        Parse the post by Frontmatter,
        and set up the value for YAML dictionary and contents.
        """
        MDINFOs = Frontmatter.read_file(filepath)
        self.YAMLDict = MDINFOs['attributes']
        self.contentstr = MDINFOs['body']
    
    def htmlParsing(self, extensions=['toc', 'tables','fenced_code']):
        """
        Input:
            self.contentstr, str, markdown content
        Set up the values for:
            content hmtl
            TOC html
        """
        MDMethod = markdown.Markdown(extensions=extensions)
        self.contenthtml = MDMethod.convert(self.contentstr)
        self.tochtml = MDMethod.toc

    def soupParsing(self):
        """
        Input:
            self.contenthtml, html str
        Set up the value for:
            self.soup, soup
        """
        self.soup = BeautifulSoup(self.contenthtml, 'html.parser')
    
    def modifyHTagAnchor(self):
        """add class to <h> tag to avoid header overlapping the anchor"""
        headList = self.soup.findAll(re.compile('^h\d'))
        for tag in headList:
            if tag.has_attr('class') and 'anchor' not in tag['class']:
                tag['class'].append('anchor')
            elif tag.has_attr('class') and 'anchor' in tag['class']:
                pass
            else:
                tag['class'] = 'anchor'
    
    def modifyIMGPath(self):
        """pay attention to image filepath"""
        IMGList = self.soup.select('p img')
        for IMGTag in IMGList:
            orisrc = IMGTag['src']
            pathList = orisrc.split('/')
            IMGTag['src'] = '/' + '/'.join(pathList[pathList.index('assets'):])

    def modifyTableHead(self):
        """delete table head content"""
        tableHeadList = self.soup.findAll("th")
        for tableHead in tableHeadList:
            tableHead.string = ''

if __name__ == '__main__':
    fp = 'posts/00projects/2020-01-16-theater-design-wudaokou.md'
    MDPostInstance = MDPost(fp)
    MDPostInstance.htmlParsing()
    MDPostInstance.soupParsing()
    MDPostInstance.modifyHTagAnchor()
    MDPostInstance.modifyIMGPath()
    MDPostInstance.modifyTableHead()
    print(MDPostInstance.YAMLDict)