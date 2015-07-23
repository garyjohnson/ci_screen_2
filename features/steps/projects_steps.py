from behave import *
import kvaut.client
    

@step(u'I see projects "(?P<projects>[^"]*)"')
def i_see_projects(context, projects):
    for project in projects.split(", "):
        kvaut.client.assert_is_visible(project)
