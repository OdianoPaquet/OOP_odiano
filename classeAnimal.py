class Animal :
    #attributs
    def __init__(self,poids,taille):
        self.set_poids(poids)
        self.set_taille(taille)

    #methodes
    def se_deplacer(*args):
        '''print le type de déplacement'''
        pass

    def __str__(self):
        return f"le poids de l'animal est : {self.__poids} et sa taille : {self.__taille}"

    #getter (lecture)
    def get_poids(self):
        return self.__poids
    def get_taille(self):
        return self.__taille

    #setter (ecriture)
    def set_poids(self, poids):
        if poids > 0 : 
            self.__poids = poids
        else : 
            print("ValueError")
    def set_taille(self, taille):
        self.__taille = taille


