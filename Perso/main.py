from Formes import *
import turtle as t
from modiflist import *
from minmaxmoy import *
from adn import *
#MENU :
choix = int(input('Entrez votre choix : 1 pour exercice 1, 2 pour exercice 2, etc... >>> '))

if choix == 1 :
    data = [1,1,1,2,3,10,10]

    print('liste comprimée :', comprime(data))
    print('liste comprimée et comptée:', compte(data))



elif choix == 2 :

    draw_figure()

elif choix == 3 :

    print(minmaxmoy())

elif choix == 4 :
    print(composition('AAAACCCGGGTTT'))
