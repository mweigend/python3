#----------------------------------------------------
# Dateiname: beratung.py
# Automatische Buergerberatung (chat bot)
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
# beratung.py
class Beratung(object):
  z1 = 'Dafür ist das Einwohnermeldeamt zuständig.'           #1
  z2 = 'Wenden Sie sich bitte an das Straßenverkehrsamt.'
  z3 = 'Ihr Ansprechpartner ist Frau Helf vom Standesamt.'
  a1 = 'Am besten, Sie melden sich morgen noch einmal.'

  def beantworte(self, frage):
    # gibt eine Antwort auf eine Frage zurück
    eingabe = frage.lower()                                 #2
    if eingabe.count('hochzeit') + eingabe.count('heirat') > 0:                         #3
        return self.z3
    elif eingabe.count('kfz') + eingabe.count('auto') > 0:
        return self.z2   
    elif eingabe.count('ausweis') + eingabe.count('pass') \
         + eingabe.count('meld') > 0:
        return self.z1
    else: return self.a1

  def __begruessen(self):
    print('Herzlich willkommen bei der Bürgerberatung!')
    print('Bitte geben Sie Ihren Nachnamen an.')
    nachname = input('Nachname: ')                
    print('Wie soll ich Sie anreden,',
              'Herr {0} oder Frau {0}?'.format(nachname))
    eingabe = input(': ')
    if 'frau' in eingabe.lower():
        self.anrede = 'Frau ' + nachname
    else:
        self.anrede = 'Herr ' + nachname     

  def chat(self):
    zufrieden = False
    self.__begruessen()
    print('Was kann ich für Sie tun, {}?'.format(self.anrede))                                 #6
    while not zufrieden:
        eingabe = input(': ').lower()
        if eingabe.count('nicht') + eingabe.count('danke') > 0:
            zufrieden = True
        else:
            print(self.beantworte(eingabe))
            print('Was kann ich noch für Sie tun, {}?'.format(self.anrede))
    print('Auf Wiedersehen, {}.'.format(self.anrede))

chat = Beratung()
chat.chat()

input()  # Warten bis <ENTER> gedrückt worden ist


