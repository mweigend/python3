#! /Python310/python.exe

#----------------------------------------------------
# Dateiname:  catserver.py 
# Service-Skript, das XML-Dokument verarbeitet
# Achtung! Die erste Zeile (Shebang-Zeile) muss an
# Ihr System angepasst werden. Unter Unix lautet sie so:
#!/usr/bin/env python3
#
# Objektorientierte Programmierung mit Python
# Kap. 26
# Michael Weigend 18.11.2009
#----------------------------------------------------

XMLPATH = "katalog/katalog_1.xml"                     #1
HTMLPATH = "katalog/katalog.html"

HTML_PATTERN = """
<html>
  <head>
   <title>{}</title>
   <meta http-equiv="Content-Type" content="charset=utf-8" />
  </head>
  <body><h1>{}</h1>{}</body>
</html>"""

GROUP_PATTERN = """
<h2> {} </h2>
<table border="0" >
  <tr bgcolor="#c0c0c0">
    <th>Nr.</th><th>Artikelbezeichnung</th><th>Preis</th>
  </tr>
  {}
</table>"""

ROW_PATTERN="""
<tr bgcolor="#c0c0c0">
  <td>{}</td><td>{}</td><td>{} EUR</td>
</tr>"""

import sys
from xml.dom import minidom


class Catalogue(object):
  # Modelliert einen XML-basierten Online-Katalog 
  def __init__(self, path):
    self.doc = minidom.parse(path)
    self.path = path

  def update(self, newItemXML):
    # XML-Dokument des Katalogs aktualisieren
    newItemDoc = minidom.parseString(newItemXML)      #2
    newItem = newItemDoc.documentElement
    groupName = newItem.getAttribute("warengruppe")
    new = newItem.getElementsByTagName("ware")[0]     #3
    self.__insert(new, groupName)                     #4
    f = open(self.path, "w", encoding="utf-8")        #5 
    f.write(self.doc.toxml())
    f.close()

  def __insert(self, new, groupName):
    # neuen Artikel in DOM-Objekt einfuegen 
    groups = self.doc.getElementsByTagName("warengruppe")
    for g in groups:
      if g.getAttribute("name") == groupName:
          g.appendChild(new)
          return

  def getTitle(self):
    # Liefert Titel des Katalogs
    return self.doc.documentElement.getAttribute("titel")

  def getGroupNames(self):
    # Liefert Liste mit Namen der Warengruppen
    groups = self.doc.getElementsByTagName("warengruppe")
    return [g.getAttribute("name") for g in groups]

  def getItems (self, groupName):
    # Liefert Liste mit Artikelbeschreibungen als Tupel
    # der Form (id, preis, beschreibung)
    groups = self.doc.getElementsByTagName("warengruppe")
    for g in groups:
      if g.getAttribute("name") == groupName:
        items = g.getElementsByTagName ("ware")
        return [(i.getAttribute("id"),
                 i.getAttribute("preis"),
                 i.firstChild.data) for i in items]   #6

class CatUpdate(object):
  # Update einer HTML-Seite
  def __init__(self):
      self.catalogue = Catalogue(XMLPATH)
      self.catalogue.update(sys.stdin.read())         #7
      self.updatePresentation()                       
      print("Content-type: text/html",
            "\n\n- Katalog wurde aktualisiert -")

  def makeHtmlGroupDescription(self, groupName):
    items = self.catalogue.getItems(groupName)        #8   
    rows = ""
    for (ID, price, descr) in items:
        rows += ROW_PATTERN.format(ID, descr, price)
    return GROUP_PATTERN.format(groupName, rows)

  def updatePresentation(self):
    title = self.catalogue.getTitle()
    htmlGroups = ""
    for g in self.catalogue.getGroupNames():
      htmlGroups += self.makeHtmlGroupDescription(g)
    htmlAll = HTML_PATTERN.format(title,title,
                                  htmlGroups)         #9
    f = open(HTMLPATH, "w", encoding="utf-8")        #10
    f.write(htmlAll)
    f.close()

CatUpdate()
    













                    
