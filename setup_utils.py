from setuptools import Command

cmdclass = {}  # Initialize the cmdclass dictionary here

def add_command(name):
    def decorator(command):
        assert issubclass(command, Command)
        cmdclass[name] = command
        return command
    return decorator