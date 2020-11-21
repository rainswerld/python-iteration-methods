# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='python-iteration-methods',
    version='0.1.0',
    description='Python Iteration Methods Lesson',
    long_description=readme,
    author='<author>',
    author_email='<email>',
    url='https://git.generalassemb.ly/ga-wdi-boston/python-iteration-methods',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
