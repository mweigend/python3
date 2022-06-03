#----------------------------------------------------
# Dateiname:  stegano.pyw
# In einem Foto ist Text versteckt
# Python 3  mitp Verlag
# Kap. 17
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import *
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.filename="manchester_2.ppm"
        self.window = Tk()
        self.img = Image.open(self.filename)
        self.pic = ImageTk.PhotoImage(self.img)
        self.c = Canvas(self.window, width=self.pic.width(),
                        height=self.pic.height())
        self.c.pack()       
        self.img_id = self.c.create_image(0, 0, anchor=NW, image=self.pic)
        self.ExtractButton=Button(master=self.window, text="Wörter finden", command=self.extract)
        self.ExtractButton.pack()
        self.window.mainloop()  
     
    def extract(self):
        w, h = self.img.size
        color = self.img.getpixel((0,0))
        pixels = [(x, y) for x in range(w) for y in range(h)]
        for x, y in pixels:
            if self.img.getpixel((x, y)) != color:
                self.img.putpixel((x, y), (255, 255, 255)) #weiß
            else:
                self.img.putpixel((x, y), (0, 0, 0))    #schwarz
        self.pic = ImageTk.PhotoImage(self.img)
        self.c.create_image(0, 0, anchor=NW, image=self.pic)
stegano = App()



