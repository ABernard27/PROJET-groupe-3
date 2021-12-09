# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 17:30:36 2021

@author: olivi
"""

from Coberny import GetKMaxConstraint
from Coberny import CreateGraphOfPath
from Coberny import FindShortestPath
from Coberny import ShortestPathWeight
from Coberny import FindBestPathForPriceV2
from Coberny import GetListOfPath
from Coberny import weight

def FindBestPathForPrice(data, entrance, outlet, k):
    if k > GetKMaxConstraint(data, entrance, outlet):
        ans = 'La contrainte k est supérieure au nombre maximal de sorties possibles'
        return ans
    else:
        listOfSP = []
        listOfSPWeight = []
        for i in range(k+1):
            G = CreateGraphOfPath(data, entrance, outlet, i)
            listOfSP.append(FindShortestPath(G, entrance, outlet))
            listOfSPWeight.append(ShortestPathWeight(G, entrance, outlet))
        best_price = min(listOfSPWeight)
        best_price_index = listOfSPWeight.index(best_price)
        bestPathForPrice = listOfSP[best_price_index]
        if len(bestPathForPrice) <= 2+k:
            return (bestPathForPrice, best_price)
        else:
            listOfTuple = GetListOfPath(data, entrance, outlet, k)
            bestTupleForPrice = FindBestPathForPriceV2(data, listOfTuple)
            best_price = weight(data, bestTupleForPrice)
            bestPathForPrice = list(bestTupleForPrice)
            return (bestPathForPrice, best_price)
