from setuptools import setup

setup(
        name='Python Soroban',
        version='0.0',
        py_modules=['soroban'],
        install_requires=[
            'Click',
        ],
        entry_points='''
            [console_scripts]
            soroban=soroban:cli
        ''',
)
