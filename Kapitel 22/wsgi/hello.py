#----------------------------------------------------
# Dateiname:  hello.py 
# wsgi-Script für eine einfache Online-Abstimmung.
# 
# Python 3
# Kap. 22
# Michael Weigend 20. 5. 2022
#----------------------------------------------------


CONTENT = b'''<html>
                 <body>
                     <h1>Hallo!</h1>
                 </body>
            </html>'''

def application(environ, start_response):           #1
    status = '200 OK'
    start_response(status,
              [('Content-type', 'text/html'),
              ('Content-Length', str(len(CONTENT)))
              ])                                    #2
    return [CONTENT]                                #3

if __name__ == '__main__':                          #4          
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000...')
    httpd.serve_forever()

