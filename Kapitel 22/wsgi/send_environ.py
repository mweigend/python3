#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  send_environ.py 
# wsgi-Skript liefert den Inhalt von environ
#
# Python 3
# Kap. 22
# Michael Weigend 22.05.2022
#----------------------------------------------------                                     


def app(environ, start_response):                              #1
    environ_text = bytes(str(environ), encoding='utf-8')
    start_response('200 OK', [('Content-Type', 'text/html')])  #2
    return [environ_text]                                      #3

if __name__ == "'__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, app)
    print('Serving on port 8000...')
    httpd.serve_forever()
