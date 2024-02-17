#Nom, Matricule
#Nom, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

#import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Verification des cartes***")

        cards = self.read_file(cards_file)
        
        # success (0) if the game is valid and optimal
        # warning (1) if the card game is not optimal 
        # error (2) if the card set is invalid

        ### Test game validity ###
        result_2 = self.test_2()
        result_3 = self.test_3()

        if (result_2 + result_3) == 0:
            ### Test game optimality ###

            result_1 = self.test_1()
            result_4 = self.test_4()
            result = result_1 + result_4

            return result if result != 2 else result - 1

        else:
            return 2

    
    
    def read_file(self, file_name):
        pass

    # test: the number of cards should be optimal
    # return 0 if the number of card is optimal
    # return 1 if the number of card is not optimal
    def test_1(self):
        pass

    # test: the number of symbols per card is the same for each card
    # return 0 if the symbols per card is the same for each card.
    # return 2 if the symbols per card is not the same for at least two card.
    def test_2(self):
        pass

    # test: each pair of cards always shares one and only one symbol in common
    # return 0 if each pair of cards always shares one and only one symbol in common
    # return 2 if not
    def test_3(self):
        pass

    # test: the total number of symbols should be optimal
    # return 0 if the total number of symbols is optimal
    # return 1 if the total number of symbols is not optimal
    def test_4(self):
        pass

