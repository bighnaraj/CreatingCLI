from setuptools import setup

setup(
    name='auto',
    version='0.1',
    py_modules=['auto'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        auto=auto:cli
    ''',
)
