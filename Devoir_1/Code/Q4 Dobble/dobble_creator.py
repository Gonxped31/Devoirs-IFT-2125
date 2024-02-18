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

        cards, order = self.parse_cards(cards_file)
        images = self.get_images()
        images_per_card = order + 1
        images_per_line = 3

        for i in range(len(cards)):
            card = self.make_card(images, cards[i], images_per_card, images_per_line)
            card.save(f'.\\my_results\\carte{i+1}.png')

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
                    im = ImageOps.expand(im, border=self.border_size, fill='black')
                    card.paste(im, (x + j*10, y + b))
                    x += self.pic_size
            b = j
            x = 0
            y += self.pic_size

        return card

    def get_images(self):
        images = []
        for file in os.listdir('images'):
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
