# ---------------------------------------------------
# Dateiname: ausgabeformate.py
# Verschiedene Formate einer Tabelle
# Objektorientierte Programmierung mit Python
# Kap. 9 Lösung 2
# Michael Weigend 8. 10. 09
#----------------------------------------------------
liste = [('Gold', 0.1234), ('Silber',23.45), ('Platin', 0.0678)]

for i in liste:
    print(i[0],i[1], end=" // ")
print()
print()

for i in liste:
    print(i[0], i[1], sep="\t")
print()

for i in liste:
    print(i[0],format(i[1],"6.2f"), sep=":\t") 
print()



