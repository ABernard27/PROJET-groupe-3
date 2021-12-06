import os.path
import sys
from download import download
import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import Coberny as cyb
from Coberny.io import *
download(url_dist, path_dist, replace=False)
DISTANCE=pd.read_csv("Distance.csv", sep=',')

def test_indice1():
    assert indice('Sete', DISTANCE) == 1


def test_indice2():
    assert indice('Castelnaudary', DISTANCE) == 17


def test_indice3():
    assert indice('Montgiscard', DISTANCE) == 22 
