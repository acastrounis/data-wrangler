name = "wrangalytics"

### Import statements
# import wrangalytics
# import wrangalytics.config.api
# import wrangalytics.converters.api
# import wrangalytics.eda.viz.api
# import wrangalytics.eda.stats.api

### Import base functions

from IPython.display import display

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf

import scipy
from scipy import stats

import sklearn

# import wrangalytics
# from wrangalytics.config import api as config

from wrangalytics.converters.api import percent2float as p2f
from wrangalytics.converters.api import str2float as s2f
from wrangalytics.converters.api import str2int as s2i

from imp import reload