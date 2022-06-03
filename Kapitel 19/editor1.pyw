#----------------------------------------------------
# Dateiname:  editor1.pyw
# Ganz einfacher Texteditor
# Objektorientierte Programmierung mit Python
# Kap. 19
# Michael Weigend 9.10.09
#----------------------------------------------------

from tkinter import *
class Editor(object):    
  def __init__ (self):
    self.fenster = Tk()
    self.fenster.title("Texteditor Nr. 1")  
    self.text = Text(self.fenster, 
                    width=40, height=20,
                    wrap=WORD,                     #1
                    font=('Arial', 10))     
    self.text.pack()                               
    self.fenster.mainloop()

editor = Editor()






                    
