from setuptools import setup

setup(
    name='coppernob',
    version='1.1',
    py_modules=['myscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'coppernob = myscript:cli',
        ],
    },
)
