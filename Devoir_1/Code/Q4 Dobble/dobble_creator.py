'''# Nom, Matricule
# Nom, Matricule
import random

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

# from PIL import Image
# import os
# import math
# import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

import os
import glob
from PIL import Image


class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def make_cards(self, cards_file="cartes.txt", verbose=False):
        if verbose:
            print("***Creation des cartes visuelles***")

        # TODO
        # a completer
            
        cards = self.read_cards(cards_file)

        # lecture des images à partir du dossier "images" : "1.png2, "2.png", "3.png", ... "<N>.png"
        # placement des images sur les cartes visuelles, rotations apreciees
        # ajout de la bordure sur les cartes visuelles
        # sauvegarde des cartes dans le dossier "results" : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"

        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"
            
    # supportCard.show()
    def read_cards(self, file_name):
        with open(file_name , 'r') as file:
            lines = file.readlines()
            allCards = []
            for line in lines:
                row = line.strip().split(" ")
                allCards.append(row)
        return allCards


    def createCard(pathToImgFolder, elementTab, noCard):
        supportCard = Image.new("RGB", (900, 900), "white")

        for i in range(0, len(elementTab)):
            imgPlace = pathToImgFolder + \
                str(elementTab[i]) + ".png"
            img = Image.open(imgPlace)
            imgSize = img.size
            const = (200/(max(imgSize)))
            img = img.resize((int(const*imgSize[0]), int(const*imgSize[1])))
            img = img.rotate(random.randint(0, 360), expand=True, fillcolor="white",
                            resample=Image.BICUBIC)

            supportCard.paste(img, ((i//3)*300, (i % 3)*300))

        namefile = "image_resultat" + str(noCard) + ".jpg"
        supportCard.save(namefile)

    pathToImgFolder = "Devoirs-IFT-2125/Devoir_1/Code/Q4 Dobble/images/MangaImg/"


    for i in range(0, len(allCards)):
        print(allCards[i])
        createCard(pathToImgFolder, allCards[i], i+1)'''





#Nom, Matricule
#Nom, Matricule

# cette classe sert a créer les cartes visuelles du jeu dans le dossier "results"
# this class is used to create the game visual cards in the "results" folder

from PIL import Image, ImageOps
import os
import math
import random

# info :
# https://pillow.readthedocs.io/en/stable/reference/Image.html

class Creator():
    def __init__(self, pic_size=300, border_size=10):
        self.pic_size = pic_size
        self.border_size = border_size

    def make_cards(self, cards_file = "cartes.txt", verbose = False):
        if verbose :
            print("***Creation des cartes visuelles***")

        relative_path = 'my_results'

        cards, order = self.parse_cards(cards_file)
        images = self.get_images()
        images_per_card = order + 1
        images_per_line = 3

        for i in range(len(cards)):
            card = self.make_card(images, cards[i], images_per_card, images_per_line)
            if os.path.exists(relative_path):
                card.save(f'.\\{relative_path}\\card{i+1}.jpg')
            else:
                os.mkdir('results')
                card.save(f'.\\{relative_path}\\card{i+1}.jpg')
            

        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"

    def make_card(self, images, numeric_card, images_per_card, images_per_line):
        list_card = list(numeric_card)
        new_width = self.pic_size * images_per_line
        new_height = self.pic_size * math.ceil(images_per_card / images_per_line)

        card = Image.new('RGB', (new_width, new_height), 'white')

        b,x,y = 0, 0, 0
        for _ in range(images_per_line):
            for j in range(images_per_line):
                if list_card:
                    im = images[list_card.pop(0)-1]
                    imgSize = im.size
                    const = (200/max(imgSize))
                    im = im.resize((int(const*imgSize[0]),int(const*imgSize[1])))
                    im = im.rotate(random.randint(0,360), expand=True, fillcolor="white", resample=Image.BICUBIC)
                    card.paste(im, (x + j*10, y + b))
                    x += self.pic_size
            b = j
            x = 0
            y += self.pic_size
        
        card = ImageOps.expand(card, border=self.border_size, fill='black')
        return card

    def get_images(self):
        images = []
        for file in os.listdir('images\\neural_confusion'):
            if file.endswith('.png'):
                im = Image.open(f'images\\{file}')
                im = im.resize((self.pic_size, self.pic_size))
                images.append(im)

        return images

    def parse_cards(self, file_name):
        file = open(file_name, 'r')
        lines = list(map(lambda x: x.strip().replace('\n', ''), file.readlines()))
        file.close()
        cards = list(map(lambda x: self.format_line(x), lines))
        random.shuffle(cards)
        order = (len(cards[0]) - 1)
        return cards, order

    def format_line(self, line):
        splitted_line = line.split(' ')
        result = ()
        for num in splitted_line:
            result += (int(num),)
        list_res = list(result)
        random.shuffle(list_res)
        return tuple(list_res)

creator = Creator()
creator.make_cards()