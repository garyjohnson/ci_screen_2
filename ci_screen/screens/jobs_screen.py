import xmltodict
import collections
from pydispatch import dispatcher
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.adapters.simplelistadapter import SimpleListAdapter
from kivy.properties import ListProperty

from ci_screen.models.project import Project


class JobsScreen(Screen):

    projects = ListProperty([])
    failed_projects = ListProperty([])

    def __init__(self, **kwargs):
        super(JobsScreen, self).__init__(**kwargs)
        dispatcher.connect(self._on_status_update, "CI_UPDATE", sender=dispatcher.Any)

    def _on_status_update(self, responses, errors):
        bad_ci_servers = errors.keys()
        new_projects = [p for p in self.get_projects_from_responses(responses) if p.last_build_status != 'Unknown']

        self._synchronize_projects(self.projects, [p for p in new_projects if p.succeeded], bad_ci_servers)
        self._synchronize_projects(self.failed_projects, [p for p in new_projects if not p.succeeded], bad_ci_servers)

    def _synchronize_projects(self, projects_model, new_projects, bad_ci_servers):
        new_project_names = [p.name for p in new_projects]
        old_project_names = [p.name for p in projects_model]

        for removed_project in [p for p in projects_model if p.name not in new_project_names and p.ci_server not in bad_ci_servers]:
            projects_model.remove(removed_project)

        for added_project in [p for p in new_projects if p.name not in old_project_names]:
            projects_model.append(added_project)

        for updated_project in [p for p in new_projects if p.name in old_project_names]:
            self.update(updated_project)

        self.sort_by_last_build_time()

    def sort_by_last_build_time(self):
        unsorted_projects = list(self.projects)
        
        for project in unsorted_projects:
            project_index = self.projects.index(project)
            desired_index = project_index
            while desired_index - 1 >= 0:
                project_in_the_way = self.projects[desired_index - 1]
                if project.last_build_time <= project_in_the_way.last_build_time:
                    break
                desired_index -= 1

            if desired_index != project_index:
                self.projects.insert(desired_index, self.projects.pop(project_index))

    def update(self, updated_project):
        project_to_update = next((p for p in self.projects if p.name == updated_project.name), None)
        if project_to_update is not None:
            project_to_update.last_build_time = updated_project.last_build_time
            project_to_update.last_build_status = updated_project.last_build_status
            project_to_update.activity = updated_project.activity

    def get_projects_from_responses(self, responses):
        projects = []
        for ci_server in responses:
            response = responses[ci_server]
            statuses = xmltodict.parse(response.text, dict_constructor=lambda *args, **kwargs: collections.defaultdict(list, *args, **kwargs))
            for response_projects in statuses['Projects']:
                for response_project in response_projects['Project']:
                    project_args = {}
                    project_args['name'] = response_project.get('@name')
                    project_args['activity'] = response_project.get('@activity')
                    project_args['last_build_status'] = response_project.get('@lastBuildStatus')
                    project_args['last_build_time'] = response_project.get('@lastBuildTime')
                    project_args['ci_server'] = ci_server

                    project = Project(**project_args)
                    projects.append(project)
        return projects
