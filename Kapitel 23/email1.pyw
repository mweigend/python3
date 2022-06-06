#----------------------------------------------------
# Dateiname: email1.pyw
# Einfacher E-Mail-Client, der über SMTP Mails verschickt.
# Passwort, Mail-Server und eigene E-Mail-Adresse muessen
# noch angepasst werden.
#
# Objektorientierte Programmierung mit Python
# Kap. 23
# Michael Weigend 23.3.2019
#----------------------------------------------------

import smtplib
from tkinter import *

SCHABLONE = '''From: {}
To: {}
Subject: {}
MIME-Version: 1.0
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

{}
'''                                                     #1
FROM = 'name@domaine.de'                                #2
PASSWORD = 'geheim'
SERVER = 'smtp.servicd.de'
PORT = 465

class SMTPClient:  
  def __init__ (self):
    window = Tk()
    window.title('SMTP-Client Nr. 1')
    Label(window, text="Adresse: ").grid(row=0, column=0)  
    self.to = Entry(window, width=40)
    self.to.grid(row=0, column=1, pady=5) 
    Label(window, text='Betrifft: ').grid(row=1, column=0)   
    self.subject = Entry(window, width=40)
    self.subject.grid(row=1, column=1,pady=5) 
    self.text = Text(window,width= 40, height =10)   
    self.text.grid(row=3, column=1, pady=5, padx=5)
    self.absenden = Button(window, text='Abschicken',
                       command=self.send)
    self.absenden.grid(row=3, column=0,padx=5)
    window.mainloop()

  def send(self):
    server = smtplib.SMTP_SSL(SERVER, PORT)             #3
    server.login(FROM, PASSWORD)
    server.set_debuglevel(1)                            #4
    message = SCHABLONE.format(FROM,
                 self.to.get(),
                 self.subject.get(),
                 self.text.get('1.0', END))             #5
    server.sendmail(FROM,
                    self.to.get(), message)             #6
    server.close()                                      #7

SMTPClient()





                    
