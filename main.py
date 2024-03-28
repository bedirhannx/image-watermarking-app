import PIL.Image
from PIL import Image, ImageDraw, ImageFont
from tkinter import *


def add_watermark():
    image_path = image_input.get()
    watermark = watermark_input.get()

    img = PIL.Image.open(image_path)
    width, heigth = img.size

    draw = ImageDraw.Draw(img)
    text = watermark

    font = ImageFont.load_default()
    _, _, txtwidth, txtheight = draw.textbbox((0, 0), text=text, font=font)

    margin = 10
    x = width - txtwidth - margin
    y = heigth - txtheight - margin

    draw.text((x, y), text, font=font)
    img.show()

    img.save('C:/Users/bedir/Downloads/watermark.jpg')


# UI
window = Tk()
window.title("Add a watermark to image")
window.config(padx=20, pady=20)

image_input = Entry(width=75)
image_input.grid(column=1, row=0)

image_label = Label(text="File Path:")
image_label.grid(column=0, row=0)

watermark_input = Entry(width=75)
watermark_input.grid(column=1, row=1)

watermark_text = Label(text="Text:")
watermark_text.grid(column=0, row=1)

add_watermark_button = Button(text="Add watermark", command=add_watermark, width=63)
add_watermark_button.grid(column=1, row=2)

window.mainloop()
