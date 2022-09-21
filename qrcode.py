from turtle import fillcolor
import qrcode


def generate_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fillcolor="black", back_color="white")
    img.save("qrimg.png")


generate_qrcode("Code with me bro")
