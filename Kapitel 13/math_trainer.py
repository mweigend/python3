#----------------------------------------------------
# Dateiname: math_trainer.py
# Mathetrainer mit Sprachausgabe
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------

import win32com.client
import random

class Speaker(object):
    def __init__ (self, pitch=0, rate=0, volume=0):
        self.pitch = pitch   # Tonhöhe
        self.voice = win32com.client.Dispatch('Sapi.SpVoice')
        self.voice.Rate = rate
        self.voice.Volume = volume

    def say(self, text):
        self.voice.Speak(
            '<pitch middle = "{}"> {} </pitch>'.format(self.pitch, text))
    
class Math_trainer(object):
    def __init__ (self, level):
        self.level = level
        self.anne = Speaker(pitch=-5, rate=-2, volume=80)
        self.laura = Speaker(pitch=10, rate=1, volume=100)
        self.points = 0

    def ask(self):
        a = random.randint(2, self.level)
        b = random.randint(2, self.level)
        question = "Wie viel ist {} + {}? ".format(a, b)
        self.anne.say(question)
        answer = input("{} + {} = ".format(a, b))
        if int(answer) == a + b:
            self.points += 1
            feedback = """Richtig!
                       Du hast {} Punkte.
                       """.format(self.points)
            self.laura.say(feedback)
            self.level += 1
        else:
            feedback = """Leider falsch.
                          {} + {} ist {}""".format(a, b, a+b)
            self.anne.say(feedback)
            self.level -=1
            if self.level < 5: self.level = 5          

    def practise(self):
        self.anne.say("Hallo, ich bin Anne. Lass uns Mathe üben.")
        for i in range(5):
            self.ask()
        self.anne.say("""Herzlichen Glückwunsch.
            Du hast {} Punkte. Bis bald!!
            """.format(self.points))
                          
Math_trainer(5).practise()        
