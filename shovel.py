import shovel
import subprocess

@shovel.task
def test():
    subprocess.call('tox', shell=True)

