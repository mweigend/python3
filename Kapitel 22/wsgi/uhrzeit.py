#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  uhrzeit.py 
# wsgi-Skript, das html-Seite mit aktueller Uhrzeit ausgibt
#
# Python 3
# Kap. 22
# Michael Weigend 22.05.2022
#----------------------------------------------------
from time import localtime
HTML = '''
<html>
  <body>
    <h2>Die aktuelle Uhrzeit </h2>
      Es ist {} Uhr und {} {}.
  </body>
</html>'''                                          #1
    
def app(environ, start_response):                   #2
    zeit = localtime()
    h, m = zeit[3], zeit[4]
    if m == 1:
        m_text = 'Minute'
    else:
        m_text = 'Minuten'
    message = bytes(HTML.format(h, m, m_text),
                    encoding='utf-8')
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [message]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 8000
    httpd = make_server('', port, app)
    print('Serving on port {}...'.format(port))
    httpd.serve_forever()
