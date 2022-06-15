#!/usr/bin/env python3

#----------------------------------------------------
# Dateiname:  videoplayer.pyw
# Ein einfacher Videoplayer
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------


from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *
import sys 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.createLayout()
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Videoplayer")
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setMinimumSize(320,180)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.videoWidget)
        self.player.setVolume(0)
        self.playButton = QPushButton("Start")
        self.playButton.clicked.connect(self.play)
        self.playButton.setEnabled(False)
        self.selectButton = QPushButton("Wähle Video")
        self.selectButton.clicked.connect(self.selectFile)
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.sliderMoved.connect(self.player.setVolume)
        self.volumeSlider.setRange(0, 100) 
     
    def createLayout(self):
        vBox = QVBoxLayout()
        vBox.addWidget(self.videoWidget)
        hBox = QHBoxLayout()
        hBox.addWidget(self.playButton)
        hBox.addWidget(self.selectButton)
        hBox.addWidget(self.volumeSlider)
        vBox.addLayout(hBox)
        self.setLayout(vBox)

    def play (self):
        if self.playButton.text() == "Start":
            self.playButton.setText("Pause")
            self.player.play()         
        else:
            self.playButton.setText("Start")
            self.player.pause()
            
    def selectFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                         "Video öffnen")
        self.media = QMediaContent(QUrl(fileName))
        self.player.setMedia(self.media)
        self.playButton.setEnabled(True)
           
     
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


