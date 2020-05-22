
def minmaxmoy(liste = [10, 18, 14, 20, 12, 16]) :

    """Prend en entrée une liste d'entiers dont elle donne en sortie le minimum, le maximum et la moyenne sous forme d'un tuple.
    Si aucun argument donné en entrée la liste traitée par défaut sera : [10, 18, 14, 20, 12, 16]"""


    min_ = min(liste)
    max_ = max(liste)
    moy_ = sum(liste)/len(liste)

    return(min_, max_, moy_)



if __name__ == '__main__' :
    print(minmaxmoy())
