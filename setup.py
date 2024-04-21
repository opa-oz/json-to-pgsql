from setuptools import setup

from mypyc.build import mypycify

setup(
    name='json-to-pgsql',
    packages=['schema'],
    ext_modules=mypycify([
        'schema/__init__.py',
        'schema/parser.py',
    ]),
)
