#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  videoplayer_aufgabe_1.pyw
# Videoplayer mit zusätzlichen Funktionen
#
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap                 #1
import sys

class Video(QVideoWidget):
    def __init__(self, master):
        super().__init__(master)

    def keyPressEvent(self, event):
        self.setFullScreen(False)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.createWidgets()
        self.createLayout()
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Videoplayer")
        self.videoWidget = Video(self)
        self.videoWidget.setMinimumSize(320,180)
        self.player = QMediaPlayer(self)
        self.player.setVideoOutput(self.videoWidget)
        self.player.setVolume(0)
        self.playButton = QPushButton("Start")
        self.playButton.clicked.connect(self.play)
        self.playButton.setEnabled(False)
        self.selectButton = QPushButton("Wähle Video")
        self.selectButton.clicked.connect(self.selectFile)
        self.fullButton = QPushButton("Vollbild")
        self.fullButton.clicked.connect(self.fullScreen)
        
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.sliderMoved.connect(self.player.setVolume)
        self.volumeSlider.setRange(0, 100)
        self.contrastSlider = QSlider(Qt.Horizontal)
        self.contrastSlider.sliderMoved.connect(
                    self.videoWidget.setContrast)
        self.contrastSlider.setRange(-100, 100)
        self.volumeLabel =  QLabel()                        #2
        self.volumeLabel.setPixmap(QPixmap("volume.png"))
        self.contrastLabel =  QLabel()                        #3
        self.contrastLabel.setPixmap(QPixmap("contrast.png"))
        self.messageLabel = QLabel(self)
        self.messageLabel.move(30, 30)
        self.messageLabel.hide()
    
        
     
    def createLayout(self):
        vBox = QVBoxLayout()
        vBox.addWidget(self.videoWidget)
        hBox1 = QHBoxLayout()
        hBox1.addWidget(self.playButton)
        hBox1.addWidget(self.selectButton)
        hBox1.addWidget(self.fullButton)
        hBox2 = QHBoxLayout()
        hBox2.addWidget(self.volumeLabel)
        hBox2.addWidget(self.volumeSlider)
        hBox2.addWidget(self.contrastLabel)
        hBox2.addWidget(self.contrastSlider)
        vBox.addLayout(hBox1)
        vBox.addLayout(hBox2)
        self.setLayout(vBox)

    def play (self):
        if self.playButton.text() == "Start":
            self.playButton.setText("Pause")
            self.messageLabel.hide()
            self.player.play()         
        else:
            self.playButton.setText("Start")
            self.messageLabel.setText(
                    "Position: {} Sekunden".format(
                    round(self.player.position()/1000))
                    )
            self.messageLabel.adjustSize()
            self.messageLabel.show()
            self.player.pause()
           
    def selectFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                         "Video öffnen")
        self.media = QMediaContent(QUrl(fileName))
        self.player.setMedia(self.media)
        self.playButton.setEnabled(True)

    def fullScreen(self):
        self.videoWidget.setFullScreen(True)


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


