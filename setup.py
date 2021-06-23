import setuptools

# sets package info using setuptools module
setuptools.setup(
    name='git-dragonfly',
    version='0.1.12',
    description='Bug analysis on Git repositories',
    author='Finn Aspenson, Corbin Vandeventer, Maddi Laizure',
    url='https://mlaizure.github.io/dragonfly/',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'dragonfly = dragonfly.main:main'
        ]
    },
    install_requires=[
        'gitpython',
        'matplotlib'
    ]
)
