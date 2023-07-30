import pygame
import random
from gameclass.Ventana import Ventana 
from characters.Auto_Player import Auto_Player 
from characters.Auto_Rival import Auto_Rival
from characters.Moto_Rival import Moto_Rival
from characters.Camion_Rival import Camion_Rival

pygame.init()

class Game:
    def __init__(self, pauto_p : Auto_Player, pauto_r : Auto_Rival, pmoto_r : Moto_Rival, pcamion_r : Camion_Rival, pventana : Ventana):
        self.vtn = pventana
        self.auto_p = pauto_p
        self.auto_r = pauto_r
        self.moto_r = pmoto_r
        self.camion_r = pcamion_r
        
    def systemLevels(self, score) -> None:
        if score % 50 == 0:
            self.moto_r._velocidad_moto += 1
            self.auto_p._velocidad_auto += 1
            self.auto_r._velocidad_auto += 1
            if score >= 60:
                self.camion_r._velocidad_auto += 1

            