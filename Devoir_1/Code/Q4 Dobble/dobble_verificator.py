# Nom, Matricule
# Nom, Matricule

# cette classe sert a verifier la validite de l'ensemble des cartes du jeu dans le fichier cartes.txt
# this class is used to check the validity  of the game cards set in the cartes.txt file

# doit retourner 0 si tout est correct, 1 si le jeu n'est pas optimal selon l'ordre et 2 si le jeu n'est pas valide
# should return 0 if everything is correct, 1 if the game set is not optimal according to the order and 2 if the game set is invalid

# import os.path

class Verificator():
    def __init__(self):
        pass

    def verify(self, cards_file="Test.txt", verbose=False):
        if verbose:
            print("***Verification des cartes***")
        # TODO
        nameFile = "Devoirs-IFT-2125/Devoir_1/Code/Q4 Dobble/" + cards_file

        with open(nameFile, 'r') as file:
            lines = file.readlines()
            allCards = []
            for line in lines:
                row = line.strip().split(" ")
                allCards.append(row)

        testValue = 2

       # the supposed order is the number of element on a card minus one
        order = len(allCards[0]) - 1

        # test: the number of symbols per card is the same for each card
        numberOfElementInTheFirstCard = len(allCards[0])
        for card in allCards:
            if (len(card) != numberOfElementInTheFirstCard):
                return testValue

        # test: each pair of cards always shares one and only one symbol in common
        for i in range(0, len(allCards)):
            for j in range(i+1, len(allCards)):
                set1 = set(allCards[i])
                set2 = set(allCards[j])
                if (len(set1.intersection(set2)) == 1):
                    continue
                else:
                    return testValue

        testValue = 1

        # test: the total number of symbols should be optimal
        elementsSet = []
        for card in allCards:
            for element in card:
                elementsSet.append(element)
        elementsSet = list(set(elementsSet))
        if (len(elementsSet) != (order**(2) + order + 1)):
            return testValue

        # test: the number of cards should be optimal
        # Total of card is len(allCards)
        if (len(allCards) != (order**(2) + order + 1)):
            return testValue

        # test: the number of symbols per card is order+1 each card
        for card in allCards:
            if (len(card) != order+1):
                # len(card) is the number of element for each card
                return testValue

        testValue = 0

        # success (0) if the game is valid and optimal
        # warning (1) if the card game is not optimal
        # error (2) if the card set is invalid

        return testValue


v = Verificator()
print(v.verify("cartes.txt", False))
