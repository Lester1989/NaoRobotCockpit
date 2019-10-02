# -*- encoding: UTF-8 -*-
#
# This is a tiny example that shows how to show live images from Nao using PyQt.
# You must have python-qt4 installed on your system.
#

import sys
import math
import time

from PyQt4.QtGui import QWidget, QImage, QApplication, QPainter,QColor,QPolygon,QPen,QFont,QBrush, QInputDialog
from PyQt4 import QtCore
from naoqi import ALProxy
import grabSmall
import grabLarge
import grabBall
import grabBottle
import speechOutput as dialog

# To get the constants relative to the video.
import vision_definitions

arrowPolygon= QPolygon()
arrowPolygon <<QtCore.QPoint(18,24)<<QtCore.QPoint( 18,3)<<QtCore.QPoint(12,9)<<QtCore.QPoint(24,9)<<QtCore.QPoint(18,3)


class ImageWidget(QWidget):
    """
    Tiny widget to display camera images from Naoqi.
    """
    def __init__(self, IP, PORT, CameraID,attitude, parent=None):
        """
        Initialization.
        """
        QWidget.__init__(self, parent)
        self._image = QImage()
        self.setWindowTitle('Nao')

        self._imgWidth = 1280
        self._imgHeight = 960
        self._cameraID = CameraID
        self.resize(self._imgWidth, self._imgHeight)

        # Proxy to ALVideoDevice.
        self._videoProxy = None
        
        # Proxies for Motion and Posture
        self._postureProxy = None 
        self._motionProxy = None
        self._walkSpeed = 0.4
        self._currentSpeeds = {'Forward':0,'Leftward':0,'CounterClockwise':0}
        
        self._currentMovement = 'IDLE'
        # Our video module name.
        self._imgClient = ""

        # This will contain this alImage we get from Nao.
        self._alImage = None

        self._registerImageClient(IP, PORT)
        self._registerPostureAndMotionClient(IP,PORT)

        # Trigget 'timerEvent' every 100 ms.
        self.startTimer(100)
        
        #init Speech Module
        dialog.set_params(attitude,IP,PORT)
        self._attitude = attitude
        
        self._typing = False

    def _registerPostureAndMotionClient(self,IP,PORT):
        self._postureProxy = ALProxy('ALRobotPosture', IP, PORT)
        self._motionProxy = ALProxy("ALMotion", IP, PORT)
        self._motionProxy.setWalkArmsEnabled(False,False)
        
        
        
    def _registerImageClient(self, IP, PORT):
        """
        Register our video module to the robot.
        """
        self._videoProxy = ALProxy("ALVideoDevice", IP, PORT)
        resolution = vision_definitions.kQVGA  # 320 * 240
        colorSpace = vision_definitions.kRGBColorSpace
        self._imgClient = self._videoProxy.subscribe("_client", resolution, colorSpace, 5)

        # Select camera.
        self._videoProxy.setParam(vision_definitions.kCameraSelectID,
                                  self._cameraID)


    def _unregisterImageClient(self):
        """
        Unregister our naoqi video module.
        """
        if self._imgClient != "":
            self._videoProxy.unsubscribe(self._imgClient)

            
    def rotatePolygon(self,polygon,degree=0,position=[0,0]):
        theta = math.radians(degree)
        cosang,sinang = math.cos(theta),math.sin(theta)
        n = len(polygon)
        cx = sum(p.x() for p in polygon)/n
        cy = sum(p.y() for p in polygon)/n
        rotatePolygon = QPolygon()
        for p in polygon:
            tx,ty = p.x()-cx,p.y()-cy
            rotatePolygon.append(QtCore.QPoint(tx*cosang+ty*sinang+cx+position[0],-tx*sinang+ty*cosang+cy+position[1]))
        return rotatePolygon
        
    def drawMoreText(self,painter,posX,posY,textlines):
        painter.fillRect(posX-5,posY-25,325,(len(textlines)+1)*20+10,QBrush(QColor(128,128,128,128)))
        for nr,line in enumerate(textlines):
            painter.drawText(posX,posY+nr*20,line)

    def paintEvent(self, event):
        """
        Draw the QImage on screen.
        """
        textPosX,textPosY = 10,200
        painter = QPainter(self)
        painter.drawImage(painter.viewport(), self._image)
        innerFont = QFont()
        innerFont.setPointSize(12)
        painter.setFont(innerFont)
        painter.setPen(QColor(QtCore.Qt.white))
        painter.drawText(10,180,'Current Action:')
        painter.drawText(10,200,self._currentMovement)
        self.drawMoreText(painter,10,300,['Control Buttons:',
        'w,s - Walking Forwards/Backwards',
        'q,e - Walking Left/Right',
        'a,d - Turning Left/Right',
        'x - stopping',
        'Space - standing up',
        'Ctrl - crouch',
        'Escape,Enter - restMode, wakeUp',
        '1 - Grabbing small',
        '2 - Grabbing large',
        '3 - Grabbing Kuscheltier',
        '4 - Grabbing bottle'])
        self.drawMoreText(painter,self.width()-300-25,300,['Dialog Control:({})'.format(self._attitude),
        'u - Introduction',
        'i - Ask for object',
        'h - Object is Somat',
        'j - Object is Muesli',
        'k - Object is Bottle',
        'l - Object is Kuscheltier',
        'n - Wertstoff',
        'm - Altpapier', 
        'o - Ask for help',
        'z - Ask proband to repeat sentence',
        'p - Repeat task',
        '0(Null) - construct initial state',
        't - Goodbye',
        'b - thanks',
        '# - Start free Speech(PopUp)'])
        self.drawMoreText(painter,100,50,['Movement Speeds','Forward: {}'.format(self._currentSpeeds['Forward']),'Leftward: {}'.format(self._currentSpeeds['Leftward']),'CounterClockwise: {}'.format(self._currentSpeeds['CounterClockwise'])])
        pen = QPen()
        pen.setColor(QColor(QtCore.Qt.red))
        pen.setWidth(5)
        painter.setPen(pen)
        painter.drawEllipse(20,15,60,30)
        pen.setColor(QColor(QtCore.Qt.blue))
        painter.setPen(pen)
        painter.drawPolygon(self.rotatePolygon(arrowPolygon,math.degrees(self._motionProxy.getAngles('HeadYaw',True)[0]),[30,20]))
        


    def _updateImage(self):
        """
        Retrieve a new image from Nao.
        """
        self._alImage = self._videoProxy.getImageRemote(self._imgClient)
        self._image = QImage(self._alImage[6],           # Pixel array.
                             self._alImage[0],           # Width.
                             self._alImage[1],           # Height.
                             QImage.Format_RGB888)


    def timerEvent(self, event):
        """
        Called periodically. Retrieve a nao image, and update the widget.
        """
        self._updateImage()
        #print(self._motionProxy.getRobotVelocity())
        self.update()


    def __del__(self):
        """
        When the widget is deleted, we unregister our naoqi video module.
        """
        self._unregisterImageClient()
        
    def changePosture(self,newPosture):
        self._postureProxy.goToPosture(newPosture,0.5)#StandInit, Stand, Crouch
        
    def walk(self,x,y,theta,increment=False):
        if increment:
            self._currentSpeeds['Forward'] +=x
            self._currentSpeeds['Leftward']+=y
            self._currentSpeeds['CounterClockwise']+=theta
            self._motionProxy.setWalkTargetVelocity(self._currentSpeeds['Forward'],self._currentSpeeds['Leftward'],self._currentSpeeds['CounterClockwise'],self._walkSpeed)
        else:
            self._currentSpeeds = {'Forward':x,'Leftward':y,'CounterClockwise':theta}
            self._motionProxy.setWalkTargetVelocity(x, y, theta, self._walkSpeed)
        
    def moveHead(self,yaw=0,pitch=0):
        self._motionProxy.changeAngles(['HeadYaw','HeadPitch'],[math.radians(yaw),math.radians(pitch)],0.25)
        
    
        
    def keyPressEvent(self,event):
        if self._typing:            
            event.accept()
            return
    
        if event.key() == QtCore.Qt.Key_Space:
            self.walk(0,0,0)
            time.sleep(0.25)
            self._currentMovement = 'Standing'
            self.changePosture('StandInit')
        elif event.key() == QtCore.Qt.Key_Control:
            self.walk(0,0,0)
            time.sleep(0.25)
            self._currentMovement = 'Crouching'
            self.changePosture('Crouch')
        elif event.key() == QtCore.Qt.Key_W:
            self._currentMovement = 'Walking forward'
            self.walk(0.25,0,0,True)    
        elif event.key() == QtCore.Qt.Key_S:
            self._currentMovement = 'Walking backward'
            self.walk(-0.25,0,0,True)    
        elif event.key() == QtCore.Qt.Key_A:
            self._currentMovement = 'Turning Left'
            self.walk(0,0,math.radians(5),True)    
        elif event.key() == QtCore.Qt.Key_D:
            self._currentMovement = 'Turning Right'
            self.walk(0,0,math.radians(-5),True)
        elif event.key() == QtCore.Qt.Key_Q:
            self._currentMovement = 'Walking Left'
            self.walk(0,0.25,0,True)    
        elif event.key() == QtCore.Qt.Key_E:
            self._currentMovement = 'Walking Right'
            self.walk(0,-0.25,0,True)    
        elif event.key() == QtCore.Qt.Key_X:
            self._currentMovement = 'Stopping'
            self.walk(0,0,0)
        elif event.key() == QtCore.Qt.Key_Left:
            self.moveHead(yaw=2.5)
        elif event.key() == QtCore.Qt.Key_Right:
            self.moveHead(yaw=-2.5)
        elif event.key() == QtCore.Qt.Key_Up:
            self.moveHead(pitch=-2.5)
        elif event.key() == QtCore.Qt.Key_Down:        
            self.moveHead(pitch=2.5)
        elif event.key() == QtCore.Qt.Key_Escape:
            self._currentMovement = 'Resting'
            self._motionProxy.rest()
        elif event.key() == QtCore.Qt.Key_Enter:
            self._currentMovement = 'Standing'
            self._motionProxy.wakeUp()
        elif event.key() == QtCore.Qt.Key_1: 
            self._currentMovement = 'Grabbing Small'   
            self._motionProxy.angleInterpolationBezier(grabSmall.names, grabSmall.times, grabSmall.keys)
        elif event.key() == QtCore.Qt.Key_2:    
            self._currentMovement = 'Grabbing Large'
            self._motionProxy.angleInterpolationBezier(grabLarge.names, grabLarge.times, grabLarge.keys)
        elif event.key() == QtCore.Qt.Key_3:    
            self._currentMovement = 'Grabbing Kuscheltier'
            self._motionProxy.angleInterpolationBezier(grabBall.names, grabBall.times, grabBall.keys)
        elif event.key() == QtCore.Qt.Key_4:    
            self._currentMovement = 'Grabbing Bottle'
            self._motionProxy.angleInterpolationBezier(grabBottle.names, grabBottle.times, grabBottle.keys)
        elif event.key() == QtCore.Qt.Key_U:  
            dialog.welcome()
        elif event.key() == QtCore.Qt.Key_I:  
            dialog.ask_what_object()
        elif event.key() == QtCore.Qt.Key_H:  
            dialog.ask_what_bin('somat')
        elif event.key() == QtCore.Qt.Key_J:  
            dialog.ask_what_bin('vitalis')
        elif event.key() == QtCore.Qt.Key_K:  
            dialog.ask_what_bin('flasche')
        elif event.key() == QtCore.Qt.Key_L:  
            dialog.ask_what_bin('Kuscheltier')
        elif event.key() == QtCore.Qt.Key_N:  
            dialog.confirm('wertstoff')
        elif event.key() == QtCore.Qt.Key_M:  
            dialog.confirm('altpapier')
        elif event.key() == QtCore.Qt.Key_O:  
            dialog.ask_for_help()
        elif event.key() == QtCore.Qt.Key_Z:  
            dialog.proband_repeat()
        elif event.key() == QtCore.Qt.Key_P:  
            dialog.repeat()
        elif event.key() == QtCore.Qt.Key_T:  
            dialog.goodbye()
        elif event.key() == QtCore.Qt.Key_B:  
            dialog.thank_you()
        elif event.key() == QtCore.Qt.Key_0:  
            dialog.initial_state()
        elif event.key() == 35:# die #-Taste
            self._typing = True
            freeSpeech,ok = QInputDialog.getText(self,'Direct Speech','Let Nao say:')
            if ok:
                dialog.free_speech(freeSpeech)
            self._typing = False
        else:
            print event.key()
        event.accept()
        
    



if __name__ == '__main__':
    #IP = "169.254.237.25"  # Replace here with your NaoQi's IP address.
    #IP = "169.254.49.47"  # Replace here with your NaoQi's IP address.
    #IP = "169.254.129.144"  # Replace here with your NaoQi's IP address.
    IP = "169.254.39.105"  # Replace here with your NaoQi's IP address.
    PORT = 9559
    CameraID = 0
    conditionsNumber = 0
    # Read ConditionsNumber from first argument if any.
    if len(sys.argv) > 1:
        conditionsNumber = int(sys.argv[1])


    conditions = ['friendly','submissive','neutral']
    app = QApplication(sys.argv)
    myWidget = ImageWidget(IP, PORT, CameraID,conditions[conditionsNumber])
    myWidget.show()
    sys.exit(app.exec_())