import pygame
from gameclass.Ventana import Ventana 

class Auto_Player:
    def __init__(self):
        self.vtn = Ventana()
        self._auto_ancho = 50
        self._auto_alto = 80
        self.__stats = {"velocidad":4, "giro":1}
        self._auto_x = (self.vtn.ventana_display().get_width() - self._auto_ancho) // 2
        self._auto_y = (self.vtn.ventana_display().get_height() + self._auto_alto * 4) // 2
        
        self._velocidad_auto = self.__stats["velocidad"]
        self._auto_image = pygame.image.load('images/car.png')
        self._velocidad_auto_giro = self.__stats["giro"]
        
    
    @property
    def auto_ancho(self):
        return self._auto_ancho
    
    @property
    def auto_alto(self):
        return self._auto_alto
    
    @property
    def auto_x(self):
        return self._auto_x
    
    @property
    def auto_y(self):
        return self._auto_y
    
    def getauto(self):
        return self._auto
    
    @property
    def velocidad_auto(self):
        return self._velocidad_auto

    @property
    def velocidad_auto_giro(self):
        return self._velocidad_auto_giro

    def setVelociad_auto(self, pvelocidad):
        self._velocidad_auto = pvelocidad
    
    def setVelocidad_auto_giro(self, pgiro):
        self._velocidad_auto_giro = pgiro
    
    def auto_rect(self):
        self._auto = pygame.Rect(self._auto_x, self._auto_y, self.auto_ancho, self._auto_alto)
        
    def auto_create_rect(self):
        self._auto_rect = pygame.Rect((self.vtn.ventana_display().get_width() - self._auto_ancho) // 2, self._auto_y, self._auto_ancho, self._auto_alto)
    
    def mover_derecha(self):
        self._auto_x -= self._velocidad_auto_giro
        
    def mover_izquierda(self):
        self._auto_x += self._velocidad_auto_giro
    
    def pausar(self):
        self._velocidad_auto = 0
        self._velocidad_auto_giro = 0
        
    def reiniciar(self):
        self._velocidad_auto = self.__stats["velocidad"]
        self._velocidad_auto_giro = self.__stats["giro"]
    
    def dibujar(self):
        self.vtn.ventana_display().blit(self._auto_image, self._auto)
