import pygame
import sys  
import random

class MisProcesos:
    def __init__(self, pscore, pvelocidad_auto, pvelocidad_auto_giro, pvelocidad_moto, pvelocidad_autoRival):
        self.score = pscore
        self.velocidad_auto = pvelocidad_auto
        self.velocidad_auto_giro = pvelocidad_auto_giro
        self.velocidad_moto = pvelocidad_moto
        self.velocidad_autoRival = pvelocidad_autoRival
        
    def detener(self):
        self.score = 0
        self.velocidad_auto = 0
        self.velocidad_auto_giro = 0
        self.velocidad_autoRival = 0
        self.velocidad_moto = 0  