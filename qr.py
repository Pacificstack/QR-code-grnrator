import qrcode
import image
qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5,

)

data = "https://youtu.be/DjlmltN0pNk?list=RDMMDjlmltN0pNk"



qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black,", back_color = "White")
img.save("test.png")