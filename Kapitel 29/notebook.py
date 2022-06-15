#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  notebook.py
# Kalender, in den man Notizen eintragen kann
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

import sys, pickle
from PyQt5.QtWidgets import (QApplication, QCalendarWidget, QHBoxLayout, 
        QMessageBox, QPushButton, QTextEdit, QVBoxLayout, QWidget)
PATH = "notes.dat"                        

class NoteBook ():
    def __init__(self):
        try:
            f = open(PATH, "rb")
            self.notes = pickle.load(f)
            f.close()
        except:
            f = open(PATH, "wb")
            self.notes = dict()
            f.close()

    def addNote(self, note, d):
        self.notes[d] = note
        f = open(PATH, "wb")
        pickle.dump(self.notes, f)
        f.close()

    def getNote(self, d):
        if d in self.notes.keys():
            return self.notes[d]  
        else: return ""

class CalendarNotes(QWidget):
    def __init__(self):
        super().__init__()
        self.notes = NoteBook()

        # Widgets
        self.setWindowTitle("Tagebuch")
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.editor = QTextEdit(self) 
        self.editor.setReadOnly(True)
        self.bEdit = QPushButton("&Edit", self)
        self.bCancel = QPushButton("&Abbrechen", self)
        self.bSave = QPushButton("&Speichern", self)

        # Layout
        vBox1 = QVBoxLayout()
        vBox1.addWidget(self.cal)
        vBox1.addWidget(self.editor)
        vBox2 = QVBoxLayout()
        vBox2.addWidget(self.bEdit)
        vBox2.addWidget(self.bCancel)
        vBox2.addWidget(self.bSave)
        vBox2.addStretch()
        hBox = QHBoxLayout()
        hBox.addLayout(vBox1)
        hBox.addLayout(vBox2)
        self.setLayout(hBox)

        # Connections
        self.bEdit.clicked.connect(self.editNote)
        self.bCancel.clicked.connect(self.display)
        self.bSave.clicked.connect(self.save)
        self.cal.selectionChanged.connect(self.display)

        self.display()
        self.show()

    def save(self):
        d = self.cal.selectedDate().toString()
        self.notes.addNote(self.editor.toPlainText(), d)
        QMessageBox.information(self, "Tagebuch",
                                "Änderung gespeichert")
        self.display() 

    def editNote(self):
        self.bSave.show()
        self.bCancel.show()
        self.editor.setReadOnly(False)

    def display(self):
        self.bSave.hide()
        self.bCancel.hide()
        d = self.cal.selectedDate().toString()
        self.editor.setText(self.notes.getNote(d))
        self.editor.setReadOnly(True)

app = QApplication(sys.argv)
notes = CalendarNotes()
sys.exit(app.exec_())
