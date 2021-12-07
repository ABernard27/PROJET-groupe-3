import Coberny as cyb
import itertools

def GetListOfPath(data, entrance, outlet, nbr_exit):
    listOfExit = cyb.GetListOfPossibleExit(data, entrance, outlet)
    listOfPath = list(itertools.combinations(listOfExit, nbr_exit))
    for i in range(len(listOfPath)):
        listOfPath[i] = (entrance,) + listOfPath[i] + (outlet,)
    return listOfPath
