
import qrcode

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = "https://www.linkedin.com/in/pranav-maity-52276126b/"

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    back_color="white"
)

img.save("test.png")

print("QR Code generated successfully!")