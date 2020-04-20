
def composition(sequence_adn) :
    composition = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}

    for nucleotide in sequence_adn :
        composition[nucleotide] += 1

    return composition


def pourcentGC(composition) :
    total = 0
    liste_valeurs = [a for a in composition.values()]

    for valeur in liste_valeurs :
        total += valeur

    pourcent = ((composition['G'] + composition['C']) / total) * 100

    return pourcent


def temp_fusion_howley(composition) :
    total = 0
    liste_valeurs = [a for a in composition.values()]
    pourcent = pourcentGC(composition)

    for valeur in liste_valeurs :
        total += valeur

    return 67.5 + (0.34*pourcent)-(395/total)







if __name__ == '__main__' :
    print(temp_fusion_howley(composition('AAAACCCGGGGTTTT')))
