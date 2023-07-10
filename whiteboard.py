from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageOps, ImageFilter, ImageTk
import os

root = Tk()
root.title("Whiteboard")
root.geometry("1200x700+150+50")
root.config(bg="#f2f3f5")
root.resizable(width=True, height=True)

current_x = 1
current_y = 1
color = "black"

def locate_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def addline(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), fill=color, width=get_current_value(), capstyle=ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def showcolor(newcolor):
    global color
    color = newcolor

def new_canvas():
    canvas.delete("all")
    display_palette()

def insert_image():
    global filename
    global f_img

    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image", filetypes=(("Png files", "*.png"), ("All files", "*.*")))
    original_image = Image.open(filename)

    resized_image = original_image.resize((int(original_image.width / 2), int(original_image.height / 2)), Image.ANTIALIAS)

    f_img = ImageTk.PhotoImage(resized_image)

    my_img = canvas.create_image(280, 100, image=f_img)
    root.bind("<B3-Motion>", my_callback)


def my_callback(event):
    global f_img
    my_img = canvas.create_image(event.x, event.y, image=f_img)

def apply_filter(filter):
    global filename

    image = Image.open(filename)

    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Contour":
        image = image.filter(ImageFilter.CONTOUR)
    elif filter == "Detail":
        image = image.filter(ImageFilter.DETAIL)
    elif filter == "Edge Enhance":
        image = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter == "Edge Enhance More":
        image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    elif filter == "Find Edges":
        image = image.filter(ImageFilter.FIND_EDGES)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Smooth More":
        image = image.filter(ImageFilter.SMOOTH_MORE)

    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")

# Components

# Icon
image_icon = PhotoImage(file="img/logo.png")
root.iconphoto(False, image_icon)

# Sidemenu
side_menu = PhotoImage(file="img/side_menu.png")
Label(root, image=side_menu, bg="#f2f3f5").place(x=10, y=20)

eraser = PhotoImage(file="img/eraser_1.png")
Button(root, image=eraser, bg="#f2f3f5", command=new_canvas).place(x=30, y=400)

add_image = PhotoImage(file="img/addimage_1.png")
Button(root, image=add_image, bg="white", command=insert_image).place(x=30, y=450)

# Color palette for sidemenu
colors = Canvas(root, width=37, height=300, bg="white", bd=0)
colors.place(x=30, y=60)

def display_palette():
    id = colors.create_rectangle(10, 10, 30, 30, fill="black")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("black"))

    id = colors.create_rectangle(10, 40, 30, 60, fill="gray")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("gray"))

    id = colors.create_rectangle(10, 70, 30, 90, fill="brown")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("brown"))


    id = colors.create_rectangle(10, 100, 30, 120, fill="red")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("red"))


    id = colors.create_rectangle(10, 130, 30, 150, fill="orange")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("orange"))


    id = colors.create_rectangle(10, 160, 30, 180, fill="yellow")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("yellow"))


    id = colors.create_rectangle(10, 190, 30, 210, fill="green")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("green"))


    id = colors.create_rectangle(10, 220, 30, 240, fill="blue")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("blue"))

    id = colors.create_rectangle(10, 250, 30, 270, fill="purple")
    colors.tag_bind(id, "<Button-1>", lambda x: showcolor("purple"))

display_palette()

# Size slider

current_value = tk.DoubleVar()
def get_current_value():
    return "{:.2f}".format(current_value.get())

def slider_change(event):
    value_label.configure(text=get_current_value())

size_label = tk.Label(root, text="Brush Size:")
size_label.place(x=100, y=20)

slider = ttk.Scale(root, from_=1, to=100, orient=tk.HORIZONTAL, variable=current_value, command=slider_change)
slider.place(x=220, y=15)

value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=180, y=20)

# Image filter
filter_label = tk.Label(root, text="Select filter:")
filter_label.place(x=350, y=20)

filter_combobox = ttk.Combobox(root, values=["None", "Blur", "Contour", "Detail", "Edge Enhance", "Edge Enhance More", "Emboss", "Find Edges", "Sharpen", "Smooth", "Smooth More"])
filter_combobox.place(x=430, y=20)

filter_combobox.bind("<<ComboboxSelected>>", lambda event: apply_filter(filter_combobox.get()))

# Main Window
canvas = Canvas(root, width=1070, height=620, bg="white", cursor="hand2")
canvas.place(x=100, y=50)

canvas.bind("<Button-1>", locate_xy)

canvas.bind("<B1-Motion>", addline)

root.mainloop()
