#----------------------------------------------------
# Dateiname:  log_test_3.py 
# Programm demonstriert einige Funktionen des Moduls logging
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------
import logging
logging.basicConfig(filename="tmp/logging.txt",
                    level=logging.DEBUG,
		    format='%(module)s, Zeile %(lineno)d: %(message)s')
for i in range(4):
    logging.debug("Meldung {}.".format(i))

