import time
def composition(sequence_adn) :
    a = time.time()
    composition = {'a' : 0, 't' : 0, 'c' : 0, 'g' : 0}

    for lettre in composition :
        composition[lettre] = sequence_adn.count(lettre)

    b = time.time()

    return b-a


def pourcentGC(composition) :

    pourcent = ((composition['g'] + composition['c']) / sum(composition.values())) * 100

    return pourcent


def temp_fusion_howley(composition) :

    total = sum(composition.values())
    pourcent = pourcentGC(composition)

    return 67.5 + (0.34*pourcent)-(395/total)


def est_complementaire(seq1, seq2):
    seq2 = list(seq2)
    seq2.reverse()
    seq2 = ''.join(seq2)

    if seq1 == seq2 :
        return True
    else :
        return False





if __name__ == '__main__' :
    print(composition('atgagtgaacgtctgagcattaccccgctggggccgtatatcggcgca'))
    # seq = 'atgagtgaacgtctgagcattaccccgctggggccgtatatcggcgca'
    # print(pourcentGC(composition(seq)))
    # print(temp_fusion_howley(composition(seq)))
    #
    # print(est_complementaire('acg', 'aca'))
