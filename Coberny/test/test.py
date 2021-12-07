import os.path
import sys
from download import download
import numpy as np
import pandas as pd

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + (os.path.sep + '..')*2)

import Coberny as cyb

def test_indice1():   
    download(cyb.url_dist, cyb.path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('Sete', DISTANCE) == 1


def test_indice2():
    download(cyb.url_dist, cyb.path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('Castelnaudary', DISTANCE) == 17


def test_indice3():
    download(cyb.url_dist, cyb.path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('Montgiscard', DISTANCE) == 22 
