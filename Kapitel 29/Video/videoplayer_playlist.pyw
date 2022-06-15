#! /Python37/pythonw.exe

#----------------------------------------------------
# Dateiname:  videoplayer_playlist.pyw
# Videoplayer mit Playlist
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------


from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import (QMediaPlayer,
                                QMediaContent, QMediaPlaylist)
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
        self.playlist = QMediaPlaylist()
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.videoWidget)
        self.player.setPlaylist(self.playlist)
        self.playButton = QPushButton("Starte nächstes Video")
        self.playButton.clicked.connect(self.play)
        self.playButton.setEnabled(False)
        self.getButton = QPushButton("Wähle Videos")
        self.getButton.clicked.connect(self.getMovie)
        self.label = QLabel(self, text="Video -/-")
        self.label.setSizePolicy(QSizePolicy.Expanding,
                                 QSizePolicy.Fixed)
        
     
    def createLayout(self):
        vBox = QVBoxLayout()
        vBox.addWidget(self.videoWidget)
        hBox = QHBoxLayout()
        hBox.addWidget(self.playButton)
        hBox.addWidget(self.getButton)
        hBox.addWidget(self.label)
        vBox.addLayout(hBox)
        self.setLayout(vBox)

    def play (self):
        self.playlist.next()
        self.player.play()
        self.label.setText(
            "Video {}/{} ".format(self.playlist.currentIndex() + 1,
                              self.playlist.mediaCount()))
            
    def getMovie(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                         "Neues Video auswählen")
        self.media = QMediaContent(QUrl(fileName))
        self.playlist.addMedia(self.media)
        self.playButton.setEnabled(True)

           
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


