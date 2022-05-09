#----------------------------------------------------
# Dateiname: beschwerde.py
# Gespraechsroboter, der Beschwerden bearbeitet
#
# Python 3
# Kap. 13 Lösung 5
# Michael Weigend 2.10.09
#----------------------------------------------------
 
# beschwerde.py
from random import randint
from re import *
class Beschwerde(object):         
    # Einleitung                                     #1
    e1 = 'Hallo, ich bin Melanie.\n'+ \
       'Was kann ich für Sie tun?\n'
    # Unverstandene Eingabe
    ue1 = 'Dazu kann ich leider nichts sagen.\n'
    ue2 = 'In diesem Punkt kann ich nicht weiterhelfen.\n'
    unverstanden=[ue1, ue2]
    # Neues Hilfsangebot
    nh1 = 'Kann ich noch irgendwie weiterhelfen?\n'
    nh2 = 'Was kann ich noch für Sie tun?\n'
    hilfe = [nh1,nh2]
    # Lange Lieferzeit
    ll1 = 'Das ist eine lange Zeit. \n'+ \
        'Wir bearbeiten alle Aufträge umgehend.\n'+ \
        'Aber manchmal gibt es Lieferschwierigkeiten.\n'
    ll2 = 'So lange? Ich kümmere mich darum.\n'
    lieferzeit=[ll1, ll2]
    # Defektes Gerät
    dg1 = 'Senden Sie das defekte Gerät zurück.\n'
    dg2 = 'Defekte Geräte senden Sie einfach an uns zurück.\n'
    defekt = [dg1, dg2]

    def waehle (self, liste):                         #2
        return liste[randint(0, len(liste)-1)]

    def antworte(self, eingabe):                      #3
        eingabe = eingabe.lower()
        gehtNicht = compile('geht nicht|funktioniert nicht|kaputt',I)
        antwort=''
        if eingabe.count('woche') + eingabe.count('monat')  >0:
            antwort += self.waehle(self.lieferzeit)
        elif gehtNicht.search(eingabe):               #4
            antwort += self.waehle(self.defekt)
        else: antwort += self.waehle(self.unverstanden) 
        return antwort + self.waehle(self.hilfe)

    def chat(self):
        zufrieden = compile('nichts|danke|nein', I)   #5
        print(self.e1)
        eingabe = input('Kunde: ')
        while not zufrieden.search(eingabe):          #6
            print(self.antworte(eingabe))
            eingabe = input('Kunde: ')
        print('Auf Wiedersehen.')

beschwerdeannahme = Beschwerde()
beschwerdeannahme.chat()


input('Beenden mit <ENTER>')
