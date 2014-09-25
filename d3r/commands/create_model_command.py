import sublime
import sublime_plugin
import os.path

from ..utilities import load_data_file
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

        module,model = name.split("_")

        # Set up tags for template replacement
        tags    = {
            'model_name': module + '_' + model,
            'author': get_setting('author', 'Your Name <you@d3r.com>'),
            'item_name': model.lower(),
            'table_name': model.lower() + "s",
        }

        php  = load_data_file('model.php.template')
        xml  = load_data_file('model.xml.template')

        if not php or not xml:
            print('Unable to read model templates')
            return

        php  = self.replace_tags(php, tags)
        xml  = self.replace_tags(xml, tags)

        # Now we just need to write the files to disk and open them!!!

    def replace_tags(self,content,tags):
        for key in tags:
            replace_key = "@" + key + "@"
            content = content.replace(replace_key, tags[key])
        return content

    # def write_file(self,filename,content):

