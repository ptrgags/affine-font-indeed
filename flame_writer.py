import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

class FlameWriter(object):
    """
    Class that takes a sequence of xforms and
    produces an Apophysis .flame file
    """
    def __init__(self):
        self.template = self.get_template()


    def write(self, fname, flame_name, xforms):
        """
        Template the flame file and write it to disk.
        """
        # Extract the part of the filename before the extension
        _, basename = os.path.split(fname)
        file_id, _ = os.path.splitext(basename)

        # Now template the file
        text = self.template.render(
            file_id=file_id, name=flame_name, xforms=xforms)

        # Finally, write it to disk
        with open(fname, 'w') as flame_file:
            flame_file.write(text)

    @classmethod
    def get_template(cls):
        """
        Fetch the template from disc
        """
        loader = FileSystemLoader('./templates')
        env = Environment(loader=loader)
        return env.get_template('template.flame')
        
