from kivy.app import App

from ci_screen.screens.jobs_screen import JobsScreen
from ci_screen.service.ci_server_poller import CIServerPoller


class CiScreenApp(App):

    def build_config(self, config):
        config.setdefaults('general', {
            'poll_rate_seconds': 10,
        })

    def on_start(self):
        self.ci_poller = CIServerPoller()
        self.ci_poller.start_polling_async()

    def on_stop(self):
        self.ci_poller.stop_polling()

