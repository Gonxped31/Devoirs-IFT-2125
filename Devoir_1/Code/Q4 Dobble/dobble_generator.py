# Nom, Matricule
# Nom, Matricule

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random  # pour le melange des symboles sur chaque carte # for mixing symbols on each card


class Generator():
    def __init__(self, order=7):
        self.order = order

    def generate(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Generation des cartes***")

        # TODO
        # random mixing of symbols on the cards,
        # so as not to have repetitions of symbols on the same places on the cards
        generator_instance = Generator()

        # length of the dico n+1
        dictLetter = generator_instance.createDict(self.order)

        cardTab = []
        # initialisation of card of the matrix
        for i in range(0, self.order):
            row = []
            for j in range(0, self.order):
                row.append([])
            cardTab.append(row)

        # card in the matrix : n^2
        for key in dictLetter:
            for i in range(1, self.order+2):
                generator_instance.fufillCard(self, cardTab, key, i)

        # card out of the matrix : n+1
        restOfTheCard = []
        for i in range(1, self.order+2):
            cardI = []
            for key in dictLetter:
                cardI.append(generator_instance.codeToLetter(self, key, i))
            cardI.append(generator_instance.codeToLetter(self, "$", 1))
            restOfTheCard.append(cardI)

        # All cards :
        allCards = []
        for row in cardTab:
            for row1 in row:
                allCards.append(row1)
        for row in restOfTheCard:
            allCards.append(row)

        # TODO
        # writing cards in the cards_file file
        nameFile = "Devoirs-IFT-2125/Devoir_1/Code/Q4 Dobble/" + cards_file
        with open(nameFile, 'w') as fichier:
            bigString = ""
            for row in allCards:
                string = ""
                for img in row:
                    string += str(img) + " "
                bigString += string + "\n"
            fichier.write(bigString)

        # TODO
    @staticmethod
    def createDict(length):
        generalDictLetter = {
            "A": 0, "B": 1, "C": 2, "D": 3,
            "E": 4, "F": 5, "G": 6, "H": 7,
            "I": 8, "J": 9, "K": 10, "L": 11,
            "M": 12, "N": 13, "O": 14, "P": 15,
            "Q": 16, "R": 17, "S": 18, "T": 19,
            "U": 20, "V": 21, "W": 22, "X": 23,
            "Y": 24, "Z": 25, "AA": 26, "AB": 27,
            "AC": 28, "AD": 29, "AE": 30, "AF": 31
        }
        if (length >= 31 or length <= 0):
            return generalDictLetter

        newDict = {}

        while (True):
            for key in generalDictLetter:
                newDict[key] = generalDictLetter[key]
                if (len(newDict) == length):
                    return newDict

    @staticmethod
    def codeToLetter(self, letter, number):
        dictLetter = Generator.createDict(self.order)
        length = self.order
        if (letter not in dictLetter):
            return (length+1)*(length) + number
        return (length+1)*(dictLetter[letter]) + number

    @staticmethod
    def initialOrdered(self, letter, number):
        length = self.order
        dictLetter = Generator.createDict(self.order)
        if (number == 1):
            number = length

        if (number == (length+1)):
            return ((length-(dictLetter[letter])*(length-1)) % length, 0)
        else:
            return (0, (length-((dictLetter[letter])*(number-1))) % length)

    @staticmethod
    def FindingCorrespondingCard(self, letter, number):

        allPlaces = [Generator.initialOrdered(self, letter, number)]

        if (number == (self.order+1)):
            while (len(allPlaces) < self.order):
                a, b = allPlaces[len(allPlaces)-1]
                allPlaces.append((a, (b+1) % self.order))
        else:
            while (len(allPlaces) < self.order):
                a, b = allPlaces[len(allPlaces)-1]
                allPlaces.append(
                    ((a+1) % self.order, (b+(number-1)) % self.order))
        return allPlaces

    @staticmethod
    def fufillCard(self, cardTab, letter, number):
        noImg = Generator.codeToLetter(self, letter, number)
        allPlaces = Generator.FindingCorrespondingCard(self, letter, number)
        for couple in allPlaces:
            a, b = couple
            cardTab[a][b].append(noImg)


g = Generator()
g.generate("Test.txt", True)
