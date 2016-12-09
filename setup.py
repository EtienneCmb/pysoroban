from setuptools import setup

setup(
        name='pysoroban',
        version='0.0',
        packages=['pysoroban'],
        description='Simple program for soroban training',
        install_requires=[
            'Click',
            'numpy',
            'time',
        ],
        url='https://github.com/EtienneCmb/pysoroban',
        author='Etienne Combrisson',
        maintainer='Etienne Combrisson',
        author_email='e.combrisson@gmail.com',
        license='GPL-3.0',
        keywords='soroban abacus boulier python training',
        entry_points='''
            [console_scripts]
            pysoroban=pysoroban:cli
        ''',
)
