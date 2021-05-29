from setuptools import setup
setup(
    name = 'dragonfly',
    version = '0.1.0',
    packages = ['dragonfly'],
    entry_points = {
        'console_scripts': [
            'dragonfly = dragonfly.__main__:main'
        ]
    })
