#
#
# Copyright 2023, Jorge Navarro, Derechos comerciales reservados.
# Este obra está bajo una licencia de Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional.
#
#

import sys
import pygame
import json
from gameclass.Ventana import Ventana 
from characters.Auto_Player import Auto_Player 
from characters.Auto_Rival import Auto_Rival
from characters.Moto_Rival import Moto_Rival
from characters.Camion_Rival import Camion_Rival
from gameclass.Carretera import Borde_Derecho, Borde_Izquierdo
from gameclass.claseJuego import Game

vtn = Ventana()
auto_p = Auto_Player()
auto_r = Auto_Rival()
moto_r = Moto_Rival()
camion_r = Camion_Rival()
bi = Borde_Izquierdo(vtn)
bd = Borde_Derecho(vtn)

game = Game(auto_p, auto_r, moto_r, camion_r, vtn)

with open("saveScore.json", "r") as archivo:
    scores = json.load(archivo)

fuente = pygame.font.Font(None, 36)
score = 0
score_surface = fuente.render("Score: {}".format(score), True, (255, 255, 255))
pygame.time.set_timer(pygame.USEREVENT, 1000)

conteo_autos = 0

auto_anterior_bajo = False
moto_anterior_bajo = False
camion_anterior_bajo = False

running = True
paused = False

lineas_centro = []

linea_centro_ancho = 10
linea_centro_alto = 100
linea_centro_x = (vtn.ventana_display().get_width() - linea_centro_ancho) // 2
linea_centro_y = 25

for i in range(4):
    linea_centro = pygame.Rect(linea_centro_x, linea_centro_y, linea_centro_ancho, linea_centro_alto)
    lineas_centro.append(linea_centro)
    linea_centro_y += linea_centro_alto + 75  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if not paused:
                score += 1
                game.systemLevels(score)
            score_surface = fuente.render("Score: {}".format(score), True, (255, 255, 255))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                auto_p.auto_create_rect()
                auto_r.auto_create_rect()
                if score >= 20:
                    moto_r.moto_create_rect()
                if score >= 60:
                    camion_r.auto_create_rect()

                # camion = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - camion_ancho),
                #      camion_y, camion_ancho, camion_alto)
                score = 0
                auto_p.reiniciar()
                auto_r.reiniciar()
                moto_r.reiniciar()
                camion_r.reiniciar()
                paused = not paused
            
    vtn.ventana_display().fill((0, 0, 0))
    vtn.ventana_display().blit(score_surface, (10, 10))
    for linea in lineas_centro:
        pygame.draw.rect(vtn.ventana_display(), (255, 255, 255), linea)
        linea.move_ip(0, auto_p._velocidad_auto)
        if linea.top >= vtn.ventana_display().get_height():
            linea.bottom = 0
            
    bd.dibujar_BDerecho()
    bi.dibujar_BIzquierdo()
    
    auto_p.auto_rect()
    
    if moto_r.moto_rect().colliderect(auto_r.auto_rect()):
        moto_r.moto_create_rect()
        
    if moto_r.moto_rect().colliderect(camion_r.auto_rect()):
        moto_r.moto_create_rect()
        
    if auto_r.auto_rect().colliderect(camion_r.auto_rect()):
        auto_r.auto_create_rect()
    
    if paused:
        pause_text = fuente.render("GAME OVER", True, (255, 0, 0))
        pause_rect = pause_text.get_rect(center=(vtn.obtener_dimensiones().width/2, vtn.obtener_dimensiones().height/2))
        pause_desc_text = pygame.font.Font(None, 24).render("Presiona 'P' para reanudar", True, (255, 255, 255))
        pause_desc_rect = pause_text.get_rect(center=(vtn.obtener_dimensiones().width/2 - 25 , vtn.obtener_dimensiones().height/2 + 30))
        vtn.ventana_display().blit(pause_text, pause_rect)
        vtn.ventana_display().blit(pause_desc_text, pause_desc_rect)
        auto_p.pausar()
        auto_r.pausar()
        moto_r.pausar()
        camion_r.pausar()
        # velocidad_camion = 0
    
    keys = pygame.key.get_pressed()
    
    if auto_p._auto.left > bi.getborde_izquierdo().right:
        if keys[pygame.K_a]:
            auto_p.mover_derecha()
    if auto_p._auto.right < bd.getborde_derecho().left:
        if keys[pygame.K_d]:
            auto_p.mover_izquierda()
    
    if auto_anterior_bajo:
        auto_r.auto_create_rect()
        auto_anterior_bajo = False
    
    if auto_r.auto_rect().top >= vtn.ventana_display().get_height():
        auto_anterior_bajo = True
    
    if moto_anterior_bajo:
        moto_r.moto_create_rect()
        moto_anterior_bajo = False
    
    if moto_r.moto_rect().top >= vtn.ventana_display().get_height():
        moto_anterior_bajo = True
        
    if camion_anterior_bajo:
        camion_r.auto_create_rect()
        camion_anterior_bajo = False
    
    if camion_r.auto_rect().top >= vtn.ventana_display().get_height():
        camion_anterior_bajo = True    
    pygame.time.delay(3)
    
    if score >= 1:
        # pygame.draw.rect(ventana, (255, 43, 123), autoRival)
        auto_r.dibujar()
        auto_r.auto_rect().move_ip(0, auto_r.velocidad_auto)
        
    if score >= 20:
        moto_r.dibujar()
        moto_r.moto_rect().move_ip(0, moto_r._velocidad_moto)

    if score >= 60:
        camion_r.dibujar()
        camion_r.auto_rect().move_ip(0, camion_r._velocidad_auto)
    
    if not paused and (auto_p._auto.colliderect(auto_r.auto_rect()) or auto_p._auto.colliderect(moto_r.moto_rect()) or auto_p._auto.colliderect(camion_r.auto_rect())):
        paused = True
        scores["score"] = score
        print(scores["score"])
    pygame.time.delay(1)
    vtn.ventana_display().blit(auto_p._auto_image, auto_p._auto)
    
    pygame.display.flip()
    pygame.display.update()
    

#
#
# Copyright 2023, Jorge Navarro, Derechos comerciales reservados.
# Este obra está bajo una licencia de Creative Commons Reconocimiento-NoComercial-CompartirIgual 4.0 Internacional.
#
#