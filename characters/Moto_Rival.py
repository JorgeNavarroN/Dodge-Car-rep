import pygame
import random
from gameclass.Ventana import Ventana 
from gameclass.Carretera import Borde_Derecho, Borde_Izquierdo

class Moto_Rival:
    def __init__(self):
        self.vtn = Ventana()
        self._moto_ancho = 25
        self._moto_alto = 64
        
        self.bi = Borde_Izquierdo(self.vtn)
        self.bd = Borde_Derecho(self.vtn)
        
        self.__stats = {"velocidad":1, "giro":1}
        # self._moto_x = (self.vtn.ventana_display().get_width() - self._moto_ancho) // 2
        self._moto_y = -64
        
        self._velocidad_moto = self.__stats["velocidad"]
        self._moto_image = pygame.image.load('images/motorbike_enemy.png')
        self._velocidad_moto_giro = self.__stats["giro"]
        self._moto_rect = pygame.Rect(random.randint(self.bi.getborde_izquierdo().right, self.bd.getborde_derecho().left - self._moto_ancho), self._moto_y, self._moto_ancho, self._moto_alto)
    @property
    def moto_ancho(self):
        return self._moto_ancho
    
    @property
    def moto_alto(self):
        return self._moto_alto
    
    @property
    def moto_y(self):
        return self._moto_y
    
    @property
    def velocidad_moto(self):
        return self._velocidad_moto

    @property
    def velocidad_moto_giro(self):
        return self._velocidad_moto_giro

    def setVelociad_moto(self, pvelocidad):
        self._velocidad_moto = pvelocidad
    
    def setVelocidad_moto_giro(self, pgiro):
        self._velocidad_moto_giro = pgiro
    
    def moto_create_rect(self):
        self._moto_rect = pygame.Rect(random.randint(self.bi.getborde_izquierdo().right, self.bd.getborde_derecho().left - self._moto_ancho), self._moto_y, self._moto_ancho, self._moto_alto)
    
    def moto_rect(self):
        return self._moto_rect
    
    def pausar(self):
        self._velocidad_moto = 0
        self._velocidad_moto_giro = 0
        
    def reiniciar(self):
        self._velocidad_moto = self.__stats["velocidad"]
        self._velocidad_moto_giro = self.__stats["giro"]
        self._moto_y = -80
    
    # def mover_derecha(self):
    #     self._auto_x -= self._velocidad_auto_giro
        
    # def mover_izquierda(self):
    #     self._auto_x += self._velocidad_auto_giro
    
    def dibujar(self):
        self.vtn.ventana_display().blit(self._moto_image, self._moto_rect)