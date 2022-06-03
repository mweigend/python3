#----------------------------------------------------
# Dateiname:  programm_editor.pyw
# Einfacher Programmeditor mit zwei Fenstern: Editor und Ausgabe
# Python 3  mitp Verlag
# Kap. 19
# Michael Weigend 7.6.2019
#----------------------------------------------------
#programm_editor.pyw
import sys                                           #1

from tkinter import (END, Menu, messagebox, 
                     mainloop, Text, Tk, WORD)

class Ausgabe(object):
  def __init__ (self):
    self.fenster = Tk()                               
    self.fenster.geometry('200x150+10+10')           #2
    self.fenster.title('Ausgabe')  
    self.text= Text(self.fenster,
                    wrap=WORD, font=('Courier', 10)) 
    self.text.pack(expand=1)
     
  def write(self, s):                                #3
    self.text.insert(END, s)

class Editor(object):
  def __init__ (self):
    self.fenster = Tk()                             
    self.fenster.geometry('250x150+240+10')          #4
    self.fenster.title('Programmeditor')
    self.text= Text(self.fenster,
                    wrap=WORD, font=('Courier', 10)) 
    self.text.pack(expand=1)
    
    self.menueleiste=Menu(self.fenster)               
    self.fenster.configure (menu=self.menueleiste)    
    self.menue= Menu(master=self.menueleiste)    
    self.menueleiste.add_cascade(label='Befehle',
                            menu=self.menue)
    self.menue.add_command(label='Programm starten',
                        command = self.starten)
    self.menue.add_command(label='Ende',
                            command=self.beenden)  
    self.ausgabe = Ausgabe()
    sys.stdout = sys.stderr = self.ausgabe

     
  def starten(self):
    programmtext =  self.text.get(1.0, END)
    exec(programmtext)
 
  def beenden (self):                                
    if messagebox.askyesno('Beenden',
           'Wollen Sie wirklich das Programm beenden?'):
        self.ausgabe.fenster.destroy()               #5
        self.fenster.destroy()

editor = Editor()
mainloop()                                           #6








                    
