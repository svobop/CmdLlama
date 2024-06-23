from setuptools import setup

setup(
    name='ask',
    version='0.1.0',
    py_modules=['ask'],
    install_requires=[
        'Click',
        'ollama'
    ],
    entry_points={
        'console_scripts': [
            'ask = ask:main',
        ],
    },
)