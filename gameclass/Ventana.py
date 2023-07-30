import pygame

class Ventana:
    def __init__(self):
        pygame.init()
        self.ventana = pygame.display.set_mode((800, 600))
    
    def ventana_display(self):
        return self.ventana
    
    def obtener_dimensiones(self):
        return self.ventana.get_rect()