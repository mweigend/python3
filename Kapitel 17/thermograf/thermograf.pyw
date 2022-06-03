#----------------------------------------------------
# Dateiname: thermograf.pyw
# Darstellung der Temperatur als Säulendiagramm

# Python 3  mitp Verlag
# Kap. 17
# Michael Weigend 5.6.2019
#----------------------------------------------------


from tkinter import *
class Thermometer(object):
  def __init__(self):
    self.fenster = Tk()
    self.t = StringVar()
    self.c = Canvas(self.fenster,width='6.5c', height='5.2c')
    hintergrund = PhotoImage(
        file='himmel.gif')                            #1
    self.c.create_image(0,0,image=hintergrund, anchor=NW)   
    self.c.pack()
    self.__initButton()                               #2
    self.__initAnzeige()
    self.__initEingabe()   
    self.fenster.mainloop()

  def __initButton(self):
    self.icon = PhotoImage(
        file = 'thermoicon.gif')      
    self.ok=Button(image=self.icon,width='0.8c', height='0.9c',
                   command=self.__aktualisiere)
    self.c.create_window('1c', '4.5c', 
                          window=self.ok)             #3

  def __initAnzeige(self):
    for grad in [-20,-10,0,10,20,30,40,50]:           #4
      self.c.create_text('5c',140-2*grad, text=str(grad))
    self.aussen = self.c.create_rectangle('5.5c',20,'5.8c',190,
                                      fill='white')   #5
    self.innen = self.c.create_rectangle('5.5c',140,'5.8c',190,
                                      fill='blue')

  def __initEingabe(self):
    self.c.create_text('0.3c','3.4c',text='Temperatur: ',
                      font=('Arial', 14), anchor=W)
    self.c.create_window('3.5c','3.4c',
            window=Entry(width=3, textvariable=self.t))


  def __aktualisiere(self):
    t = int(self.t.get())
    if -20 < t <55:                                   #6
        self.c.coords( self.innen, '5.5c', 140-2*t, '5.8c', 190)


t = Thermometer()


                    
