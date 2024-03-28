from setuptools import Command
from setup_utils import add_command
import os
import sys

@add_command('docs')
class DocsCommand(Command):
    """ For building the pygame documentation with `python setup.py docs`.
    This generates html, and documentation .h header files.
    """
    user_options = [
        (
            'fullgeneration',
            'f',
            'Full generation. Do not use a saved environment, always read all files.'
        )
    ]
    boolean_options = ['fullgeneration']

    def initialize_options(self):
        self._dir = os.getcwd()
        self.fullgeneration = None

    def finalize_options(self):
        pass

    def run(self):
        '''
        runs Sphinx to build the docs.
        '''
        import subprocess
        print("Using python:", sys.executable)
        command_line = [
            sys.executable, os.path.join('buildconfig', 'makeref.py')
        ]
        if self.fullgeneration:
            command_line.append('full_generation')
        if subprocess.call(command_line) != 0:
            raise SystemExit("Failed to build documentation")