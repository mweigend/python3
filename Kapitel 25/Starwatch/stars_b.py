#----------------------------------------------------
# Dateiname:  stars_b.py
# Modul mit erweiterten Klassen zur Repräsentation
# eines Sternenhimmels
# Lösung Aufgabe 3
# 
# Python 3
# Kap. 25
# Michael Weigend 08.06.2019
#----------------------------------------------------
import math
class Star(object):
  """ modelliert einen Stern"""
  m0 = 1             # Magnitude des Referenzsterns
  s0 = 0.00001       # Lichtenergie des Referenzsterns
  def __init__(self, dot):
        self.__dots = [dot]

  def integrate (self, dot):                           
    x,y = dot
    r = 2
    for (x0, y0)  in self.__dots:
        if (x0-r <= x <= x0+r) and (y0-r <= y <= y0+r): 
          self.__dots.append(dot)                     
          return True                               
    return False                                      

  def contains (self, dot):
      return dot in self.__dots
  
  def getBrightness(self):
      return len(self.__dots)    

class Sky(object):
  """ Modelliert einen Sternenhimmel"""
  def __init__ (self, image):
    self.threshold = 200                              
    self.image = image
    lightdots = self.__search()
    self.__createStars(lightdots)

  def __brightness (self, pixel):                     
    a, b, c = pixel
    return int(a) + int(b) + int (c)

  def __createStars(self, lightdots):
    self.__stars = []
    for p in lightdots:                    
      self.__integrate(p)
      
  def __integrate (self, lightdot):                 
      for star in self.__stars:
        if star.integrate(lightdot): return  
      self.__stars.append (Star(lightdot))         
  
  def __search (self):                                
    dotlist =[] 
    for x in range(self.image.width()):
      for y in range(self.image.height()):
        brightness = self.__brightness(self.image.get(x, y))
        if brightness > self.threshold:
          dotlist.append((x,y))
    return dotlist           

  def count(self):
    return len(self.__stars)

  def getStar(self, dot):
      for star in self.__stars:
          if star.contains(dot):
              return star


# Testen

def test(sky):
    import random
    for i in range(1000):
        position = (random.randint(0, 100),
                    random.randint(0,100))
        sky.getStar(position)   

if __name__ == "__main__":                             
    import profile, tkinter
    window = tkinter.Tk()                                           
    image = tkinter.PhotoImage(file="bilder/gr_wagen.gif" ) 
    sky = Sky(image)           
    profile.run("test(sky)")              

