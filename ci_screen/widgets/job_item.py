from kivy.uix.listview import SelectableView
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

from ci_screen.models.project import Project


class JobItem(SelectableView, Widget):

    project = ObjectProperty(defaultvalue=Project(name=''), rebind=True)

    @classmethod
    def args_converter(cls, index, data_item):
        return { 'project': data_item }

    def __init__(self, *args, **kwargs):
        super(SelectableView, self).__init__()
        super(Widget, self).__init__(*args, **kwargs)
        self.project = kwargs.get('project')
