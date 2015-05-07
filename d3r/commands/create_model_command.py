import sublime
import sublime_plugin
import os.path
import datetime

from ..utilities import load_data_file
from ..utilities import find_base_directory
from ..utilities import make_directory
from ..settings import get_setting

class CreateModelCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        view = self.view
        view.window().show_input_panel("Class name for the new model", "", self.on_done, None, None)

    def on_done(self, input):
        self.create_model(input)

    def create_model(self, name):
        if not "_" in name:
            print('Invalid model name ' + name)
            return

        name = name.strip()
        module,model = name.split("_", 1)

        tags    = {
            'model_name': module + '_' + model,
            'author': get_setting('author', 'Your Name <you@d3r.com>'),
            'item_name': model.lower(),
            'table_name': model.lower() + "s",
            'date': datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        }

        files = {
            "php": load_data_file('templates_model_php'),
            "xml": load_data_file('templates_model_xml')
        }

        baseDir = find_base_directory()
        if False == baseDir:
            return

        baseDir = os.path.join(baseDir, 'modules', module, 'models')
        make_directory(baseDir)

        for key in files:
            if not files[key]:
                print('Unable to read model templates')
                return
            content = self.replace_tags(files[key], tags)
            path = os.path.join(baseDir, module + "_" + model + "." + key)
            if os.path.isfile(path):
                print('File ' + path + ' already exists')
                continue
            print('Writing content to file ' + path)
            with open(path, "w") as file:
                file.write(content)
            self.view.window().run_command('open_file', { "file": path })

    def replace_tags(self,content,tags):
        for key in tags:
            replace_key = "@" + key + "@"
            content = content.replace(replace_key, tags[key])
        return content
