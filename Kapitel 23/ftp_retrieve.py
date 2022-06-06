#----------------------------------------------------
# Dateiname: ftp_retrieve.py
# Vom FTP-Server der DLR wird ein Satellitenfoto
# heruntergeladen.
#
# Python 3
# Kap. 23
# Michael Weigend 04.06.2022
#----------------------------------------------------

# ftp_retrieve.py
import ftplib
ftp = ftplib.FTP('ftp.dfd.dlr.de', 'name', 'ich@meinedomain.de')
ftp.cwd('ql/www')
print(ftp.retrlines('LIST'))

with open('foto.gif', 'wb') as stream:
  ftp.retrbinary('RETR ndvi_new.gif', stream.write)  #1
ftp.close()
                    

