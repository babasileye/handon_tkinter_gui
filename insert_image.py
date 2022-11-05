from tkinter import *
import numpy as np
from PIL import Image,ImageTk

def insert_image(image_path):
    """
    """
    gui=Tk(className='Image Insertion')
    gui.configure(bg='black')
    img=Image.open(image_path)
    img_shape=np.shape(img)
    canvas=Canvas(gui, bg="dark grey",height=img_shape[0],width=img_shape[1])
    canvas.pack(side=LEFT)
    photo=ImageTk.PhotoImage(img)
    canvas.create_image(img_shape[1]//2,img_shape[0]//2, image=photo, anchor=CENTER)
    text=Label(gui,text="Hello world",fg="red")
    text.pack()
    button=Button(gui,text="quit",command=gui.destroy)
    button.pack(side=BOTTOM,padx=3,pady=3)
    gui.mainloop()
