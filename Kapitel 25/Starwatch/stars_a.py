#----------------------------------------------------
# Dateiname:  stars.py
# Modul mit Klassen Star und Sky zur Reprsesentation
# eines Sternenhimmels
# 
# Python 3
# Kap. 25
# Michael Weigend 08.06.2019
#----------------------------------------------------
# stars.py
class Star(object):                                     
  """ modelliert einen Stern"""
  def __init__(self, dot):
        self.__dots = [dot]                           #1

  def integrate (self, dot):                          #2
    x,y = dot
    r = 2
    for (x0, y0)  in self.__dots:
        if (x0-r <= x <= x0+r) and (y0-r <= y <= y0+r): 
          self.__dots.append(dot)                     #3
          return True                               
    return False                                      #4

class Sky(object):
  """ Modelliert einen Sternenhimmel"""
  def __init__ (self, image):
    self.threshold = 200                              #5
    self.image = image
    lightdots = self.__search()
    self.__createStars(lightdots)

  def __brightness (self, pixel):                   #6
    a, b, c = pixel
    return int(a) + int(b) + int (c)


  def __createStars(self, lightdots):
    self.__stars = []
    for p in lightdots:                               #7
      self.__integrate(p)
      
  def __integrate (self, lightdot):                   #8
      for star in self.__stars:
        if star.integrate(lightdot): return  
      self.__stars.append (Star(lightdot))            #9 
  
  def __search (self):                                #10
    dotlist =[] 
    for x in range(self.image.width()):
      for y in range(self.image.height()):
        brightness = self.__brightness(self.image.get(x, y))
        if brightness > self.threshold:
          dotlist.append((x,y))
    return dotlist           

  def count(self):
    return len(self.__stars)

# Testen 
if __name__ == "__main__":                            #11
    import profile, tkinter 
    window = tkinter.Tk()                             #12             
    image = tkinter.PhotoImage(file="bilder/wagen.gif" )                   
    profile.run("stars = Sky(image)")                 #13

