import sublime
import sublime_plugin
import os.path

class ToggleModelCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        filename = view.file_name()

        if not "." in filename:
            print(filename + " doesn't seem to have an extension")
            return

        current = filename[-4:]
        if ".xml" == current:
            ext = ".php"
        elif ".php" == current:
            ext = ".xml"
        else:
            ext = None

        if ext:
            filename = filename[:-4] + ext
            if os.path.isfile(filename):
                view.window().run_command("open_file", { "file": filename })

