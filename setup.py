from setuptools import setup

setup(
    name='wranglyzer',
    url='https://github.com/acastrounis/wranglyzer',
    author='Alex Castrounis',
    packages=['wranglyzer'],
    install_requires=['numpy'], # TODO: Fill in
    version='0.1',
    license='MIT',
    description='An example of a python package from pre-existing code',
    long_description=open('README.txt').read(),
    scripts = [''] # ['scripts/hello.py']
)