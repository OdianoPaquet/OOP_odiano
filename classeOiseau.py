#import classe mère
from classeAnimal import Animal

class Oiseau(Animal):

    #attributs
    def __init__(self,poids,taille,altitude_max) :
        self.set_altitude_max(altitude_max)
        super().__init__(poids,taille)

    #methodes
    def se_deplacer(*args):
        '''print le type de déplacement'''
        print("je vole")

    #getteur
    def get_altitude_max(self):
        return self.__altitude_max

    #setteur
    def set_altitude_max(self, altitude_max):
        self.__altitude_max = altitude_max
