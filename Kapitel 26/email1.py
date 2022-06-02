#----------------------------------------------------
# Dateiname: email.py
# Modul mit einer XML-basierten Klasse Addresses
#
# Python 3,  mitp Verlag
# Kap. 26
# Lösung Aufgabe 2
# Michael Weigend 08. 06. 2019
#----------------------------------------------------

from xml.dom import minidom

class Addresses(object):
    
  def __init__(self, path):  
    self.doc = minidom.parse(path)
    
    
  def getAllAddresses (self):
    # Liefert Dictionary, das zu jedem Namen eine Liste mit
    # zugehoerigen E-Mail-Adressen enthaelt
    d = {}
    for p in self.doc.getElementsByTagName("person"):
        name = p.getAttribute("name")
        emails = p.getElementsByTagName("email")
        d[name] = [e.firstChild.data for e in emails]
    return d
            

  def getAddresses(self, name):
    # Liefert die E-Mail-Adressen der Person name
    for p in self.doc.getElementsByTagName("person"):
        if p.getAttribute("name") == name:
            emails = p.getElementsByTagName("email")
            return [e.firstChild.data for e in emails]

  def insertAddress (self, name, email):
    # Fuegt neue Email-Adresse email fuer Person name ein
    for p in self.doc.getElementsByTagName("person"):
      if p.getAttribute("name") == name:
        textNode = self.doc.createTextNode(email)
        elementNode = self.doc.createElement("email")
        elementNode.appendChild(textNode)
        p.appendChild(elementNode)
        return                                   

  def insertPerson(self, name):
    # Fuegt neue Person mit Namen name ein
    group = self.doc.documentElement
    person = self.doc.createElement("person")
    person.setAttribute("name", name)
    group.appendChild(person)
    pass
    
  def deleteAddress (self, email):
    # Loescht erstes Vorkommen der E-Mail-Adresse email
    emails = self.doc.getElementsByTagName("email")
    for e in emails:
        if e.firstChild.data == email: 
            p = e.parentNode
            p.removeChild(e)
            e.unlink()

  def removePerson (self, name):
    # Loescht Daten der Person mit Namen name
    for p in self.doc.getElementsByTagName("person"):
        if p.getAttribute("name") == name:
            self.doc.documentElement.removeChild(p)
            p.unlink()

  def save (self, path):
        f = file(path, 'w')
        f.write(self.doc.toxml())

  def __str__(self):
        return self.doc.toxml()


# Test
if __name__ == "__main__":
    a = Addresses("gruppeattr.xml")

    emailDict = a.getAllAddresses()
    sabrinasEmails = a.getAddresses("Sabrina Maier")
    print("E-Mail-Adressen:")
    print(emailDict)
    print("E-Mail-Adressen von Sabrina Maier:")
    print(sabrinasEmails)
    name = "Karl"
    a.insertPerson(name)       
    print ("XML-Dokument mit Karl:")
    print (a)
    a.removePerson("Karl")
    print ("XML-Dokument ohne Karl:")
    print (a)
   

    

        
