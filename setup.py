from setuptools import setup

setup(
    name = 'noty',
    packages=["noty"],
    version = '0.11.0',
    description = 'Creating sticky notes has never been easier.',
    long_desciption = 'A simple GUI sticky note program created with tkinter.',
    author = 'yellowtrr',
    url = 'https://github.com/yellowtrr/noty',
    license = 'MIT',
    py_modules=['noty'],
    install_requires=[''],
    entry_points='''
        [console_scripts]
        noty=noty.main:cli
    ''',
)
