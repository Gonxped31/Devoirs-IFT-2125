import os
from PIL import Image
from fpdf import FPDF

NO = 0
TABCOORD = [(3, 35), (107, 150), (107, 35), (3, 150)]
tab2 = [(60, 25), (60, 160)]
solo = [(60, 80)]


def convertir_image_en_page_pdf(image_path, pdf):
    global NO
    global TABCOORD

    image = Image.open(image_path)
    width, height = image.size
    page_width = pdf.w
    page_height = pdf.h

    const = (200)/(2*width)

    pdf.add_page()

    pdf.image(image_path, TABCOORD[0][0],
              TABCOORD[0][1], width*const, height*const)


def convertir_image_en_solo(image_path, pdf):
    global NO
    global solo

    image = Image.open(image_path)
    width, height = image.size
    page_width = pdf.w
    page_height = pdf.h

    const = (200)/(2*width)

    pdf.add_page()

    pdf.image(image_path, solo[0][0],
              solo[0][1], width*const, height*const)


def convertir_2(image_pathTab, pdf):
    global NO
    global TABCOORD

    image0 = Image.open(image_pathTab[0])
    image1 = Image.open(image_pathTab[1])
    image2 = Image.open(image_pathTab[2])
    image3 = Image.open(image_pathTab[3])

    width, height = image1.size

    const = (200)/(2*width)

    pdf.add_page()

    pdf.image(image_pathTab[0], TABCOORD[0][0],
              TABCOORD[0][1], width*const, height*const)
    pdf.image(image_pathTab[1], TABCOORD[1][0],
              TABCOORD[1][1], width*const, height*const)
    pdf.image(image_pathTab[2], TABCOORD[2][0],
              TABCOORD[2][1], width*const, height*const)
    pdf.image(image_pathTab[3], TABCOORD[3][0],
              TABCOORD[3][1], width*const, height*const)


def convertir_2parpage(image_pathTab, pdf):
    global NO
    global tab2

    image0 = Image.open(image_pathTab[0])
    image1 = Image.open(image_pathTab[1])

    width, height = image1.size

    const = (200)/(2*width)

    pdf.add_page()

    pdf.image(image_pathTab[0], tab2[0][0],
              tab2[0][1], width*const, height*const)
    pdf.image(image_pathTab[1], tab2[1][0],
              tab2[1][1], width*const, height*const)


# Définir le chemin du dossier contenant les images
dossier_images = "results"

# Définir le chemin de destination du PDF
fichier_pdf = "fichier.pdf"

# Créer une instance FPDF
pdf = FPDF()
TableauImage = []

# Parcourir les images du dossier
for image_fichier in os.listdir(dossier_images):
    # Ignorer les fichiers non-image
    if not image_fichier.lower().endswith((".png", ".jpg", ".jpeg")):
        continue

    # Convertir l'image en page PDF
    image_path = os.path.join(dossier_images, image_fichier)
    TableauImage.append(image_path)
    # convertir_image_en_page_pdf(image_path, pdf)

row = []
for img in TableauImage:
    row.append(img)
    if len(row) == 4:
        convertir_2(row, pdf)
        row = []
convertir_image_en_solo(TableauImage[56], pdf)


# Enregistrer le PDF
pdf.output(fichier_pdf)

print(f"Le PDF a été généré avec succès : {fichier_pdf}")
