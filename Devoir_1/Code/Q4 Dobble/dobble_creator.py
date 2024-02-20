# Nom, Matricule
# Nom, Matricule
import random
import os

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
        creator = Creator()
        # TODO

        allCards = creator.readFile("cartes.txt")
        pathToImgFolder = "Devoirs-IFT-2125/Devoir_1/Code/Q4 Dobble/images/dogs/"
        for i in range(0, len(allCards)):
            creator.createCard(pathToImgFolder, allCards[i], i+1)
        # a completer

    def readFile(self, card_file):
        nameFile = "Devoirs-IFT-2125/Devoir_1/Code/Q4 Dobble/" + card_file

        with open(nameFile, 'r') as file:
            lines = file.readlines()
            allCards = []
            for line in lines:
                row = line.strip().split(" ")
                allCards.append(row)
        return allCards

    def createCard(self, pathToImgFolder, elementTab, noCard):
        supportCard = Image.new("RGB", (900, 900), "white")
        folderName = "Devoirs-IFT-2125/Devoir_1/Code/Q4 Dobble/results"

        if not os.path.exists(folderName):
            os.makedirs(folderName)

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

        namefile = folderName + "/card" + str(noCard) + ".jpg"
        supportCard.save(namefile)

        # reading images from the "images" folder: "1.png2, "2.png", "3.png", ..., "<N>.png"
        # placement of images on visual cards, rotations appreciated
        # added border on visual cards
        # save cards in the “results” folder : "card1.jpg", "card2.jpg", "card3.jpg", ... "card<N>.jpg"


c = Creator()
c.make_cards("cartes.txt")
