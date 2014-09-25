import sublime
import os.path

from .constants import Constants

def load_data_file(filename):
    """This method loads a given filename (no path) from the resources directory"""
    filename = os.path.join('Packages', Constants.PACKAGE, Constants.RESOURCES, filename)
    # print(filename)
    try:
        return sublime.load_resource(filename)
    except IOError:
        return False
