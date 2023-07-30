import pygame
from gameclass.Ventana import Ventana 
from characters.Auto_Player import Auto_Player 

class Borde_Derecho:
    def __init__(self, pventana):
        pygame.init()
        self.carP = Auto_Player()
        self.vtn = pventana
        self.borde_derecho_ancho = 10
        self.borde_derecho_alto = self.vtn.ventana_display().get_height()
        self.borde_derecho_x = (self.vtn.ventana_display().get_width() + self.carP.auto_ancho * 10) // 2
        self.borde_derecho_y = (self.vtn.ventana_display().get_height() - self.borde_derecho_alto) // 2
        self.borde_derecho = pygame.Rect(self.borde_derecho_x, self.borde_derecho_y, self.borde_derecho_ancho, self.borde_derecho_alto)

    def getborde_derecho(self):
        return self.borde_derecho
    
    def dibujar_BDerecho(self):
        pygame.draw.rect(self.vtn.ventana_display(), (255, 255, 255), self.borde_derecho)

class Borde_Izquierdo:
    def __init__(self, pventana):
        pygame.init()
        self.carP = Auto_Player()
        self.vtn = pventana
        self.bd = Borde_Derecho(pventana)
        self.borde_izquierdo_ancho = 10
        self.borde_izquierdo_alto = self.vtn.ventana_display().get_height()
        self.borde_izquierdo_x = (self.vtn.ventana_display().get_width() - self.carP.auto_ancho * 10) // 2
        self.borde_izquierdo_y = (self.vtn.ventana_display().get_height() - self.bd.borde_derecho_alto) // 2
        self.borde_izquierdo = pygame.Rect(self.borde_izquierdo_x, self.borde_izquierdo_y, self.borde_izquierdo_ancho, self.borde_izquierdo_alto)

    def getborde_izquierdo(self):
        return self.borde_izquierdo

    def dibujar_BIzquierdo(self):
        pygame.draw.rect(self.vtn.ventana_display(), (255, 255, 255), self.borde_izquierdo)

class Lineas_Centro:
    def __init__(self, pventana):
        pygame.init()
        self.carP = Auto_Player()
        self.vtn = pventana
        self.lineas_centro = []
        self.linea_centro_ancho = 10
        self.linea_centro_alto = 100
        self.linea_centro_x = (self.vtn.ventana_display().get_width() - self.linea_centro_ancho) // 2
        self.linea_centro_y = 25

    