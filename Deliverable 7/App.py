import pygame
from pygame.locals import *
from MotionController import MotionController

class App:
    NOTHING_IS_HAPPENING = 0
    HAND_OVER_NOT_CENTERED = 1
    HAND_OVER_CENTERED = 2
    SIGN_CORRECT = 3
    
    def __init__(self):
        #Pygame initialization
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1200, 900
        #Initialize my stuff
        self.programState = App.NOTHING_IS_HAPPENING
        self.motionController = MotionController()
         
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
        self._display_surf.blit(self._image_surf,(50,50))
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
        self.on_cleanup()  
              
    #def on_state_change(programState):
    #    self.programState = programState
    #    if self.programState == App.NOTHING_IS_HAPPENING:
    #        self._image_surf = pygame.image.load("C:/Users/Tetris/Desktop/HCI 2016/images/handhoverleap.jpg").convert()
    #        
        #elif self.programState == App.HAND_OVER_NOT_CENTERED:
        #
        #elif self.programState == App.HAND_OVER_CENTERED:
        #
        #elif self.programState == App.SIGN_CORRECT:
        #    
            
      
        
        

 

 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()