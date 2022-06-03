#----------------------------------------------------
# Dateiname:  stegano_pic_advanced.pyw
# 
# Python 3  mitp Verlag
# Kap. 17
# Michael Weigend 5.6.2019
#----------------------------------------------------
from tkinter import (Canvas, filedialog, Tk, Button, 
                     PhotoImage, NW)


class App:
    def __init__(self):
        self.filename="manchester_1.ppm"
        self.window = Tk()
        self.pic = PhotoImage(file= self.filename)
        self.c = Canvas(self.window, width=self.pic.width(),
                        height=self.pic.height())
        self.c.pack()       
        self.c.create_image(0, 0, anchor=NW, image=self.pic)
        self.LoadButton=Button(master=self.window, text="Laden", command=self.load)
        self.LoadButton.pack()
        self.ExtractButton=Button(master=self.window, text="Wörter finden", command=self.extract)
        self.ExtractButton.pack()
        self.window.mainloop()  

    def load(self):
        self.filename = filedialog.askopenfilename()
        self.pic = PhotoImage(file=self.filename)
        self.c.config(width=self.pic.width(), height=self.pic.height())
        self.c.create_image(0, 0, anchor ="nw", image=self.pic)
        

    def extract(self):
        w = self.pic.width()
        h = self.pic.height()
        colors = [self.pic.get(i,0) for i in [0, 1, 2, 3]]
        pixels = [(x, y) for x in range(w) for y in range(h)]
        for (x, y) in pixels:
            if self.pic.get(x, y) not in colors:
                self.pic.put("white", to=(x, y))
            else:
                self.pic.put("black", to=(x, y))
                

        

App()



