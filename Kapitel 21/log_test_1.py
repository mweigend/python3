#----------------------------------------------------
# Dateiname:  log_test_1.py 
# Programm demonstriert einige Funktionen des Moduls logging
#
# Python 3  mitp Verlag
# Kap. 21
# Michael Weigend 7.6.2019
#----------------------------------------------------
# log_test_1.py
import logging, sys
logging.basicConfig(file=sys.stdout)    #1

log = logging.getLogger("Modul 1")
log.setLevel(logging.INFO)
log.debug("nicht so wichtig")           #2
log.info("wichtig")

