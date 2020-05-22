import time
import random
import re
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

    composition_ = {'a' : 0, 't' : 0, 'c' : 0, 'g' : 0}

    for lettre in composition_ :
        composition_[lettre] = sequence_adn.count(lettre)

    return composition_



def pourcentGC(composition_) :
    """Prend en entrée le dictionnaire donnant la composition d'une séquence en chaque nucléotide et renvoie le pourcentage de GC sur le total."""

    somme = sum(composition_.values())
    pourcent = ((composition_['g'] + composition_['c']) / somme) * 100

    return pourcent



def temp_fusion_howley(composition_) :
    """Prend en entrée le dictionnaire donnant la composition d'une séquence, et retourne la température de fusion de Howley"""

    total = sum(composition_.values())
    pourcent = pourcentGC(composition_)

    return 67.5 + (0.34*pourcent)-(395/total)



def est_complementaire(seq1, seq2):
    """Prend en entrée deux séquences, et les compare, renvoie une booléen, True si elles sont complémentaires, False sinon"""

    #--------------------------#
    #On remplace chaque nucléotide par son nucléotide complémentaire, il faut prendre une valeur temporaire pour une lettre sur deux d'un couple
    seq2 = seq2.replace('a','x')
    seq2 = seq2.replace('t', 'a')
    seq2 = seq2.replace('x', 't')

    seq2 = seq2.replace('g', 'x')
    seq2 = seq2.replace('c', 'g')
    seq2 = seq2.replace('x', 'c')
    #---------------------------#

    #On inverse le sens de la sequence, pour que les deux soient bien dans le même sens
    seq2 = list(seq2)
    seq2.reverse()
    seq2 = ''.join(seq2)

    #Et on compare
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



def localiser_motif_simple(seq, motif, position) :
    index_motif = seq[position:].index(motif)
    return index_motif

def localiser_motif_RE(seq, motif, position) :
    match = re.search(motif,seq[position:])
    #retourne l'indice de début du motif, ainsi que le motif trouvé
    try :
        return(match.start(), match.group())
    except AttributeError :
        return('xxx', 'xxx')

def signature(sequence,taille) :
    motifs = []
    signature_ = {}
    for i in range(0,len(sequence)-taille,taille) :
        motifs.append(sequence[i:i+taille])
    motifs.sort()
    for mot in motifs :
        signature_[mot] = signature_.get(mot, 0) + 1
    return signature_
 
