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

    # success (0) if the game is valid and optimal
    # warning (1) if the card game is not optimal 
    # error (2) if the card set is invalid
    def verify(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Verification des cartes***")

        cards = self.read_file(cards_file)
        number_of_cards = len(cards)
        order = 0

        ### Test game validity ###
        result_2 = self.test_2(cards)
        if result_2[0] == 2:
            return 2
        else:
            order = result_2[1]
            result_3 = self.test_3(cards)

        if (result_2[0] + result_3) == 0:
            ### Test game optimality ###
            result_1 = self.test_1(order, number_of_cards)
            if result_1 == 1:
                return 1
            else:
                result_4 = self.test_4(order, cards)
                return result_4
        else:
            return 2

    def read_file(self, file_name):
        file = open(file_name, 'r')
        lines = list(map(lambda x: x.strip().replace('\n', ''), file.readlines()))
        file.close()
        #print(lines)
        cards = list(map(lambda x: self.format_line(x), lines))
        #print(cards)
        return cards

    def format_line(self, line):
        splitted_line = line.split(' ')
        result = ()
        for num in splitted_line:
            result += (int(num),)
        
        return result
            
    # test: the number of cards should be optimal
    # return 0 if the number of card is optimal
    # return 1 if the number of card is not optimal
    def test_1(self, order, number_of_cards):
        return int(number_of_cards != (order**2 + order + 1))

    # test: the number of symbols per card is the same for each card
    # return (0, order) the game if the symbols per card is the same for each card and the order is valid.
    # return (2, None) if the symbols per card is not the same for at least two card or the order is not valid.
    def test_2(self, cards):
        number_of_symbol = len(cards[0])
        for i in range(1, len(cards)):
            if len(cards[i]) != number_of_symbol:
                #print('test 2 failed: the number of symbols per card is the same for each card')
                return (2, None)
        #print()
        #print('test 2 passed: the number of symbols per card is the same for each card')
        return (0, (number_of_symbol - 1))

    # test: each pair of cards always shares one and only one symbol in common
    # return 0 if each pair of cards always shares one and only one symbol in common
    # return 2 if not
    def test_3(self, cards):
        for i in range(len(cards)):
            set_1 = set(cards[i])
            for j in range(i+1, len(cards)):
                set_2 = set(cards[j])
                if len(set_1.intersection(set_2)) != 1:
                    #print()
                    #print(f'test 3 failed -> {tuple(set_1)} and {tuple(set_2)} : no/too much symbols in common')
                    return 2
        #print()
        #print('test 3 passed: each pair of cards always shares one and only one symbol in common')
        return 0
        
    # test: the total number of symbols should be optimal
    # return 0 if the total number of symbols is optimal
    # return 1 if the total number of symbols is not optimal
    def test_4(self, order, cards):
        symbols = []
        for card in cards:
            for symbol in card:
                if symbol not in symbols:
                    symbols.append(symbol)
        #print(sorted(symbols))
        return int(len(symbols) != (order**2 + order + 1))
        

verificator = Verificator()
result  = verificator.verify(cards_file='cartes_test6.txt', verbose=True)
print()
print('Result ->' ,result)
