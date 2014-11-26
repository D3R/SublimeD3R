import sublime
import os
import errno

from .constants import Constants

def load_data_file(filename):
    """This method loads a given filename (no path) from the resources directory"""
    filename = os.path.join('Packages', Constants.PACKAGE, Constants.RESOURCES, filename)
    # print(filename)
    try:
        return sublime.load_resource(filename)
    except IOError:
        return False

def find_base_directory(rootDir = False):
    if False == rootDir:
        rootDir = sublime.active_window().active_view().file_name()

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
