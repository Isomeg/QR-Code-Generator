import qrcode
import os


dir_path = './QRCODES/'
count = 0

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=7,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=30,
        border=1,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save('./QRCODES/qr' + str(count).zfill(5) + '.jpg', 'JPEG')

for path in os.listdir(dir_path):

    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1

user_input = input("Enter the desire URL/PHONE NUMBER/EMAIL: ")
generate_qrcode(user_input)