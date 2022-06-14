#----------------------------------------------------
# Dateiname:  ranking.py 
# Modul mit Klasse Ranking für Wahl des "Wortes des Jahres"
# Demonstration der Funktion doctest.testmod()
# 
# Python 3
# Kap. 25
# Michael Weigend 29.1.2013
#----------------------------------------------------

"""
Modul mit der Klasse Ranking


>>> r = Ranking("not_existing.txt")                   #A
>>> r.add("Titan")
>>> r.add("Titan")
>>> r.add("Titan")
>>> r.add("Einstein")
>>> r.add("Methan")
>>> r.add("Einstein")
>>> r.getRank("Titan")                                #B
1
>>> r.getRank("Methan")
3
>>> r.getTop(0)                                       #C
''
>>>                                                   #D
>>> r.getTop(2) #doctest: +NORMALIZE_WHITESPACE
'Titan 3 <br>
Einstein 2 <br> '
>>>                                                   #E
>>> r.getTop(1000) #doctest:+ELLIPSIS, +NORMALIZE_WHITESPACE
'Titan 3
...'
>>> d = {'Einstein': 2, \
         'Methan': 1,   \
         'Titan': 3}                                  #F
>>> r.voting == d  
True
"""

import pickle 
class Ranking:                                        #1
  def __init__ (self, filename):
    self.filename = filename
    try:                                              #2
        f = open(filename, "rb")
        self.voting = pickle.load(f)
        f.close()
    except: self.voting = {}

  def add (self, word):                               #3
      if word in self.voting.keys():
          self.voting[word] += 1
      else: self.voting[word] = 1

  def getTop(self, n):
      items = [(self.voting[word], word)              #4
               for word in self.voting.keys()]
      items.sort(reverse = True)                      #5
      top = items[:n]                                 #6
      response = ""                                   #7
      for (votes, word) in top:
          response += "{} {} <br> ".format(word, votes)
      return response

  def getRank (self, word):                           #8
      votes = self.voting[word]                       
      vote_list = list(self.voting.values())          #9
      vote_list.sort(reverse = True)
      return vote_list.index(votes)+1                #10

  def save (self):
      f = open (self.filename, "wb")
      pickle.dump(self.voting, f)
      f.close()

if __name__ == "__main__":                           #11
    import doctest
    doctest.testmod()


    

