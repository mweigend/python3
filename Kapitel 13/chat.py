#----------------------------------------------------
# Dateiname: chat.py
# Chat Bot
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
# chat.py
from re import *                      
class Chat (object):
    def __alle(self, e):                         
        re1 = compile('alle \w\w+en', I)              #1
        re2 = compile('alle', I)                      #2
        re3 = compile('[.!,;]+')                      #3
        m1 = re1.search(e)                              
        m2 = re2.search(e)
        if m1:
            passendesStueck1 = m1.string[m1.start():m1.end()]  #4
            verb = passendesStueck1.split()[1]        #5
            stamm = verb[:-2]                         #6
            passendesStueck2 = m2.string[m2.start():] #7
            satz = re3.split(passendesStueck2) [0]    #8
            restsatz = passendesStueck2.split(' ',2)[2] #9
            restsatz = restsatz.replace('mich','Sie')   
            restsatz = restsatz.replace('mein', 'Ihr')
            antwort = 'Wer {}t {}?'.format(stamm, restsatz)
            
            antwort += ' Denken Sie an bestimmte Personen?'
            return antwort

    def __familie(self, e):                                
         re = compile('bruder|schwester|mutter|vater', I)
         if re.search(e):
             antwort = 'Erzählen Sie mir mehr über Ihre Familie.'
             return antwort

    def __negativ(self, e):                           
         re = compile('nein|nicht|kein', I)
         if re.search(e):
             antwort = 'Denken Sie nicht ein bisschen negativ?'
             return antwort

    def chat(self):
      print('Hallo, ich bin Mini-Eliza.')
      e = input('Sie: ')
      while e:
        if self.__alle(e): print(self.__alle(e)) 
        elif self.__familie(e): print(self.__familie(e))
        elif self.__negativ(e): print(self.__negativ(e))
        else: print('Aha ...')
        e = input('Sie: ')
      print('Auf Wiedersehen!')

chat = Chat()
chat.chat()



input('Beenden mit <ENTER>')
