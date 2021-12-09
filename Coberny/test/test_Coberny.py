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
    assert cyb.indice('AGDE', DISTANCE) == 2


def test_indice2():
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('CASTELNAUDARY', DISTANCE) == 16


def test_indice3():
    download(url_dist, path_dist, replace=True)
    DISTANCE=pd.read_csv("Distance.csv", sep=',')
    assert cyb.indice('MONTGISCARD', DISTANCE) == 21 


df_price = pd.read_csv('prix.csv')
df_price = df_price.fillna(0)


def KMaxConstraint():
    assert GetKMaxConstraint(df_price, 'Sete', 'Narbonne est ') == 4

def cheaperPath():
    couple = FindBestPathForPrice(df_price, 'St-Jean-de-Vedas', 'Montgiscard', 3)
    cheaper_path = couple[0]
    assert cheaper_path == ['St-Jean-de-Vedas', 'Sete', 'Agde Pezenas', 'Narbonne sud',
                            'Montgiscard']
    
def PricecheaperPath():
    couple = FindBestPathForPrice(df_price, 'St-Jean-de-Vedas', 'Bram', 3)
    PriceOfCheaperPath = couple[1]
    assert PriceOfCheaperPath == 14.7
