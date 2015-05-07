import sublime
import os
import errno

from .constants import Constants
from .settings import get_setting

def load_data_file(key):
    """This method loads a given data file key from the resources directory"""
    filename = get_setting(key)
    filenames = [
        filename, # Absolute path
        os.path.join('Packages', 'User', Constants.PACKAGE, filename), # Template in the User\SublimeD3R
        os.path.join('Packages', Constants.PACKAGE, Constants.RESOURCES, filename) # Standard package template
    ]
    for f in filenames:
        try:
            if (os.path.exists(f)):
                # print('Attempting disk load : ' + f)
                handle = open(f, "r")
                return handle.read()
            else:
                # print('Attempting resource load : ' + f)
                return sublime.load_resource(f)
        except FileNotFoundError:
            print('FileNotFoundError : ' + f)
        except IOError:
            print('IOError : ' + f)
    return False

def find_base_directory(rootDir = False):
    if False == rootDir:
        rootDir = sublime.active_window().active_view().file_name()
    if None == rootDir:
        sublime.status_message('Sorry! You need to open a file before we can work out paths')
        return False
    root = os.path.abspath(os.path.join(rootDir, os.pardir))

    for dirname in os.listdir(root):
        if "." == dirname or ".." == dirname:
            continue
        if "home" == dirname:
            return False
        if "/" == dirname:
            return False
        if "core" == dirname:
            return root
    return find_base_directory(root)

def make_directory(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
