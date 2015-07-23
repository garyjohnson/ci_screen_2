from kivy.app import App


class CiScreenApp(App):

    def build_config(self, config):
        config.setdefaults('general', {
            'poll_rate_seconds': 10,
        })
