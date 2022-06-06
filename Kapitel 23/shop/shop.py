#! /python36/python.exe                               #1

#----------------------------------------------------
# Dateiname:  shop.py 
# WSCGI-Skript, das Teil eines online-Shops ist.
# Folgende Variablen eines HTML-Formulars werden verarbeitet:
# email: E-Mail-Adresse des Kunden
# artikel: Liste der ausgewählten Artikel.
# Das Skript sendet eine Antwortseite und zwei E-Mails mit
# einer Auftragsbestätigung.
# 
# Python 3, 8. Auflage 2019
# Kap. 23 Lösung 2
# Michael Weigend 2.4.2019
#----------------------------------------------------
START = '''
<html>
<head><title>Online-Shop</title></head>
<body bgcolor=#C0C0C0>
 <h2> Willkommen im Schuh-Shop</h2>
  <form method="POST">
   <input type="Checkbox" name="item" value="buerste"/>
   Schuhb&uuml;rste 4.50 EUR<br/>
   <input type="Checkbox" name="item" value="schwarz"/>
   Schuhcreme (schwarz) 3.00 EUR<br/>
   <input type="Checkbox" name="item" value="farblos"/>
   Schuhcreme (farblos) 3.00 EUR<br/><br/>
   Ihre E-Mail-Adresse: &nbsp;
   <input type="Text" name="email" size="30"/><br/><br/>
   <input type="Submit" value="Bestellung absenden"/>
  </form>
 </body>
</html>
'''                                                      #1
FROM = 'shop@xxxxxx.de'                      #2
PASSWORD = 'mixxxxxxxx'
SERVER = 'smtp.strxxx.de'
PORT = 465 


import cgi, smtplib
MESSAGE = ''''From: {}
To: {}
Subject: Bestellung Online-Shop
MIME-Version: 1.0
Content-Type: text/html
Content-Transfer-Encoding: quoted-printable

<html><body>
<h3>Vielen Dank f&uuml;r Ihre Bestellung!</h3>
{}
</body></html>'''                                    #1

RESPONSE_1 = '''
<html><body>
<h3>Vielen Dank f&uuml;r Ihre Bestellung!</h3>
Sie erhalten eine Mail mit einer
Auftragsbest&auml;tigung.</body></html>'''           #2

RESPONSE_2 = '''
<html><body>
<h3>Fehler</h3>
Ihre Bestellung konnte nicht bearbeitet werden.
</body></html>'''

class Mail:                                    #3
  def __init__(self):
    self.server=smtplib.SMTP_SSL(SERVER, PORT)

  def send (self, toaddr, order):
    self.server.login(FROM, PASSWORD)
    self.server.set_debuglevel(1) 
    msg=MESSAGE.format(FROM, toaddr, order)
    self.server.sendmail(FROM,toaddr, msg)
    self.server.close()

class Shop():                                                #4
  offer = {'buerste':('Schuhb&uuml;rste', '4.50'),
           'schwarz':('Schuhcreme (schwarz)', '3.00'),
           'farblos':('Schuhcreme (farblos)', '3.00')}
  
  def __call__(self, environ, start_response):
    status = '200 OK'
    if environ['REQUEST_METHOD'] == 'POST':
      form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True)
      self.items = form.getlist('item') # vom Kunden gewählte Artikel
      self.client = form.getvalue('email')
      self.mail = Mail()
      self.order = self.createOrder()
      if self.order:
          self.mail.send(self.client, self.order)
          content = RESPONSE_1.encode('utf-8')
      else:
          content = RESPONSE_2.encode('utf-8')
    else:
        content = START.encode('utf-8')
      
    response_headers = [('Content-type', 'text/html'),
                          ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    return [content]

  def createOrder(self):                         #5
    text = '''E-Mail-Adresse des Kunden: {}<br/><br/>
            Bestellte Artikel:<br/>'''.format(self.client)
    sum_ = 0
    for item in self.items:
        description, price = self.offer[item]
        text += '{} {} EUR<br/>'.format(description, price)
        sum_ += float(price)
    text += '''Transport und Verpackung: 5 EUR<br/>
               Summe: {} EUR'''.format(sum_ + 5)
    if self.client and self.items:
        return text
    else: return ''

application = Shop()

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server("", 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
















                    
