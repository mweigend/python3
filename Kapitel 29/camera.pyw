#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  camera.pyw
# Fotos aufnehmen und speichern
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

# camera.pyw
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import (QCamera,
                                QCameraImageCapture)
from PyQt5.QtMultimediaWidgets import QVideoWidget
import sys, time

class Window(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.createWidgets()
        self.createCamera()
        self.createLayout()
        self.show()

    def takePhoto(self):
        if self.imageCapture.isReadyForCapture():
            path = 'c:\\media\\foto{}.jpg'.format(time.time())    #Pfad anpassen
            self.imageCapture.capture(path)
            
    def createWidgets(self):
        self.videoWidget = QVideoWidget()
        self.button = QPushButton("Foto")
        self.button.clicked.connect(self.takePhoto)
   
    def createLayout(self):
        self.box = QVBoxLayout()
        self.box.addWidget(self.videoWidget)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

    def createCamera(self):
        self.device = QCamera.availableDevices()[0]
        self.camera = QCamera(self.device)
        self.camera.setViewfinder(self.videoWidget)
        self.camera.setCaptureMode(
                    QCamera.CaptureStillImage)
        self.imageCapture = QCameraImageCapture(
                    self.camera)
        self.camera.start() # Startet Sucherbild

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
