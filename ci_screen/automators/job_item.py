from kvaut.automator.custom_automator import CustomAutomator


class JobItemAutomator(CustomAutomator):

    def is_match(self, value=None, **custom_attributes):
        if 'status' not in custom_attributes:
            return False

        project = self._target.project
        return value == project.name and custom_attributes['status'] == project.last_build_status
