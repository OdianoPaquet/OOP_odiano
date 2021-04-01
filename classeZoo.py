#import classe mère
from classeAnimal import *

class Zoo :

    #instanciation avec un constructeur
    def __init__(self,liste_Animal) :
        self.set_Animaux(liste_Animal)

    #méthodes
    def ajout(self,newAnimal) :
        '''ajouter un animal avec un annimal du type "Animal"'''
        if isinstance(newAnimal, Animal) == True :
            self.__listAnimaux.append(newAnimal) 
        else:
            print("l'ajout n'est pas un animal du type Animal")

    def __add__(self,other):
        '''ajouter une liste type "zoo" à la suite d'une liste du type "zoo"'''
        if isinstance(other, Zoo) == True:
            Total_listAmniaux = self.__listAnimaux + other.__listAnimaux
            return Zoo(Total_listAmniaux)
        else:
            print("Votre liste n'est pas de type Zoo")
    
    def affichage_listAnimal(self):
        '''affiche la liste de type "zoo"'''
        for elm in self.__listAnimaux:
            print(elm)
    
    #getteur (lecture)
    def get_listAnimaux(self):
        '''le type des éléments de la liste'''
        return self.__listAnimaux

    #setteur (ecriture)
    def set_Animaux(self, liste_Animal):
        '''crée une liste d'annimaux'''
        self.__listAnimaux = list()
        for elm in liste_Animal:
            if isinstance(elm, Animal) == True:
                self.__listAnimaux.append(elm)
            else:
                print("False")
    



