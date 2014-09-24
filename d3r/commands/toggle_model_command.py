import sublime
import sublime_plugin

class ToggleModelCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        filename = view.file_name()
        print(filename)
        if not "." in filename:
            print(filename + " not found")
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
            print("opening filename " + filename)
            view.window().run_command("open_file", { "file": filename })
