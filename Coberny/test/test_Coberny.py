import os.path
import sys
from download import download
import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import Coberny as cyb
from Coberny.url import *

def test_indice1():   
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('SETE', DISTANCE) == 1


def test_indice2():
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('CASTELNAUDARY', DISTANCE) == 17


def test_indice3():
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('MONTGISCARD', DISTANCE) == 22 
