#! /Python310/pythonw.exe

#----------------------------------------------------
# Dateiname:  videoplayer_dashboard_hide.pyw
# Videoplayer, bei dem das Dashbord ausgeblendet ist.
# Wird die Maus über das Femszter bewegt, wird es eingeblendet.
#
# Python 3,  mitp Verlag
# Kap. 29
# Michael Weigend 11. 06. 2019
#----------------------------------------------------


# videoplayer_dashboard_hide.pyw
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import *
import sys 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.createWidgets()
        self.createLayout()
        self.show()

    def createWidgets(self):
        self.setWindowTitle("Videoplayer")
        self.videoWidget = QVideoWidget(self)
        self.videoWidget.setMinimumSize(320,180)
        self.player = QMediaPlayer(self)
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
        self.dashboard = QFrame(self)
        self.dashboard.resize(300,40)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.dashboard.hide)
     
    def createLayout(self):
        hBox = QHBoxLayout()
        hBox.addWidget(self.playButton)
        hBox.addWidget(self.selectButton)
        hBox.addWidget(self.volumeSlider)
        self.dashboard.setLayout(hBox)
        self.dashboard.move(0, self.height()-self.dashboard.height()- 2)
        vBox = QVBoxLayout()
        vBox.addWidget(self.videoWidget)
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

    def mouseMoveEvent(self, event):
        self.dashboard.show()
        self.timer.start(2000)

    def resizeEvent(self, event):
        self.dashboard.move(0, self.height()-self.dashboard.height()- 2)
     
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())


