#----------------------------------------------------
# Dateiname:  stegano_pic_min.pyw
# 
# Python 3  mitp Verlag
# Kap. 17
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import *

class App:
    def __init__(self):
        self.filename="manchester_2.ppm"
        self.window = Tk()
        self.pic = PhotoImage(file= self.filename)
        self.c = Canvas(self.window, width=self.pic.width(),
                        height=self.pic.height())
        self.c.pack()       
        self.c.create_image(0, 0, anchor=NW, image=self.pic)
        self.ExtractButton=Button(master=self.window, text="Wörter finden", command=self.extract)
        self.ExtractButton.pack()
        self.window.mainloop()  
     
    def extract(self):
        w = self.pic.width()
        h = self.pic.height()
        color = self.pic.get(0,0)
        pixels = [(x, y) for x in range(w) for y in range(h)]
        for (x, y) in pixels:
            if self.pic.get(x, y) != color:
                self.pic.put("white", to=(x, y))
            else:
                self.pic.put("{black black} {black black}", to=(x, y))
                
App()



