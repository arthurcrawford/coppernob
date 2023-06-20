from setuptools import setup

setup(
    name='myscript',
    version='0.1.0',
    py_modules=['myscript'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'myscript = myscript:cli',
        ],
    },
)
