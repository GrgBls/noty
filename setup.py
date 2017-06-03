from distutils.core import setup

setup(
    name = 'noty',
    packages=["noty"],
    version = '0.2.0',
    description = 'Creating sticky notes has never been easier',
    author = 'GrgBls',
    author_email = 'gmpalis6@gmail.com',
    url = 'https://github.com/GrgBls/noty', 
    py_modules=['noty'],
    install_requires=[
        
    ],
    entry_points='''
        [console_scripts]
        noty=noty.__main__:cli
    ''',
)










