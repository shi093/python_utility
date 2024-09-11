!pip install qrcode

import qrcode
from google.colab import files

def generate_qr_code(link, filename):
    """Generates a QR code for the given link and saves it as filename."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    files.download(filename)

if __name__ == "__main__":
    website = input('Your website: ')
    qr_name = input('Your QR code name: ')
    #generate_qr_code("http://www.njyoungartists.org/", "njyaa.jpg")
    generate_qr_code(website, qr_name+".jpg")
    print(f"QR code saved successfully!!")
