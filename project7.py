# install lib needed
# create a function that collects text and lowercase 
# convert to a qrcode
# save it as image
# run the function

import qrcode
import sys

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qeimg.png')

def main():
    ask = input("Please enter the link you want QR code of: ")
    generate_qrcode(ask)
    sys.exit()

if __name__ == '__main__':
    main()
