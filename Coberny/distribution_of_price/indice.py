def indice(l, DISTANCE):
    ind = 0
    for i in range(DISTANCE.shape[0]):
        if (DISTANCE.columns[i+1] == l):
            return i 
        else: i = i + 1
    
