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
    assert cyb.ind('Agde Pezenas', DISTANCE) == 2


def test_indice2():
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.ind('Castelnaudary', DISTANCE) == 17


def test_indice3():
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.ind('Montgiscard', DISTANCE) == 22


def KMaxConstraint():
    download(url_prix , path_prix , replace=True)
    assert cyb.GetKMaxConstraint(df_price, 'Sete', 'Narbonne est ') == 4

def cheaperPath():
    download(url_prix , path_prix , replace=True)
    couple = cyb.FindBestPathForPrice(df_price, 'St-Jean-de-Vedas', 'Montgiscard', 3)
    cheaper_path = couple[0]
    assert cheaper_path == ['St-Jean-de-Vedas', 'Sete', 'Agde Pezenas', 'Narbonne sud',
                            'Montgiscard']
    
def PricecheaperPath():
    download(url_prix , path_prix , replace=True)
    couple = cyb.FindBestPathForPrice(df_price, 'St-Jean-de-Vedas', 'Bram', 3)
    PriceOfCheaperPath = couple[1]
    assert PriceOfCheaperPath == 14.7
