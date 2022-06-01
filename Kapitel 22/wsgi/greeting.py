import cgi

START = '''
<html>
    <head>
        <title>Frage</title>
    </head>
    <body>
        <form method="POST">
            <label>Dein Name: </label>
            <input type="text" name="name">
            <input type="submit" value="OK">
        </form>
    </body>
</html>
'''

RESPONSE = '''
<html>
    <head>
        <title>Antwort</title>
    </head>
    <body>
        <h1> Hallo {}!</h1>
    </body>
</html>
'''

def application(environ, start_response):
    status = '200 OK'    
    if environ['REQUEST_METHOD'] == 'POST':
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=environ,
            keep_blank_values=True)
        content_string = RESPONSE.format(form.getvalue('name'))
        content = content_string.encode('utf-8')
    else:
        content = START.encode('utf-8')
    response_headers = [('Content-type', 'text/html'),
                        ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    return [content]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    httpd = make_server("", 8000, application)
    print("Serving on port 8000...")
    httpd.serve_forever()
