import sublime
import sublime_plugin

import re

class ExtractInterfaceCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        print('here')
        view = self.view
        region = view.find(r"class\s+\w+\s+\{", 0)
        if region.empty():
            return sublime.status_message('No class definition found')

        print(view.substr(region))

        # Hack hack hacky
        # Find the end of the class by expanding the selection to the matching
        # bracket. Store and restore the current selection while we're at it!
        stored = [[item.a, item.b] for item in view.sel()]
        view.sel().clear()
        view.sel().add(region)
        view.run_command('expand_selection', { "to": "brackets" })
        region = view.sel()[0]
        view.sel().clear()

