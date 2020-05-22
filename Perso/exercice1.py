

def comprime(data) :
    """prends une liste en entrée et retourne une liste sans répétitions de nombres"""
    wdict = {}
    listef = list(data)

    for index, elem in enumerate(listef) :
        wdict[index] = elem

    for n in range(len(wdict)-1) :

        if wdict[n] == wdict[n+1] :
            listef.remove(wdict[n])

    return listef



def compte(data) :
    """Prends une liste d'entiers en entrée, et retourne une liste sans répétitions et avec comptage des éléments répétés"""
    #initialisation des variables :

    wdict = {}
    cdict = {}
    listef = []
    listetemp = list(data)

    #On crée un dictionnaire de travail (wdict) et un dictionnaire de comptage (cdict) à partir des indexs et des valeurs de la liste :
    for index, elem in enumerate(listetemp) :
        wdict[index] = elem
        cdict[elem] = 1


    for n in range(len(wdict)-1) :
        #si on a deux valeurs adjacentes identiques, on retire cette valeur de la liste, et on incrémente le compteur de la valeur dans le dictionnaire de comptage
        if wdict[n] == wdict[n+1] :
            listetemp.remove(wdict[n])
            cdict[wdict[n]] += 1
    #On convertit le dictionnaire de comptage en une liste
    for elem, nbr in cdict.items() :
        listef.append(elem)
        listef.append(nbr)

    return listef
