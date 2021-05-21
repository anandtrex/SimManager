__author__ = "Arjun Rao, Anand Subramoney"
__version__ = "0.8.4"

from .paths import Paths
from .simmanager import SimManager

__all__ = ['Paths', 'SimManager']

import random
from datetime import datetime

def get_random_name():
    datetime_suffix = datetime.now().strftime("D%d-%m-%Y-T%H-%M-%S")
    randnum = str(random.randint(1e3, 1e5))
    sim_name = "sim-{}-{}".format(randnum, datetime_suffix)
    return sim_name
