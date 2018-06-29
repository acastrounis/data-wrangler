# https://test.pypi.org/project/wranglyzer/

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='wranglyzer',
    url='https://github.com/acastrounis/wranglyzer',
    author='Alex Castrounis',
    author_email='dev@innoarchitech.com',
    packages=['wranglyzer'],
    # packages=setuptools.find_packages(),
    # install_requires=['numpy', 'pandas'], # TODO: Fill in
    version='0.0.2.dev0',
    license='MIT',
    description='A python package for routine data wrangling and analytics tasks',
    long_description=long_description,
    long_description_content_type="text/markdown",
    # scripts = [''],
    python_requires='>=3.6.*',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)