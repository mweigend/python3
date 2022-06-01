#!/Python310/python.exe                             

#----------------------------------------------------
# Dateiname:  chat.py 
# wsgi-Script für einen einfachen Chat-Room.
# 
# Python 3
# Kap. 22
# Michael Weigend 20. 2. 19
#----------------------------------------------------
import cgi
START = '''
<html>
  <head>
    <title>Python Chat Room</title>
  </head>
  <body>
    <h1>Python Chat</h1>
    Willkommen im Python Chat Room. <br>
    Unter welchem Namen m&ouml;chtest du auftreten?
    <form method="POST" >
      Name:&nbsp;
      <input type="Text" name= "name"
       size="12" maxlength="12"/>
      <input type="hidden" name="contribution"
       value="Hallo, ich bin gerade gekommen."/>
      <input type="Submit"  value="Login"/>
    </form>
   </body>
</html>'''                                        #1
                         
CHAT = '''
<html>
  <head><title>Python-Chat</title></head>
  <body>
    <h1>Python-Chat</h1>
     {} <hr/>
     <form method="POST">
       <input type="hidden" name="name" value="{}"/>
       Ich sage:&nbsp;
       <input type="Text" name="contribution" size="40"
       maxlength="40"/>
       <input type="Submit"  value="OK"/>
     </form>
  </body>
</html>'''                                        #2

PATH = "dialog.txt"                               #3
                                     
class Dialog:
  # Modelliert den Dialog eines Chats
  
  def __init__(self, path):
    self.filename = path
    try:                                                
      f = open(self.filename,'r')                 #4
      self.lines = f.readlines()
      f.close()
    except:                                       #5
      self.lines=[]
      f = open(self.filename, 'w')
      f.close()

  def update(self, name, contribution):  
    # Neuen Beitrag in Dialog einfügen und speichern
    if len(self.lines)>10:                        #6               
        self.lines = self.lines[-10:]
    newLine = '{}: {} <br>\n'.format(
                          name, contribution)
    self.lines.append (newLine)                   #7
    f = open(self.filename,'w')                   #8
    for line in self.lines:
        f.write(line)
    f.close()

  def __str__(self):
    # liefert Darstellung des Dialogs als HTML-Text
    dialog = ''
    for line in self.lines:
      dialog += line
    return dialog

class Chatroom:
  html = {'>':'&gt;', '<':'&lt;',
          'ä':'&auml;', 'Ä':'&Auml;',
          'ö':'&ouml;', 'Ö':'&Ouml;',
          'ü':'&uuml;', 'Ü':'&Uuml;',
          'ß':'&szlig;'}                          #9

  def escape(self, text):
    for ch in self.html.keys():
      text = text.replace(ch, self.html[ch])
    return text                                   #10

  def __call__(self, environ, start_response):  
    if environ['REQUEST_METHOD'] == 'POST':
        form = cgi.FieldStorage(
            fp=environ['wsgi.input'],             
            environ=environ,
            keep_blank_values=True)               #11
        contribution = self.escape(
                 form.getvalue('contribution'))    
        name = self.escape(
                 form.getvalue('name'))           #12
        dialog = Dialog(PATH)                     #13
        if contribution:                     
            dialog.update(
              name, self.escape(contribution))    #14
        content = CHAT.format(dialog, name)       #15 
    else:
        content = START                           #16   
    response_headers = [
         ('Content-type', 'text/html; charset=utf-8'),
         ('Content-Length', str(len(content)))] 
    status = '200 OK'    
    start_response(status, response_headers)
    return [content.encode('utf-8')]              #17
    
application = Chatroom()

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, application)
    print('Serving on port 8000... ')
    httpd.serve_forever()














                    
