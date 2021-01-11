import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from main import main_func
from tkinter import filedialog

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a whatsapp voice message ", font="Raleway")

instructions.grid(columnspan=3, column=0, row=1)

def open_file():
    browse_text.set("loading...")
    # input = filedialog.askopenfile(initialdir="/")
    input  = filedialog.askopenfile(parent=root, title="Choose a file", filetype=[("ogg file", "*.ogg")])
    file = input.name

    main_func(file)

    browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

root.mainloop()
