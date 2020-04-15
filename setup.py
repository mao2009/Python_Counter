from setuptools import setup
from os import path

with open('README.md') as f:
    long_description = f.read()

setup(
    name='itrcnt', 
    module='itrcnt.py',
    version='0.1.1',
    license='BSD',

    author='mao2009',

    url='https://github.com/mao2009/Python_Counter',

    description='Alternative for Range and Enumerator',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='range enumrator'

)