#!/usr/bin/env python
import sys
import kvaut.server
from ci_screen.automators.job_item import JobItemAutomator
from ci_screen.widgets.job_item import JobItem


if __name__ == '__main__':
    kvaut.automator.factory.register((JobItem, JobItemAutomator))
    kvaut.server.start_automation_server()

    from ci_screen.ci_screen_app import CiScreenApp
    CiScreenApp().run()
