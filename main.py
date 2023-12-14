import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from tkinter import ttk

# Main TKinter settings
parent = tk.Tk()
parent.title("Watermark Generator")
parent.config(padx=100, pady=50)

img = img2 = None

def watermark():
    if img and img2:
        logo_image = Image.open(img2).convert("RGBA")
        background_image = Image.open(img).convert("RGBA")
        logo_width, logo_height = logo_image.size
        background_width, background_height = background_image.size
        if logo_width > background_width or logo_height > background_height:
            logo_image.thumbnail((background_width, background_height))

        logo_x = 0
        logo_y = 0

        background_image.paste(logo_image, (logo_x, logo_y), mask=logo_image)
        background_image.show()

def open_file():
    global img
    img = filedialog.askopenfilename(initialdir='Users/picture')

def open_filelogo():
    global img2
    img2 = filedialog.askopenfilename(initialdir='Users/picture')


button1 = ttk.Button(parent, text="Select Image", command=open_file)
button1.pack()

button2 = ttk.Button(parent, text="Select Image Watermark", command=open_filelogo)
button2.pack()

button3 = ttk.Button(parent, text="Show Watermark Image", command=watermark)
button3.pack()

parent.mainloop()
