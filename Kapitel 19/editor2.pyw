#----------------------------------------------------
# Dateiname:  editor2.pyw
# Einfacher Texteditor mit Rollbalken
# Objektorientierte Programmierung mit Python
# Kap. 19
# Michael Weigend 9.10.09
#----------------------------------------------------


from tkinter import *
class Editor(object):   
  def __init__ (self):
    self.fenster = Tk()
    self.fenster.title("Texteditor Nr. 1")
    self.scrollbar = Scrollbar(self.fenster)          #1
    self.scrollbar.pack(side =RIGHT, fill=Y)          #2
    self.text = Text(self.fenster,
                   width=24, height=10,
                   wrap=WORD, font=('Arial', 10),
                   yscrollcommand=self.scrollbar.set) #3   
    self.text.pack()
    self.scrollbar.config(command=self.text.yview)    #4 
    self.fenster.mainloop()

editor = Editor()







                    
