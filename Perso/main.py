import time
from exercice2 import *
from exercice1 import *
from exercice3 import *
from exercice4 import *
#MENU :
choix = int(input('Entrez votre choix : 1 pour exercice 1, 2 pour exercice 2, etc... >>> '))

if choix == 1 :
    data = [1,1,1,2,3,10,10]

    print('liste comprimée :', comprime(data))
    print('liste comprimée et comptée:', compte(data))



elif choix == 2 :

    draw_figure()

elif choix == 3 :
    #Liste par défaut : [10, 18, 14, 20, 12, 16]
    print(minmaxmoy())

elif choix == 4 :
    t_start = time.time()

    #création d'une séquence d'adn aléatoire
    sequence_aleatoire = create_seq(100000)

    #affichage de sa composition :
    composition_ = composition(sequence_aleatoire)
    print('composition en nucléotides de la séquence : \n',composition_ ,'\n\n')

    #affichage du pourcentage en GC de la séquence :

    pourcentage_GC = pourcentGC(composition_)
    print('Pourcentage en GC de la séquence : \n', pourcentage_GC,'\n\n')

    #affichage de la température de fusion de Howley.
    temperature_fusion = temp_fusion_howley(composition_)
    print('Température de fusion de howley : \n',temperature_fusion,'\n\n')

    #Vérifications que deux séquences complémentaires le sont bien :
    print(est_complementaire('acgagag','ctctcgt'), '\n\n')

    #Transformation d'une séquence d'ADN en ARN (remplacement de 't' par des 'u')
    sequence_ADN = ''.join(sequence_aleatoire)
    print('Séquence en ADN :\n', sequence_ADN,'\n')
    sequence_ARN = ADN2ARN(sequence_ADN)
    print('Séquence en ARN :\n', sequence_ARN,'\n\n')

    #Traduction d'une séquence d'ARN en séquence nucléotidique
    sequence_aa = traduction(sequence_ARN)[0]
    print('Séquence en ARN traduite :\n', sequence_aa,'\n\n')

    #Localisation d'un motif simple, et affichage de l'index auquel il débute. On commence la recherche au début de la séquence.
    #Ici par exemple, on recherche la localisation du premier codon start de la séquence.
    print('Il y a un codon start à l\'indice :\n',localiser_motif_simple(sequence_ARN,'aug',0),'\n\n')

    #Localisation d'un motif contenant : A ou T, puis G ou C, 2 caractère quelconque, puis un A , puis 0 ou plusieurs T
    #Et affichage de son indice et du motif trouvé :
    match_infos = localiser_motif_RE(sequence_ADN, '[at][gc]..at*', 0)
    print('On trouve le motif < {} > à l\'indice < {} >\n\n'.format(match_infos[1], match_infos[0]))

    #Détermination de la signature d'une séquence d'ADN, ici on prend des mots de 3 lettres.
    signature_ = signature(sequence_ADN, 3)
    print('Signature de la séquence :\n', signature_, '\n\n')

    t_stop = time.time()
    print('Exécution de l\'exercice 4 en {}s'.format(t_stop-t_start))
