import pygame
from pygame.locals import *

class AppState(Enum):
    NOTHING_IS_HAPPENING = 0
    HAND_OVER_NOT_CENTERED = 1
    HAND_OVER_CENTERED = 2
    SIGN_CORRECT = 3 

class App:
    
      
    def __init__(self):
        #Pygame initialization
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1200, 900
        #Initialize my stuff
        self.programState = AppState.NOTHING_IS_HAPPENING
        self.MotionController = MotionController()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((1100,800), pygame.HWSURFACE)
        self._running = True
        self._image_surf = pygame.image.load("C:/Users/Tetris/Desktop/HCI 2016/images/handhoverleap.jpg").convert()
 
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
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()