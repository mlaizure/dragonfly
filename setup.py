import setuptools

setuptools.setup(
    name='git-dragonfly',
    version='0.1.6',
    description='Bug analysis on Git repositories',
    author='Finn Aspenson, Corbin Vandeventer, Maddi Laizure',
    url='https://mlaizure.github.io/dragonfly/',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'dragonfly = dragonfly.__main__:main'
        ]
    },
    install_requires=[
        'gitpython',
        'matplotlib'
    ]
)
