import sys
from setuptools import setup
from distutils.core import setup

DISTNAME = 'wranglyzer'

setup(
    name=DISTNAME,
    url='https://github.com/acastrounis/wranglyzer',
    author='Alex Castrounis',
    packages=['wranglyzer', 'wranglyzer.*'],
    install_requires=['numpy'], # TODO: Fill in
    version='0.1',
    license='MIT',
    description='A python package for routine data wrangling and EDA tasks',
    long_description=open('README.txt').read(),
    scripts = [''], # ['scripts/hello.py']
    python_requires='>=3.6.*',
    **setuptools_kwargs
)