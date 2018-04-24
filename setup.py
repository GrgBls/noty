from setuptools import setup

setup(
    name = 'noty',
    packages=["noty"],
    version = '0.9.2',
    description = 'Creating sticky notes has never been easier',
    long_desciption = open('README.md').read(),
    author = 'GrgBls',
    author_email = 'grgbls647@gmail.com',
    url = 'https://github.com/GrgBls/noty',
    py_modules=['noty'],
    install_requires=[],
    entry_points='''
        [console_scripts]
        noty=noty.noty:cli
    ''',
)
