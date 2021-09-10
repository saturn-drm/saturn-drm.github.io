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

    def __init__(self, orip):
        """
        Input:
            orip, str, Original path to the folder for all MD posts
            desp, str, Destination path to the foler for articles after convention
        Set the values for the path
        """
        self.orip = orip
    
    def getFiles(self):
        """
        Get all the paths to the MD posts under the original path
        Convert to paths to the html posts under the destination path
        make directories in those locations
        """
        mdlist = []
        for root, dirs, files in os.walk(self.orip):
            for filename in files:
                if filename == '.DS_Store':
                    continue
                mdpath = os.path.join(root, filename)
                mdlist.append(mdpath)
        self.mdlist = mdlist
    
    @staticmethod
    def convertPath(path, desp):
        """
        Input:
            path, str, path to md post
            desp, str, path to the destination folder
        Return:
            path for html post
            and makedir
        """
        pathls = path.split(os.path.sep)
        pathls[0] = desp
        htmlpath = os.path.splitext(os.path.join(*pathls))[0] + '.html'
        os.makedirs(os.path.dirname(htmlpath), exist_ok=True)
        return htmlpath


if __name__ == '__main__':
    orip = 'posts'
    desp = 'articles'
    MDPathInstance = MDPath(orip)
    MDPathInstance.getFiles()
    print(MDPath.convertPath(MDPathInstance.mdlist[0], desp))