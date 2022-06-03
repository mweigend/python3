#----------------------------------------------------
# Dateiname:  editor5.pyw
# Einfacher Texteditor mit Textbausteinen
# Objektorientierte Programmierung mit Python
# Kap. 19 Lösung 2
# Michael Weigend 29.5.21
#----------------------------------------------------

from tkinter import (END, Menu, messagebox, filedialog,
                     mainloop, Text, Tk, WORD, INSERT,
                     RIGHT, Scrollbar, Y, StringVar)

class Editor(object):
  def __init__ (self):
    self.fenster = Tk()
    self.fenster.title("Texteditor")
    self.scrollbar=Scrollbar(self.fenster)  
    self.scrollbar.pack(side =RIGHT,fill =Y) 
    self.text= Text(self.fenster,
                    wrap=WORD, font=('Arial', 10),
                    yscrollcommand=self.scrollbar.set) 
    self.text.pack(expand=1)
    self.scrollbar.config(command=self.text.yview)  
    self.__addMenueleiste()
    self.__addDateimenue()                             
    self.__addFormatmenue()
    self.__addTbmenue()                 # eingefügt
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
    self.dateimenue=Menu(self.menueleiste)             
    self.dateimenue.add_command(label="Laden",
                            command = self.laden)        
    self.dateimenue.add_command(label="Speichern unter",
                            command = self.speichern)
    self.dateimenue.add_separator()                    
    self.dateimenue.add_command(label='Ende',
                            command=self.beenden)
    self.menueleiste.add_cascade(label="Datei",
                            menu=self.dateimenue)      

  def __addTbmenue(self):
    self.tb = StringVar()                           # eingefügt  
    self.tbmenue = Menu(master=self.menueleiste)
    self.menueleiste.add_cascade(label='Textbausteine',
                            menu=self.tbmenue)  
    self.tbmenue.add_radiobutton(label='Rauch', 
            variable=self.tb,
            value='Zu beobachten war intensive Rauchentwicklung.',
            command=self.einfuegen)
    self.tbmenue.add_radiobutton(label='Glühen',
            variable=self.tb,
            value='Das Reaktionsgemisch glühte.',
            command=self.einfuegen)
    self.tbmenue.add_radiobutton(label='Gas',
            variable=self.tb,
            value='Es entstand ein Gas.',
            command=self.einfuegen)


  def formatieren(self):
    schrifttyp=self.schrifttyp.get()                  
    self.text.config(font=(schrifttyp,10))
    
  def laden (self):
    self.datei = filedialog.askopenfile()            
    self.text.delete(1.0, END)                        
    if self.datei:                           
            self.text.insert(1.0, self.datei.read())   

  def speichern (self):
    self.datei = filedialog.asksaveasfile()          
    if self.datei:
        self.datei.write(self.text.get(1.0, END) )    
        self.datei.close()

  def beenden (self):                                
    if messagebox.askyesno('Beenden',
           'Wollen Sie wirklich das Programm beenden?'):
        self.fenster.destroy()

  def einfuegen(self):                  # eingefuegt
      self.text.insert(INSERT,self.tb.get())


editor = Editor()






                    
