from PIL import Image, ImageFont, ImageDraw
import textwrap

def decode_image(file_location="./encoded_mario_PNG55.png"):
    encoded_image = Image.open(file_location)
    red_channel = encoded_image.split()[0]

    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]

    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()

    for i in range(x_size):
        for j in range(y_size):
            if bin(red_channel.getpixel((i, j)))[-1] == '0':
                pixels[i, j] = (255, 255, 255)
            else:
                pixels[i, j] = (0, 0, 0)

    decoded_image.save("./decoded_mario_PNG55.png")

def write_text(text_to_write, image_size):
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    margin = offset = 10
    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text

def encode_image(text_to_encode, template_image="./mario_PNG55.png"):
    template_image = Image.open(template_image)
    x_size = template_image.size[0]
    y_size = template_image.size[1]

    R = template_image.split()[0]
    G = template_image.split()[1]
    B = template_image.split()[2]

    img = write_text(text_to_encode, template_image.size)
    bw_encode = img.convert('1')
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()
    for i in range(x_size):
        for j in range(y_size):
            pixel = bin(bw_encode.getpixel((i, j)))
            R_pixel = bin(R.getpixel((i, j)))

            if pixel[-1] == '1':
                R_pixel = R_pixel[:-1] + '1'

            else:
                R_pixel = R_pixel[:-1] + '0'
            pixels[i, j] = (int(R_pixel, 2), G.getpixel((i, j)), B.getpixel((i, j)))

    encoded_image.save("./encoded_mario_PNG55.png")

if __name__ == '__main__':
    print("Encoding the image...")
    encode_image("ZASZUFROWANA WIADOMOSC")
    print("Decoding the image...")
    decode_image()

