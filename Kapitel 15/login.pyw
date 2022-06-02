#----------------------------------------------------
# Dateiname: login.pyw
#
# Python 3, mitp Verlag
# Kap. 15
# Michael Weigend 5.6.2019
#----------------------------------------------------
 
from tkinter import *
class Login(object):
  def __init__(self):
    self.user = {'Tim':'krone2', 'Mick':'selters$',
                'Laura':'prater00', 'Kai':'pasta$1'}  #1
    self.fenster = Tk()
    self.ausgabe = Label(self.fenster, width=20, height=2)
    self.name = Entry(self.fenster)                          #2
    self.passwort = Entry(self.fenster, show='*')            #3
    self.loginButton = Button(self.fenster,
                      text='login', command=self.login)
    self.name.pack(padx=10, pady=10)                  #4
    self.passwort.pack(pady=10)
    self.loginButton.pack(pady=10)
    self.ausgabe.pack()
    self.fenster.mainloop()

  def login(self):
    name = self.name.get()                                    #5
    if name in self.user.keys():
      if self.passwort.get() == self.user[name]:
        self.ausgabe.config(text='Herzlich Willkommen, '+name+'!')
      else: self.ausgabe.config(text='Passwort falsch!')
    else: self.ausgabe.config(text='User unbekannt!')
    self.name.config(text='')                         #6
    self.name.config(text='')

l = Login()


 



