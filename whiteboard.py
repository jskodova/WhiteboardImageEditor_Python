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

# Main Window
canvas = Canvas(root, width=1070, height=620, bg="white", cursor="hand2")
canvas.place(x=100, y=50)

canvas.bind("<Button-1>", locate_xy)

canvas.bind("<B1-Motion>", addline)

root.mainloop()
