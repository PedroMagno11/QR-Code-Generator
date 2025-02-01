import qrcode
import sys
import os
import platform

def generate(link, filename = "qr_code.png"):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3
    )

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Detecta o sistema operacional
    system = platform.system()

    if system == "Windows":
        desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
    elif system == "Linux" or system == "Darwin":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    else:
        raise Exception(f"Sistema operacional não suportado: {platform.system}")

    # Salva a imagem
    img_path = os.path.join(desktop_path, filename)
    img.save(img_path)
    print(f"QR Code gerado: {img_path}")

# Obtém o link enviado pela linha de comando
if len(sys.argv) > 1:
    link = sys.argv[1]
    filename = sys.argv[2] if len(sys.argv) > 2 else "qr_code.png"

    # Garante que o nome do arquivo termine com .png
    if not filename.lower().endswith(".png"):
        filename += ".png"

    generate(link, filename)
else:
    print("Uso: python main.py <link> [nome do arquivo.png]")
