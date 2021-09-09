"""
Take in the filepath to the MD posts folder, find all the post paths,
and return a dictionary of the original paths
with the destination paths correspondingly.
"""

import os

class MDPath():
    """
    Input:
        orip, str, Original path to the folder for all MD posts
        desp, str, Destination path to the foler for articles after convention
    Attributes:
        Dictionary of the original path with destination path.
    """

    def __init__(self, orip, desp):
        """
        Input:
            orip, str, Original path to the folder for all MD posts
            desp, str, Destination path to the foler for articles after convention
        Set the values for the path
        """
        self.orip = orip
        self.desp = desp
    
    def getFiles(self):
        """
        Get all the paths to the MD posts under the original path
        Convert to paths to the html posts under the destination path
        make directories in those locations
        """
        pathdict = {}
        for root, dirs, files in os.walk(self.orip):
            for filename in files:
                if filename == '.DS_Store':
                    continue
                mdpath = os.path.join(root, filename)
                pathls = mdpath.split(os.path.sep)
                pathls[0] = self.desp
                htmlpath = os.path.splitext(os.path.join(*pathls))[0] + '.html'
                pathdict[mdpath] = htmlpath
                os.makedirs(os.path.dirname(htmlpath), exist_ok=True)
        self.pathdict = pathdict

if __name__ == '__main__':
    orip = 'posts'
    desp = 'articles'
    MDPathInstance = MDPath(orip, desp)
    MDPathInstance.getFiles()
    print(MDPathInstance.pathdict)