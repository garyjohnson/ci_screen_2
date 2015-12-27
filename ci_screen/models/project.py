from kivy.event import EventDispatcher
from kivy.properties import StringProperty, NumericProperty, AliasProperty


def get_succeeded(*args):
    self = args[0]
    return self.last_build_status != 'Failure' and self.last_build_status != 'Exception'

def set_succeeded(*args):
    return False

class Project(EventDispatcher):

    name = StringProperty('')
    activity = StringProperty('Sleeping')
    last_build_status = StringProperty('Unknown')
    last_build_time = StringProperty('2015-07-01T18:04:22Z')
    succeeded = AliasProperty(get_succeeded, set_succeeded, bind=['last_build_status'])

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.activity = kwargs.get('activity', 'Sleeping')
        self.last_build_status = kwargs.get('last_build_status', 'Unknown')
        self.last_build_time = kwargs.get('last_build_time', '2015-07-01T18:04:22Z')
