#----------------------------------------------------
# Dateiname:  log_gui.py 
# Gebrauch des Moduls logging bei Programmen mit GUI
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------
import logging
from tkinter import Tk, Button, Label, Entry, END


class App(object):
   def __init__(self):
      self.fenster = Tk()
      self.eingabe = Entry(self.fenster)
      self.label = Label(self.fenster, text="Bitte Name eingeben!")
      self.ok_button = Button(self.fenster, text ="OK",
                              command=self.verarbeiten)
      self.eingabe.pack()
      self.label.pack()
      self.ok_button.pack()
      self.fenster.mainloop()

   def verarbeiten(self):
      name = self.eingabe.get()
      logging.debug("Eingabe erfolgt. Name: " + name)
      self.eingabe.delete(0, END)
      
logging.basicConfig(filename="tmp/logging.txt", level=logging.DEBUG)
logging.debug("Start")
App()








                    
