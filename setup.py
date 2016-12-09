from setuptools import setup

setup(
        name='Python Soroban',
        version='0.0',
        py_modules=['pysoroban'],
        packages=['pysoroban'],
        install_requires=[
            'Click',
            'numpy',
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
