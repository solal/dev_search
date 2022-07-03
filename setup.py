from setuptools import setup

setup(
    name='devsearch',
    version='0.1',
    py_modules=['devsearch'],
    install_requires=[
        'bs4>=0.0.1'
        'click>=8.1.3',
        'rich>=12.4.1',
        'prompt-toolkit>=3.0.29'
    ],
    entry_points='''
        [console_scripts]
        ds=devsearch:cli
    ''',
)
