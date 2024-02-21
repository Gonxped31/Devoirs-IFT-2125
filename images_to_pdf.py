from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image
import os

def add_images_to_pdf(image_folder, output_pdf):
    # Define page size and margins
    page_width, page_height = letter
    print(page_width, page_height)
    margin = 0  # 1 inch
    image_width = 300#(page_width - 3 * margin) / 2
    image_height = 300#(page_height - 3 * margin) / 2

    # Initialize PDF
    c = canvas.Canvas(output_pdf, pagesize=letter)

    # Read images from folder
    images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()  # Sort images to maintain order

    for index, image_name in enumerate(images):
        if index % 4 == 0 and index != 0:
            c.showPage()  # Create a new page after every 4 images
        
        # Calculate image position
        x = margin + (index % 2) * (image_width + margin)
        y = page_height - margin - image_height - ((index % 4) // 2) * (image_height + margin)
        
        # Open and resize image
        with Image.open(os.path.join(image_folder, image_name)) as img:
            img.thumbnail((image_width, image_height))
            img_path = f"temp_{index}.jpg"
            img.save(img_path)
            
            # Add image to PDF
            c.drawImage(img_path, x, y, image_width, image_height)
            os.remove(img_path)  # Remove temporary resized image

    c.save()

# Example usage
image_folder = 'C:\\Users\\Samir\\Documents\\GitHub\\Devoirs-IFT-2125\\Devoir_1\\Code\\Q4 Dobble\\my_results'
output_pdf = 'output.pdf'
add_images_to_pdf(image_folder, output_pdf)
