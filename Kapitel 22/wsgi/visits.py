#! /Python310/python.exe                               #1

#----------------------------------------------------
# Dateiname:  visits.py 
# WSGI-Skript, das eine html-Seite generiert. Es merkt sich
# in einem Cookie, wie oft der Client diese Seite schon besucht hat.
# 
# Objektorientierte Programmierung mit Python
# Kap. 22
# Michael Weigend 27.05.2022
#----------------------------------------------------
                             
from http.cookies import SimpleCookie
# Stringkonstanten
START = '''
<html>
  <head><title>Z&auml;hler</title></head>
  <body>
  <h3> Willkommen!</h3>
   Sie besuchen diese Seite zum ersten Mal
  </body>
</html>'''                                      #1

RESPONSE = '''
<html>
  <head><title>Z&auml;hler</title></head>
  <body>
    <h3> Sch&ouml;n, dass Sie wieder hier sind!</h3>
    Sie besuchen zum {}. Mal diese Seite.
  </body>
</html>'''                                      #2

class Counter:
   def __call__(self, environ, start_response):
     cookie = SimpleCookie()                    #3
     try:
         cookie.load(environ['HTTP_COOKIE'])    #4
         n = int(cookie['counter'].value) + 1   #5
         content = RESPONSE.format(n)   #6
     except:
         content = START                        #7
         n = 1                                  #8        
       
     response_headers = [
         ('Content-type', 'text/html; charset=utf-8'),
         ('Content-Length', str(len(content))),
         ('Set-Cookie', 'counter={}'.format(n))] #9
     status = '200 OK'    
     start_response(status, response_headers)
     return [content.encode('utf-8')] 

application = Counter()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000... ')
    httpd.serve_forever()

















                    
