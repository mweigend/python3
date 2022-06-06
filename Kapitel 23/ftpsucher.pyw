#----------------------------------------------------
# Dateiname: ftpsucher.pyw
# Suchroboter fuer FTP-Server.
#
# Objektorientierte Programmierung mit Python
# Kap. 23
# Michael Weigend 23.10.09
#----------------------------------------------------

# ftpsucher.pyw
from tkinter import*
from threading import *
import ftplib
class Archie(object):
  def __init__(self):
    self.fenster = Tk()
    self.fenster.title('Mini-Archie')
    self.suchwort = StringVar()                       #1
    self.server = StringVar()
    self.oben = Frame(self.fenster)                   #2
    self.oben.pack(padx=5, pady=5)
    Label(self.oben, text='Server: ').pack(side=LEFT)
    Entry(self.oben, width=30,
          textvariable=self.server).pack(side=LEFT)
    Label(self.oben,
          text='  Suchwort: ').pack(side=LEFT)
    Entry(self.oben,
          textvariable=self.suchwort).pack(side=LEFT)
    Button(self.oben, text=' Suche! ',
           command=self.suche).pack(side=LEFT, padx=5)
    self.text = Text(self.fenster)
    self.text.pack(padx=5, pady=5)
    self.fenster.mainloop()

  def suche(self):                                    #3
      Robot(self)                                     #4

class  Robot(Thread):
  def __init__(self, oberfläche):
        Thread.__init__(self)                         #5
        self.ob = oberfläche                         #6
        self.start()                                  #7

  def run(self):
    self.ob.text.delete('1.0', END)                   #8
    self.ob.text.insert(END, 'Suchergebnis:\n\n')
    self.server = self.ob.server.get()
    self.suchwort = self.ob.suchwort.get()
    try:
      self.ftp = ftplib.FTP(self.server, 'anonymous', 
                        'ich@meinedomain.de')         #9
      self.schlange = ['/']                          #10
      self.breitensuche()
      self.ftp.quit()                                #11
      self.ob.text.insert(END,'--- Ende der Suche ---')
    except:                                          #12
      self.ob.text.insert(END,'Kein anonymes Login möglich.')

  def breitensuche(self):                            #13
    while self.schlange:
      self.pfad = self.schlange[0]
      del self.schlange[0]
      if len(self.schlange)<20:                      #14
        try:
          self.ftp.cwd(self.pfad)
          verz = []
          self.ftp.retrlines('LIST', verz.append)
          unterverzeichnisse, dateien = self.untersuche(verz)
          self.schlange.extend(unterverzeichnisse)
          for d in dateien:
            self.ob.text.insert(END,d+'\n')
        except: pass

  def untersuche(self, verzeichnis):                         #15
    liste1 = []
    liste2 = []
    for z in verzeichnis:
      name = z.split()[-1]
      if z[0] == 'd':
        if name not in ['.', '..']:   
          liste1.append(self.pfad + name +'/')
      elif self.suchwort in name:
                liste2.append(self.pfad + name)
    return liste1, liste2

a = Archie()


                    
