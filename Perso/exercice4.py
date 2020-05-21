import time
import random
def create_seq(length):
    """Crée une séquence d'adn aléatoire, d'une longueur donnée."""

    nucleotides = ['a','t','g','c']
    seq = []
    for i in range(length) :
        seq.append(random.choice(nucleotides))
    #seq = ''.join(seq)
    return seq


def composition(sequence_adn) :
    """Prend en entrée soit une chaîne de caractères, soit une liste de nucléotides, et en compte les occurences.
    Retourne un dictionnaire"""

    composition = {'a' : 0, 't' : 0, 'c' : 0, 'g' : 0}

    for lettre in composition :
        composition[lettre] = sequence_adn.count(lettre)

    return composition



def pourcentGC(composition) :
    """Prend en entrée le dictionnaire donnant la composition d'une séquence en chaque nucléotide et renvoie le pourcentage de GC sur le total."""

    pourcent = ((composition['g'] + composition['c']) / sum(composition.values())) * 100

    return pourcent



def temp_fusion_howley(composition) :
    """Prend en entrée le dictionnaire donnant la composition d'une séquence, et retourne la température de fusion de Howley"""

    total = sum(composition.values())
    pourcent = pourcentGC(composition)

    return 67.5 + (0.34*pourcent)-(395/total)



def est_complementaire(seq1, seq2):
    """Prend en entrée deux séquences, et les compare, renvoie une booléen, True si elles sont complémentaires, False sinon"""

    seq2 = list(seq2)
    seq2.reverse()
    seq2 = ''.join(seq2)

    if seq1 == seq2 :
        return True
    else :
        return False


def ADN2ARN(seq):
    """Remplace les 't' d'une séquence sous forme d'un chaîne de caractères par 'u'"""
    return seq.replace('t', 'u')

def traduction(seq) :
    "Prend une séquence d'ARN en entrée sous forme d'une chaîne de caractères, et la traduit en séquence peptidique"""
    code_genetique = {'uuu': 'F', 'ucu': 'S', 'uau': 'Y', 'ugu': 'C','uuc': 'F', 'ucc': 'S', 'uac': 'Y', 'ugc': 'C','uua': 'L', 'uca': 'S', 'uaa': '*', 'uga': '*','uug': 'L', 'ucg': 'S', 'uag': '*', 'ugg': 'W','cuu': 'L', 'ccu': 'P', 'cau': 'H', 'cgu': 'R','cuc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R','cua': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R','cug': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R','auu': 'I', 'acu': 'T', 'aau': 'N', 'agu': 'S','auc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S','aua': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R','aug': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R','guu': 'V', 'gcu': 'A', 'gau': 'D', 'ggu': 'G','guc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G','gua': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G','gug': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G',}
    aa = ''
    cadre = 0

    #if cadre != 0 and cadre != 1 and cadre != 2 :
        #raise ValueError


    for i in range(cadre, len(seq)-len(seq)%3, 3) :
        aa += code_genetique[seq[i:i+3]]


    return (aa,len(aa))



def localiser_motif_simple(seq, motif) :
    index = [0]
    occurence = 0
    for i in range(len(seq)) :
        index.append(seq(motif)[index[:-1]].index)





if __name__ == '__main__' :
    a = time.time()
    #seq = 'uuuauguugcugugagccaugcuaguauaa'
    seq = create_seq(1000)
    trad = traduction(seq)
    print(trad[0],'\nlen :\n', trad[1])

    print(find_ORF(trad[0]),'\n')
    b = time.time()
    print(b-a)

    seq = 'atgagtgaacgtctgagcattaccccgctggggccgtatatcggcgca'
    print(pourcentGC(composition(seq)))
    print(temp_fusion_howley(composition(seq)))

    print(est_complementaire('acg', 'aca'))
