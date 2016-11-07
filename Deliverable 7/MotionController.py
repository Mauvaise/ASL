import Leap
from App import App

class MotionController:
    
    def __init__(self): 
        self.controller = Leap.Controller()
        self.frame = self.controller.frame()
        self.app = App()
        
    def set_app(app):        
        App.app = app
    
    def detect_hand(self):
        while True:         
            if not self.frame.hands.is_empty:
                self.app.on_state_change(App.HAND_OVER_NOT_CENTERED)
                #hand = self.frame.hands[0]
                #fingers = hand.fingers
    
                #for i in range(0,5):
                #    finger = fingers[i]
                #    #ax.set_xlim(xMin,xMax)
                #    #ax.set_ylim(yMin,yMax)
                #    #ax.set_zlim(zMin,zMax)
                #    #ax.view_init(azim=90)
                #    #
                #    for j in range(0,4):
                #        bone = finger.bone(j)
                #        tip = bone.next_joint
                #        base = bone.prev_joint
                #        xBase = base[0]
                #        yBase = base[1]
                #        zBase = base[2]
                #        xTip = tip[0]
                #        yTip = tip[1]
                #        zTip = tip[2]
                