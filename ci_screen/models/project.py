class Project(object):
    
    def __init__(self, name, activity, last_build_status, last_build_time, ci_server):
        self.name = name
        self.activity = activity
        self.last_build_status = last_build_status
        self.last_build_time = last_build_time

    def is_failed(self):
        return self.last_build_status == 'Failure' or self.last_build_status == 'Exception'
