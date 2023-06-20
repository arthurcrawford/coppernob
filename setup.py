from setuptools import setup

setup(
    name='coppernob',
    version='1.2',
    py_modules=['myscript'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'coppernob = myscript:cli',
        ],
    },
)
