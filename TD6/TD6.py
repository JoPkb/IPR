def intervertir(dic):
    listValueToKey = []
    listKeyToValue = []
    dicFinal = {}

    for item in dic.items() :
        listKeyToValue.append(item[0])
        listValueToKey.append(item[1])

    for newValue, newKey in zip(listKeyToValue, listValueToKey) :
        dicFinal[newKey] = newValue


    return dicFinal


def compteSeq(seq) :
    lettres = {'A' : 0, 'T' : 0, 'C' : 0, 'G' : 0}
    for nt in seq :
        lettres[nt] = lettres.get(nt, 0) + 1

    return lettres


def compteCodon(seq) :
    codons = {}
    for i in range(0, len(seq) - len(seq) % 3, 3):
        codons[seq[i:i+3]] = codons.get(seq[i:i+3],0) + 1

    return codons


if __name__ == '__main__' :

    choix = int(input("1 pour l'exo 1, 2 pour le 2, 3 pour le 3 :\n"))

    if choix == 1 :
        dic = {'computer' : 'ordinateur', 'screen' : 'écran', 'mouse' : 'souris', 'keyboard' : 'clavier'}
        print(dic)
        print(intervertir(dic))
    elif choix == 2 :
        seq = input("sequence :    ")
        for objet in compteSeq(seq).items() :
            print(objet[0], ":", objet[1])
    elif choix == 3 :
        seq = input("sequence :    ")
        for objet in compteCodon(seq).items() :
            print(objet[0], ":", objet[1])
