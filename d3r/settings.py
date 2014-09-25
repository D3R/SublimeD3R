import sublime

def filename():
    return 'D3R.sublime-settings'

def get_setting(name, default=None):
    v = sublime.active_window().project_data().get("d3r", {}).get(name, None)
    if v != None:
        return v
    else:
        return sublime.load_settings(filename()).get(name, default)
