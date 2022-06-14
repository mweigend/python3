#----------------------------------------------------
# Dateiname:  rankingtest_fortgeschritten.py 
# Fortgeschrittene Testumgebung für das Modul ranking
# 
# Python 3
# Kap. 25 
# Michael Weigend 15. 11. 2009
#----------------------------------------------------

import unittest, os, random, ranking

class TestRanking1 (unittest.TestCase):              #1
  """Funktionstests"""

  def setUp(self):                                   #2
    """Erzeuge Testdaten und Ranking-Objekt """
    self.words = ["Titan", "Jupiter", "Titan",
                  "Titan", "Huygens", "Jupiter"]      
    self.r = ranking.Ranking("not_existing.txt")
    for w in self.words:
            self.r.add(w)
    self.r.save()

  def tearDown(self):
    """Lösche Testdatei """
    try:
        os.remove("not_existing.txt")                #3
    except: pass

  def testRank(self):                                #4
    """Prüfe, ob Rang richtig berechnet wird"""
    self.assertTrue (self.r.getRank("Titan") == 1)
    self.assertTrue (self.r.getRank("Jupiter") == 2)
    self.assertTrue (self.r.getRank("Huygens") == 3)

  def testSave(self):
    """ Pruefe, ob alle Woerter uebernommen wurden"""
    r = ranking.Ranking("not_existing.txt")
    for w in set(self.words):
        self.assertTrue (r.voting[w]==self.words.count(w))

  def testGetTop(self):
    """ Wird das am häufigsten gewählte Wort erkannt?"""
    expected = "Titan 3 <br> "
    text = self.r.getTop(1)
    self.assertEqual(text, expected)

class TestRanking2 (unittest.TestCase):              #5
  """Belastungstest"""
  def setUp(self):  
    """erzeuge Zufallsliste von Wörtern"""
    f = open("willkommen.txt", "r")                  #6
    text = f.read()
    f.close()
    words = text.split()                             #7
    self. words = [random.choice(words)
                       for i in range(1000)]         #8

  def tearDown(self):
    """Lösche Datei, die durch den Test erzeugt worden ist"""
    try: os.remove("testfile.txt")
    except: pass

  def testAdd(self):   
    """Belastungstest"""
    for w in self.words:                             #9
      r = ranking.Ranking("testfile.txt")
      r.add(w)
      r.save()
    for w in set(self.words):
      self.assertTrue(r.voting[w]==self.words.count(w))

suite = unittest.TestSuite()                         #10
suite.addTests((TestRanking1("testRank"),
                TestRanking1("testSave"),
                TestRanking1("testGetTop"),
                TestRanking2("testAdd")))
testrunner = unittest.TextTestRunner(verbosity=2)    #11
testrunner.run(suite)


 
