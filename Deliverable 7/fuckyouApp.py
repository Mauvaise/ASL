import pygame
from pygame.locals import *
import Leap

class MotionListener(Leap.Listener):
    def on_frame(self, controller):
        print "Frame available"
        #if not frame().hands.is_empty:
        #    print "There's a hand!"
        #        #self.on_state_change(HAND_OVER_NOT_CENTERED)
    

class App:   
    def __init__(self):
        #Pygame initialization
        self._running = True
        self._display_surf = True
        self.size = self.weight, self.height = 1200, 900
        #Initialize my stuff
        self.programState = 0
        self.controller = Leap.Controller()
        #listener = MotionListener()
        #self.controller.add_listener(listener)
        self.frame = self.controller.frame()
        self.red = (255,0,0)

         
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((1100,800), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
   
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
            
    def on_loop(self):
        pass
        
    def on_render(self):
        #self._display_surf.blit(self.handHover,(50,50))
        pygame.display.flip()        
        pass
        
    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            print "Running..."
            self.frame = self.controller.frame()
            print self.frame
            if not self.frame.hands.is_empty:
                self.on_state_change(1)
            else:
                self.on_state_change(0)
        self.on_cleanup()  
              
    def on_state_change(self, programState):
        self.programState = programState
        
        if self.programState == 0:
            print "I'm here"
            self.handHover = pygame.image.load("C:/Users/Tetris/Desktop/HCI 2016/images/handhoverleap.jpg").convert()
            self._display_surf.blit(self.handHover,(200,200))   
            
        elif self.programState == 1:
            self.wireframe = pygame.draw.lines(self._display_surf, red, (xBase, yBase, zBase), (xTip, yTip, zTip), 1)
            
            
        elif self.programState == 1:
            self.arrows = pygame.image.load("C:/Users/Tetris/Desktop/HCI 2016/images/leapaxes.jpg").convert()
            self._display_surf.blit(self.arrows,(200,200))
        
            
        #elif self.programState == App.HAND_OVER_CENTERED:
        #
        #elif self.programState == App.SIGN_CORRECT:
        #   

    #def detect_hand(self):
    #    if self.frame.is_valid:         
    #        if not self.frame.hands.is_empty:
    #            self.on_state_change(HAND_OVER_NOT_CENTERED)
                    
      
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()