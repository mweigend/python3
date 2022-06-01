#!/Python310/python.exe                             

#----------------------------------------------------
# Dateiname:  abstimmung.py 
# wsgi-Script für eine einfache Online-Abstimmung.
# 
# Python 3
# Kap. 22
# Michael Weigend 20. 3. 2019
#----------------------------------------------------

import pickle
from cgi import FieldStorage
from http.cookies import SimpleCookie

# Globale Konstanten:
START ='''
<html>
<head>
    <title>Abstimmung</title>
</head>
<body>
  <h2> Willkommen zur Online-Abstimmung!</h2>
  <h3> Sind Studiengeb&uuml;hren an Unis sinnvoll?</h3>
  <form method="POST">
    <input type="Radio" name="option" value="Ja">&nbsp;ja<br>
    <input type="Radio" name="option" value="Nein">&nbsp;nein<br><br>
    <input type="Submit" value="Abstimmen">
  </form>
</body>
</html>'''                                      #1

RESULT = '''
<html>
  <head><title>Online-Abstimmung</title></head>
  <body><h1>Online-Abstimmung</h1>
    <h3> {} </h3>
    Hier ist das aktuelle Abstimmungsergebnis:<br>
    Frage: {} <br><br> {}
  </body>
</html>'''                                      #2

PATH = 'count.dat'                              #3
OPTIONS = ['Ja', 'Nein']
QUESTION = 'Sind Studiengeb&uuml;hren an Unis sinnvoll?'

class Counter:
  '''Modelliert einen Zähler für Abstimmungsergebnisse'''
  def __init__(self, filename,options):
    self.filename = filename
    try:        # vorhandene Datei laden
       f = open(filename,'rb')                  #4
       self.votes = pickle.load(f)
       f.close()
    except:     # neue Datei anlegen
       self.votes = {}                          #5
       for i in options:
           self.votes[i] = 0
       f = open(filename,'wb')
       pickle.dump(self.votes, f)
       f.close()       

  def vote(self, option):
    # Option erhält eine Stimme
    self.votes[option] += 1                     #6
    f = open(self.filename, 'wb')
    pickle.dump(self.votes, f)
    f.close()

  def __str__(self):
    # liefert HTML-Text mit Abstimmungsergebnis
    result = ''
    for option in self.votes.keys():
      result += '<b>{}: </b>{} Stimmen<br>\n'.format(
                            option, self.votes[option])
    return result

class Voting:
  '''Modelliert ein Abstimmungssystem'''
  def __call__(self, environ, start_response):
      self.counter = Counter(PATH, OPTIONS)
      try:
          cookie = SimpleCookie()
          cookie.load(environ['HTTP_COOKIE'])
          status = cookie['status'].value       #7
          print(1, status)
      except:
          status = 'Start'
      if status =='Start':
          content = START                       #8
          new_status= 'Abstimmen'
      elif status == 'Abstimmen':                 
          form = FieldStorage(
                fp=environ['wsgi.input'],             
                environ=environ,
                keep_blank_values=True)   
          option = form.getvalue('option')
          if option:                            #9
              self.counter.vote(option)
              content = RESULT.format(
                  'Vielen Dank für Ihr Voting!',
                    QUESTION, self.counter)
              new_status = 'Abgestimmt'
          else:
                content = START
                new_status= 'Abstimmen'
      else:
          new_status = 'Abgestimmt'
          content = RESULT.format(
              'Sie haben bereits abgestimmt ...',
              QUESTION, self.counter)     
                    
      response_headers = [
         ('Content-type', 'text/html; charset=utf-8'),
         ('Content-Length', str(len(content))),
         ('Set-Cookie','status={}'.format(new_status))]
      print(response_headers)
      status = '200 OK'    
      start_response(status, response_headers)
      return [content.encode('utf-8')]

application = Voting()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000... ')
    httpd.serve_forever()


















                    
