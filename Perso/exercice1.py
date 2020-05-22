

def comprime(data) :

    liste_copie = list(data)
    i = 0
    while i < len(liste_copie)-1  :
        if liste_copie[i] == liste_copie[i+1] :
            del(liste_copie[i+1])
        else :
            i+=1
    return liste_copie



def prime(data):
    data = list(data)
    i = 1
    var = data[0]
    compteur = 1
    while i < len(data):

        if data[i] == var:
            compteur+=1
            del(data[i])
        else:
            data.insert(i, compteur)
            var = data[i+1]
            compteur = 1

            i+=2
    data.append(compteur)
    return data
if __name__ == '__main__' :
    print(prime([1,1,1,1,2,3,3,10,10,11,11,11]))
