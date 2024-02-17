#Nom, Matricule
#Nom, Matricule

# cette classe sert a créer les cartes du jeu dans le fichier cartes.txt
# this class is used to create the game cards in the cartes.txt file

import random # pour le melange des symboles sur chaque carte # for mixing symbols on each card
import re

class Generator():
    def __init__(self, order):
        self.order = order

    def generate(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Generation des cartes***")

        matrix, horizon = self.create_matrix()

        self.write(matrix, horizon, cards_file)
            
    def write(self, matrix, horizon, file_name):
        order = len(horizon) - 1
        content = ''
        for line in matrix:
            for elem in line:
                string = re.sub(r'[(),]', '', str(elem))
                content += f'{string}\n'
        
        for elem in horizon:
            string = re.sub(r'[(),]', '', str(elem))
            content += f'{string}\n'

        file = open(file_name, 'w')
        file.write(content)
        file.close()

    def transpose(self, matrix): 
        return list(map(lambda i: list(map(lambda x : x[i], matrix)), list(range(len(matrix[0])))))

    def horizontal_lines(self, matrix, horizon, position, images):
        order = self.order
        for i in range(order):
            image = images.pop()
            for j in range(order):
                matrix[i][j] += (image,)
            horizon[position] += (image,)
        return matrix, images

    def oblique_lines(self, matrix, horizon, images):
        order = self.order
        for jump in range(1, order):
            k = 0
            for _ in range(order):
                image = images.pop()
                for j in range(order):
                    index = k % order
                    matrix[j][index] += (image,)
                    k += jump
                k += jump
                horizon[jump+1] += (image,)            
        return matrix, horizon, images
    
    def link_horizon_elemets(self, horizon, image):
        for i in range(len(horizon)):
            horizon[i] += (image,)
        return horizon
    
    def create_matrix(self):
        order = self.order
        num_of_pic = order**2 + order + 1
        random_images = random.sample(range(1, num_of_pic + 1), num_of_pic)
        matrix = [[()] * order for _ in range(order)]
        horizon = [() * order for _ in range(order+1)]
        matrix, random_images = self.horizontal_lines(matrix, horizon, 0, random_images)
        matrix, random_images = self.horizontal_lines(self.transpose(matrix), horizon, 1, random_images)
        matrix, horizon, images = self.oblique_lines(self.transpose(matrix), horizon, random_images)

        return matrix, self.link_horizon_elemets(horizon, images.pop())
    
generator = Generator(5)
generator.generate(cards_file='cartes.txt', verbose=True)