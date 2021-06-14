import setuptools

setuptools.setup(
    name = 'git-dragonfly',
    version = '0.1.5',
    packages = setuptools.find_packages(),
    entry_points = {
        'console_scripts': [
            'dragonfly = dragonfly.__main__:main'
        ]
    },
    install_requires = [
        'gitpython',
        'matplotlib'
    ]
)
