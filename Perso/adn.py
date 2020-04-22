import time
import random
def create_seq(length):
    nucleotides = ['a','t','g','c']
    seq = ''
    for i in range(length):
        chooser = random.randint(0,3)
        seq += nucleotides[chooser]


    return seq

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


def ADN2ARN(seq):
    return seq.replace('t', 'u')

def traduction(seq) :

    code_genetique = {'uuu': 'F', 'ucu': 'S', 'uau': 'Y', 'ugu': 'C','uuc': 'F', 'ucc': 'S', 'uac': 'Y', 'ugc': 'C','uua': 'L', 'uca': 'S', 'uaa': '*', 'uga': '*','uug': 'L', 'ucg': 'S', 'uag': '*', 'ugg': 'W','cuu': 'L', 'ccu': 'P', 'cau': 'H', 'cgu': 'R','cuc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R','cua': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R','cug': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R','auu': 'I', 'acu': 'T', 'aau': 'N', 'agu': 'S','auc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S','aua': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R','aug': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R','guu': 'V', 'gcu': 'A', 'gau': 'D', 'ggu': 'G','guc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G','gua': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G','gug': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G',}
    aa = ''
    cadre = int(input('Entrez le cadre de lecture :0, 1 ou 2 :  '))

    if cadre != 0 and cadre != 1 and cadre != 2 :
        raise ValueError

    seq = ADN2ARN(seq)
    for i in range(cadre, len(seq)-len(seq)%3, 3) :
        aa += code_genetique[seq[i:i+3]]


    return (aa, len(aa))




if __name__ == '__main__' :
    a = time.time()
    seq = create_seq(3000000)
    trad = traduction(seq)
    print(trad[0],'\nlen :\n', trad[1])
    b = time.time()
    print(b-a)
    # seq = 'atgagtgaacgtctgagcattaccccgctggggccgtatatcggcgca'
    # print(pourcentGC(composition(seq)))
    # print(temp_fusion_howley(composition(seq)))
    #
    # print(est_complementaire('acg', 'aca'))
