from distutils.core import setup

setup(
    name = 'Noty',
    version = '0.1.0',
    description = 'Creating sticky notes has never been easier',
    author = 'GrgBls',
    author_email = 'gmpalis6@gmail.com',
    url = 'https://github.com/GrgBls/Noty', 
    py_modules=['Noty'],
    install_requires=[
        # list of this package dependencies
    ],
    entry_points='''
        [console_scripts]
        Noty=Noty:cli
    ''',
)
