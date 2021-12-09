# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:28:23 2021

@author: olivi
"""

from Coberny import GetListOfPossibleExit

def GetKMaxConstraint(data, entrance, outlet):
    k = len(GetListOfPossibleExit(data, entrance, outlet))
    return k
