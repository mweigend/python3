#! /usr/bin/env python3                              #1

#----------------------------------------------------
# Dateiname:  rankingtest.py 
# Einfache Testumgebung für das Modul ranking
# 
# Python 3
# Kap. 25 
# Michael Weigend 29.1.2013
#----------------------------------------------------
import unittest, ranking
class TestRanking (unittest.TestCase):
  def setUp(self):
    """Erzeuge Liste von Woertern und Ranking-Objekt"""
    self.words = ["Jupiter", "Titan", "Jupiter"]
    self.r = ranking.Ranking("not_existing.txt")
        
  def testAdd(self):
    for w in self.words:
        self.r.add(w)
    for word in self.r.voting.keys():
        n_voting = self.r.voting[word]
        n_words = self.words.count(word)
        self.assertTrue(n_voting == n_words)
             
suite = unittest.TestSuite()
test = TestRanking("testAdd")
suite.addTest(test)
testrunner = unittest.TextTestRunner(verbosity=2)
testrunner.run(suite)
