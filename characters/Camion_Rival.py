import pygame
import random
from gameclass.Ventana import Ventana 
from gameclass.Carretera import Borde_Derecho, Borde_Izquierdo

class Camion_Rival:
    def __init__(self):
        self.vtn = Ventana()
        self._auto_ancho = 69
        self._auto_alto = 226
        
        self.bi = Borde_Izquierdo(self.vtn)
        self.bd = Borde_Derecho(self.vtn)
        
        self.__stats = {"velocidad":1, "giro":1}
        # self._auto_x = (self.vtn.ventana_display().get_width() - self._auto_ancho) // 2
        self._auto_y = -226
        
        self._velocidad_auto = self.__stats["velocidad"]
        self._auto_image = pygame.image.load('images/truck_enemy.png')
        self._velocidad_auto_giro = self.__stats["giro"]
        self._auto_rect = pygame.Rect(random.randint(self.bi.getborde_izquierdo().right, self.bd.getborde_derecho().left - self._auto_ancho), self._auto_y, self.auto_ancho, self._auto_alto)
    @property
    def auto_ancho(self):
        return self._auto_ancho
    
    @property
    def auto_alto(self):
        return self._auto_alto
    
    @property
    def auto_y(self):
        return self._auto_y
    
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
    
    def auto_create_rect(self):
        self._auto_rect = pygame.Rect(random.randint(self.bi.getborde_izquierdo().right, self.bd.getborde_derecho().left - self._auto_ancho), self._auto_y, self.auto_ancho, self._auto_alto)
    
    def auto_rect(self):
        return self._auto_rect
    
    def pausar(self):
        self._velocidad_auto = 0
        self._velocidad_auto_giro = 0
        
    def reiniciar(self):
        self._velocidad_auto = self.__stats["velocidad"]
        self._velocidad_auto_giro = self.__stats["giro"]
        self._auto_y = -226
    
    # def mover_derecha(self):
    #     self._auto_x -= self._velocidad_auto_giro
        
    # def mover_izquierda(self):
    #     self._auto_x += self._velocidad_auto_giro
    
    def dibujar(self):
        self.vtn.ventana_display().blit(self._auto_image, self._auto_rect)