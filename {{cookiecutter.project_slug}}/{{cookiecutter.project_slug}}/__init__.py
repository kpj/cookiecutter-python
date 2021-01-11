# set version dunder variable
from importlib import metadata

__version__ = metadata.version('{{cookiecutter.project_slug}}')
