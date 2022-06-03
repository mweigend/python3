#----------------------------------------------------
# Dateiname:  editor3.pyw
# Einfacher Texteditor mit Rollbalken und Menue
# Objektorientierte Programmierung mit Python
# Kap. 19
# Michael Weigend 7.10.09
#----------------------------------------------------

from tkinter import *
class Editor(object):    
  def __init__ (self):
    self.fenster = Tk()
    self.fenster.title("Texteditor Nr. 1")
    self.scrollbar=Scrollbar(self.fenster)  
    self.scrollbar.pack(side =RIGHT,fill =Y) 
    self.text= Text(self.fenster,
                    wrap=WORD, font=('Arial', 10),
                    yscrollcommand=self.scrollbar.set) 
    self.text.pack(expand=1)
    self.scrollbar.config(command=self.text.yview)  

    self.__addMenueleiste()
    self.__addFormatmenue()   
    self.fenster.mainloop()

  def __addMenueleiste(self):
    self.menueleiste=Menu(self.fenster)               #1
    self.fenster.configure (menu=self.menueleiste)    #2 

  def __addFormatmenue(self):
    self.formatmenue= Menu(master=self.menueleiste)   #3
    self.schrifttyp=StringVar()
    self.menueleiste.add_cascade(label="Schrifttyp",
                            menu=self.formatmenue)    #4
    self.formatmenue.add_radiobutton(label='Arial',
             variable=self.schrifttyp, value='Arial',
             command = self.formatieren)              #5
    self.formatmenue.add_radiobutton(label='Courier',
             variable=self.schrifttyp, value='Courier',
             command = self.formatieren)
    self.formatmenue.add_radiobutton(label='Times',
             variable=self.schrifttyp, value='Times',
             command = self.formatieren)

  def formatieren(self):
    schrifttyp=self.schrifttyp.get()                  #6
    self.text.config(font=(schrifttyp,10))

editor = Editor()





                    
