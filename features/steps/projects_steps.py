from behave import *
import kvaut.client

from features.support.assertions import *
import features.support.helpers as helpers
    

@step(u'I see projects "(?P<projects>[^"]*)"')
def i_see_projects(context, projects):
    for project in projects.split(", "):
        kvaut.client.assert_is_visible(project)

@step(u'I do not see projects "(?P<projects>[^"]*)"')
def i_do_not_see_projects(context, projects):
    for project in projects.split(", "):
        kvaut.client.assert_is_not_visible(project)

@step(u'"(?P<above>[^"]*)" is above "(?P<below>[^"]*)"')
def is_above(context, above, below):
    kvaut.client.assert_is_above(above, below)

@step(u'I see successful projects "(?P<project>[^"]*)"')
def i_see_successful_projects(context, project):
    kvaut.client.assert_is_visible(project, status='Success')

@step(u'I see failed projects "(?P<project>[^"]*)"')
def i_see_failed_projects(context, project):
    kvaut.client.assert_is_visible(project, status='Failure')

@step(u'I do not see failed projects "(?P<project>[^"]*)"')
def i_do_not_see_failed_projects(context, project):
    assert_raises(lambda: kvaut.client.assert_is_visible(project, status='Failure'), kvaut.errors.AssertionError, "Expected error to occur when asserting visible")

@step(u'I do not see successful projects "(?P<project>[^"]*)"')
def i_do_not_see_successful_projects(context, project):
    assert_raises(lambda: kvaut.client.assert_is_visible(project, status='Success'), kvaut.errors.AssertionError, "Expected error to occur when asserting visible")
