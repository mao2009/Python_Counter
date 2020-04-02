from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='counter', 
    module='count.py',
    version='1.0.0',
    license='BSD',

    author='mao2009',

    url='https://github.com/mao2009/Python_Counter',

    description='Alternative for Range and Enumerator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='range enumrator'

)