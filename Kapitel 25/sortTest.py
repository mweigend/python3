#----------------------------------------------------
# Dateiname:  sortTest.py 
# Testarrangement zum Testen der sort()-Methode
# von Listen
# 
# Objektorientierte Programmierung mit Python
# Kap. 25 
# Michael Weigend 15. 11. 2009
#----------------------------------------------------

#sortTest.py
import unittest, random

class TestSort (unittest.TestCase):
  def setUp(self):
    self.list = [random.randint(0, 100)
                 for i in range(20)]                  #1

  def testlength(self):
    """ Ist die sortierte Liste genauso lang
    wie die unsortierte Liste?"""
    len_unsorted = len(self.list)
    self.list.sort()
    len_sorted = len (self.list)
    self.assertTrue(len_sorted == len_unsorted) 

  def testbegin(self):
    """Ist am Anfang der sortierten Liste
    das kleinste Element?"""
    self.list.sort()
    self.assertTrue(self.list[0] == min (self.list))

  def testorder (self):
    """Ist der linke Nachbar eines Listenelementes
    nicht größer?"""
    self.list.sort()
    for i in range(1,len(self.list)):
      self.assertFalse(self.list[i-1]> self.list[i])

suite = unittest.TestSuite()
TestSort("testlength")
suite.addTest(TestSort("testlength"))
suite.addTest(TestSort("testbegin"))
suite.addTest(TestSort("testorder"))
testrunner = unittest.TextTestRunner(verbosity=2)
testrunner.run(suite)

