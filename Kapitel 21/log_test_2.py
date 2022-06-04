#----------------------------------------------------
# Dateiname:  log_test_2.py 
# Programm demonstriert einige Funktionen des Moduls logging
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------

import logging
logging.basicConfig(filename="tmp/logging.txt",
		    format='%(asctime)s -> %(message)s')

logging.critical("Wassereinbruch in Laufwerk E")

