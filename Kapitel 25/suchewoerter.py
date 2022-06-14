#----------------------------------------------------
# Dateiname:  suchewoerter.py 
# Demo fuer doctest
# Loesung Aufgabe 1
# 
# Python 3
# Kap. 25 
# Michael Weigend 15.06.2022
#----------------------------------------------------

def sucheWörter (text, n):
  """ Liefert Menge aller Wörter mit n Buchstaben 

  >>> text = "Habe nun, ach! Philosophie,\
  Juristerei und Medizin und leider auch Theologie\
  durchaus studiert, mit heißem Bemühn."
  >>> s = sucheWörter (text, 4)
  >>> s == {"Habe", "auch"}                           #1
  True
  """

  textBereinigt = "".join(
             [c for c in text if c not in "!?.,;:-"]) #2
  wortmenge = set(textBereinigt.split())
  liste = [wort for wort in wortmenge 
                if len(wort) == n]                    #3
  return set(liste)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)


