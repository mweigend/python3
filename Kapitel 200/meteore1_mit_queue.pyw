#----------------------------------------------------
# Dateiname:  meteore1_mit_queue.pyw
# Fallende Meteore (Threads) mit threadsicherer Schlange
# Kap. 20
# Michael Weigend 5.1.2010
#----------------------------------------------------


from tkinter import Tk, Canvas, PhotoImage
from threading import Thread
from time import sleep
from random import randint
from queue import Queue

class Weltraum(object): 
  def __init__(self):
    self.fenster = Tk()                                  
    self.canvas = Canvas(self.fenster, width='10c',
                         height='7c', bg='black')      
    self.canvas.pack()
    m1 = PhotoImage(file='metgross.gif')                                    
    m2 = PhotoImage(file='metklein.gif')
    self.q = Queue()                                        
    for bild in [m1, m2, m2, m1, m2, m1, m2]:               
        id_nr = self.canvas.create_image(50, -50, image=bild)
        Meteor(queue=self.q, id_nr=id_nr)          
    Mover(weltraum=self.canvas, queue=self.q)
    self.fenster.mainloop()
    
class Mover(Thread):
    # Ein Objekt dieser Klasse 
    def __init__(self, weltraum=None, queue=None):
      Thread.__init__(self)
      self.weltraum = weltraum
      self.queue = queue
      self.start()

    def run(self):
      while True:
        id_nr, x, y = self.queue.get() 
        self.weltraum.coords(id_nr, x, y)
      

class Meteor(Thread):                                  
  def __init__(self, queue=None, id_nr=0):
    Thread.__init__(self)                              
    self.queue = queue                  
    self.id = id_nr
    self.__neustart()
    self.start()                                       

  def __neustart(self):                                
     self.x = randint(0, 250)
     self.y = - randint(30, 100)
     self.vx = randint(-2, +2)
     self.vy = randint (1, 3)

  def run(self):
    while True:                                       
        sleep(0.02)
        self.x += self.vx
        self.y += self.vy
        self.queue.put((self.id, self.x, self.y))    
        if self.y > 300:   
               self.__neustart()
               
        
w = Weltraum()










                    
