# wrangalytics

A python package for routine data wrangling and analytics tasks.

## To Install

PIP via GitHub: pip install -e git+https://github.com/acastrounis/wrangalytics.git#egg=wrangalytics

PIP: pip install wrangalytics

From Conda: conda install -c alexcastrounis wrangalytics

**NOTES** 
- Currently installing with PIP via GitHub ensures the latest version
- The package may not be available for your platform when installing via conda if you receive the error: "PackagesNotFoundError: The following packages are not available from current channels"

## Upgrading

PIP via GitHub: pip install --upgrade -e git+https://github.com/acastrounis/wrangalytics.git#egg=wrangalytics

PIP: pip install --upgrade wrangalytics

From Conda: conda update -c alexcastrounis wrangalytics

## Importing

**Top-level package**

import wrangalytics as <alias>

**Subpackage**

import wrangalytics.<subpackageName> as <alias>

OR

from wrangalytics.<subpackageName> import api as <alias>

**Module APIs**

from wrangalytics.<subpackageName>.api import <apiName> as <alias>

## Documentation

This package does not have accompanying API documentation yet.