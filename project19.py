# resize an image using pillow

from PIL import Image

def resize_image(size1, size2)

    open = Image.open('...') # name of the picture you wanna open

    print(f'Current size: {open.size}')

    resize = open.resize((size1, size2))

    resize.save("...") # name of new file


size1 = input("Enter length: ")
size2 = input("Enter width: ")
resize_image(size1, size2)