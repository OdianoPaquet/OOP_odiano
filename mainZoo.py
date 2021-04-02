#import des fichier Python
from classeAnimal import *
from classeOiseau import *
from classeSerpent import *
from classeZoo import *

animal1 = Animal(poids = 50, taille = 2)
Anaconda = Serpent(poids = 5, taille = 10)
Pigeon = Oiseau(poids = 1, taille = 1, altitude_max = 10)
Aigle = Oiseau(poids = 2, taille = 2, altitude_max = 500)

#changement du poid d'un animal
print("animal1 :")
print(animal1.get_poids())
animal1.set_poids(60)
print(animal1.get_poids())

#changement du poid d'un serpent
print("Anaconda :")
print(Anaconda.get_poids())
Anaconda.set_poids(35)
print(Anaconda.get_poids())

#changement du poids/altitude max d'un oiseau 
print("Pigeon :")
print(Pigeon.get_poids())
Pigeon.set_poids(60)
print(Pigeon.get_poids())
Pigeon.set_altitude_max(600)
print(Pigeon.get_altitude_max())

#affichage des action d'un oiseau et d'un serpent
print("l'anaconda: ")
Anaconda.se_deplacer()
print("le pigeon : ")
Pigeon.se_deplacer()

#cas d'une erreur (poids négatif)
print("Anaconda poids négatif :")
print(Anaconda.get_poids())
Anaconda.set_poids(-5)
print(Anaconda.get_poids())

#test affichage de toute les caractériqtiques d'un animal
print("caractéristiques d'un animal : ")
ani = Animal(10,60)
print(str(ani))

#création d'une liste d'animaux
x = animal1
y = Anaconda
z = Pigeon
falseAnimal = "Maison"
g = Aigle

mammifere = [x,falseAnimal,y]
listeOiseau = [z,g]

#Ajout d'un animal dans une liste zooMammifere
zooMammifere = Zoo(liste_Animal=mammifere)
zooMammifere.ajout(z)
print(zooMammifere.get_listAnimaux())

zooMammifere.ajout(falseAnimal)
print(zooMammifere.get_listAnimaux())
zooMammifere.affichage_listAnimal()

#Ajout d'une liste (non zoo) dans la liste zoo principal
print("\nAjout d'une liste dans la liste pricipale")
zooMammifere.__add__(listeOiseau)
zooMammifere.affichage_listAnimal()

#Ajout d'une liste zoo dans la liste zoo principal
print("\nAjout d'une liste dans la liste pricipale")
zooOiseau = Zoo(listeOiseau)
zooCombinee = zooMammifere + zooOiseau
zooCombinee.affichage_listAnimal()
zooiajsi = Zoo(listeOiseau)

