import qrcode

def generate_qr_code(data, file_name="qrcode.png", color_scheme="black_on_white"):
    color_schemes = {
        "black_on_white": {"fill": "black", "back": "white"},
        "blue_on_yellow": {"fill": "blue", "back": "yellow"},
        "green_on_pink": {"fill": "green", "back": "pink"},
        "purple_on_orange": {"fill": "purple", "back": "orange"},
        "red_on_cyan": {"fill": "red", "back": "cyan"},
    }

    if color_scheme not in color_schemes:
        print("Invalid color scheme. Using default black_on_white.")
        color_scheme = "black_on_white"

    scheme = color_schemes[color_scheme]

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=scheme["fill"], back_color=scheme["back"])
    img.save(file_name)
    print(f"QR Code saved as {file_name} with color scheme: {color_scheme}")


data = input("Enter the URL to encode: ")

print("Choose a color scheme:")
print("1. Black on White")
print("2. Blue on Yellow")
print("3. Green on Pink")
print("4. Purple on Orange")
print("5. Red on Cyan")

choice = input("Enter a number (1-5) for color scheme: ")

color_mapping = {
        "1": "black_on_white",
        "2": "blue_on_yellow",
        "3": "green_on_pink",
        "4": "purple_on_orange",
        "5": "red_on_cyan",
    }

color = color_mapping.get(choice, "black_on_white")

generate_qr_code(data, color_scheme=color)
