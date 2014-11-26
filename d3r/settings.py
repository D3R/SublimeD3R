import sublime

from .constants import Constants

def get_setting(name, default=None):
    v = sublime.active_window().project_data().get(Constants.CONFIG_NAME, {}).get(name, None)
    if v != None:
        return v
    else:
        return sublime.load_settings(Constants.SETTINGS_FILE).get(name, default)
