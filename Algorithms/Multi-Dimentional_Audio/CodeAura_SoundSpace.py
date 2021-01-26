import math
from math import pi,sin,cos
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.showbase.Audio3DManager import Audio3DManager


#creates a room object, requires parameter of max number of voice users
#author: kevin good
#to run create instance of class followed by soundSpace.run(), where "soundSpace is user chosen variable name

class soundSpace(ShowBase):

    voiceSourceList = [] #List of voice source objects (sound stream from mics)
    musicSource = None #Source of room music (music streaming service)
    musicMgr = None
    seatCoord = [] #List of calculated x,y coordinates of "seats"

    #On init calculates all seat postions
    #builds an audio object at each virtual position
    #builds an audio oject for music (default center of all seats)
    #TODO Connect mic stream to seats
    #TODO Connect music stream to mSource
    #TODO Music source hardcoded toposition x,y
    def __init__(self,capacity):
        self.base = ShowBase.__init__(self)
        theta = 360 / capacity
        for t in range(0, (capacity)):
            x = 5 * (math.cos(math.radians(t * theta)))
            y = 5 * (math.sin(math.radians(t * theta)))
            self.seatCoord.append((x, y, 0))

        #creats voice sound objects
        for x in range(capacity):
            vSource = self.loader.loadModel("cube.egg") #white square visual for sound sources
            vSource.reparentTo(self.render)
            vSource.setScale(.25, .25, .25)
            vSource.setPos(self.seatCoord[x])
            self.voiceSourceList.append(vSource)

        #creates music source object
        self.musicSource = self.loader.loadModel("cube.egg")
        self.musicSource.reparentTo(self.render)
        self.musicSource.setScale(.25, .25, .25)
        self.musicSource.setPos(0, 0, 0) #TODO make position changable


        #Sets camera position to position of first created seat x,y (5,0)
        #camera is used as the listener
        self.musicMgr = self.musicManager
        self.disable_mouse() #comment out to move camera around virtual room, this will change the sound locations, only for visual understanding
        self.camera.setPos(5,0,0) #listener position
        self.camera.setHpr(90,0,0) #listener "view" (straigt ahead)

        audio3d = Audio3DManager(self.musicMgr,self.camera)
        music = audio3d.loadSfx('StarWars60.wav') #hard coded audio sample/ should be source of music stream
        audio3d.attachSoundToObject(music, self.musicSource) #music attached to music source
        music.play()


    #make camera able to be moved when mouse is enabled
    def spinCameraTask(self, task):
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0)
        self.camera.setPos(0,0,15)
        #self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians),3)
        self.camera.setHpr(angleDegrees,0,0)
        return Task.cont

    #TODO
    def addVoiceSource(self):
        return None

    #TODO
    def addMusicSource(self,source):
        return None