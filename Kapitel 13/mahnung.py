#----------------------------------------------------
# Dateiname: mahnung.py
# Automatische Produktion von Mahnbriefen
#
# Python 3
# Kap. 13
# Michael Weigend 4.6.2019
#----------------------------------------------------
# mahnung.py
class Mahnung:
    basistext = """{anrede} {name},

dies soll keine Mahnung sein. Ich möchte dich nur daran
erinnern, dass du deine Clubbeiträge für die Monate
{von} bis {bis} noch nicht bezahlt hast.
Bitte überweise sie umgehend auf das unten stehende Konto.

Mit freundlichen Grüßen
Tim (Kassenwart)
"""                                                   #1
    def __init__(self, geschlecht, name, von, bis ):
        if geschlecht == 'm':
            anrede = 'Lieber'
        else:
            anrede = 'Liebe'

        self.text = self.basistext.format(anrede=anrede,
                                         name=name,
                                         von=von,
                                         bis=bis)     #2

    def __str__(self):
         return self.text                             #3

# Hauptprogramm
personen = [('m', 'Sven', 'Januar', 'Mai'),
            ('w', 'Jenny', 'Februar', 'Juli')]

for g, n, v, b in personen:
    print(Mahnung(g, n, v, b))


input('Beenden mit <ENTER>')
        
