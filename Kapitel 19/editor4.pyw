#----------------------------------------------------
# Dateiname:  editor4.pyw
# Einfacher Texteditor mit Rollbalken und Menue
# Python 3  mitp Verlag
# Kap. 19
# Michael Weigend 7.6.2019
#----------------------------------------------------

from tkinter import (END, filedialog, Menu, messagebox, 
                RIGHT, Scrollbar, StringVar, Text, Tk, WORD, Y)

class Editor(object):
  def __init__ (self):
    self.fenster = Tk()
    self.fenster.title("Texteditor")
    self.scrollbar = Scrollbar(self.fenster)  
    self.scrollbar.pack(side=RIGHT, fill=Y) 
    self.text= Text(self.fenster,
                    wrap=WORD, font=('Arial', 10),
                    yscrollcommand=self.scrollbar.set) 
    self.text.pack(expand=1)
    self.scrollbar.config(command=self.text.yview)  
    self.__addMenueleiste()
    self.__addDateimenue()                            #1
    self.__addFormatmenue()  
    self.fenster.mainloop()
    
  def __addMenueleiste(self):
    self.menueleiste=Menu(self.fenster)               
    self.fenster.configure (menu=self.menueleiste)     

  def __addFormatmenue(self):
    self.formatmenue= Menu(master=self.menueleiste)    
    self.schrifttyp=StringVar()
    self.menueleiste.add_cascade(label="Schrifttyp",
                            menu=self.formatmenue)     
    self.formatmenue.add_radiobutton(label='Arial',
             variable=self.schrifttyp, value='Arial',
             command = self.formatieren)               
    self.formatmenue.add_radiobutton(label='Courier',
             variable=self.schrifttyp, value='Courier',
             command = self.formatieren)
    self.formatmenue.add_radiobutton(label='Times',
             variable=self.schrifttyp, value='Times',
             command = self.formatieren)



  def __addDateimenue(self):
    self.dateimenue=Menu(self.menueleiste)            #2
    self.dateimenue.add_command(label="Laden",
                            command = self.laden)     #3  
    self.dateimenue.add_command(label="Speichern unter",
                            command = self.speichern)
    self.dateimenue.add_separator()                   #4
    self.dateimenue.add_command(label='Ende',
                            command=self.beenden)
    self.menueleiste.add_cascade(label="Datei",
                            menu=self.dateimenue)     #5

  def formatieren(self):
    schrifttyp=self.schrifttyp.get()                  
    self.text.config(font=(schrifttyp,10))
    
  def laden (self):
    self.datei = filedialog.askopenfile()           #6
    self.text.delete(1.0, END)                        #7
    if self.datei:                           
            self.text.insert(1.0, self.datei.read())  #8
            self.datei.close()

  def speichern (self):
    self.datei = filedialog.asksaveasfile()         #9
    if self.datei:
        self.datei.write(self.text.get(1.0, END) )   #10
        self.datei.close()

  def beenden (self):                                #11
    if messagebox.askyesno('Beenden',
           'Wollen Sie wirklich das Programm beenden?'):
        self.fenster.destroy()

editor = Editor()






                    
