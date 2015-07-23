#!/usr/bin/env python
import sys
import kvaut.server

if __name__ == '__main__':
    kvaut.server.start_automation_server()

    from ci_screen.ci_screen_app import CiScreenApp
    CiScreenApp().run()
