import sys
import pygame
import random
import json

pygame.init()

with open("saveScore.json", "r") as archivo:
    scores = json.load(archivo)

ventana = pygame.display.set_mode((800, 600))
ventana_rect = ventana.get_rect()

fuente = pygame.font.Font(None, 36)
score = 0
score_surface = fuente.render("Score: {}".format(score), True, (255, 255, 255))
pygame.time.set_timer(pygame.USEREVENT, 1000)

auto_ancho = 50
auto_alto = 80
auto_x = (ventana.get_width() - auto_ancho) // 2
auto_y = (ventana.get_height() + auto_alto * 4) // 2
auto = pygame.Rect(auto_x, auto_y, auto_ancho, auto_alto)

borde_derecho_ancho = 10
borde_derecho_alto = ventana.get_height()
borde_derecho_x = (ventana.get_width() + auto_ancho * 10) // 2
borde_derecho_y = (ventana.get_height() - borde_derecho_alto) // 2
borde_derecho = pygame.Rect(borde_derecho_x, borde_derecho_y, borde_derecho_ancho, borde_derecho_alto)

borde_izquierdo_ancho = 10
borde_izquierdo_alto = ventana.get_height()
borde_izquierdo_x = (ventana.get_width() - auto_ancho * 10) // 2
borde_izquierdo_y = (ventana.get_height() - borde_derecho_alto) // 2
borde_izquierdo = pygame.Rect(borde_izquierdo_x, borde_izquierdo_y, borde_izquierdo_ancho, borde_izquierdo_alto)

conteo_autos = 0

lineas_centro = []

linea_centro_ancho = 10
linea_centro_alto = 100
linea_centro_x = (ventana.get_width() - linea_centro_ancho) // 2
linea_centro_y = 25

autoRival_ancho = 50
autoRival_alto = 80
autoRival_y = -80
autoRival = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - autoRival_ancho),
                            autoRival_y, autoRival_ancho, autoRival_alto)

moto_ancho = 25
moto_alto = 50
moto_y = -80
moto = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - moto_ancho),
                            moto_y, moto_ancho, moto_alto)

camion_ancho = 70
camion_alto = 120
camion_y = -120
camion = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - camion_ancho),
                     camion_y, camion_ancho, camion_alto)

for i in range(4):
    linea_centro = pygame.Rect(linea_centro_x, linea_centro_y, linea_centro_ancho, linea_centro_alto)
    lineas_centro.append(linea_centro)
    linea_centro_y += linea_centro_alto + 75  
    
auto_anterior_bajo = False
moto_anterior_bajo = False
camion_anterior_bajo = False

velocidad_auto = 3
velocidad_auto_giro = 0.8
velocidad_moto = 1
velocidad_camion = 1
velocidad_autoRival = 2
running = True
paused = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if not paused:
                score += 1
            score_surface = fuente.render("Score: {}".format(score), True, (255, 255, 255))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                auto = pygame.Rect((ventana.get_width() - auto_ancho) // 2, auto_y, auto_ancho, auto_alto)
                autoRival = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - autoRival_ancho),
                            autoRival_y, autoRival_ancho, autoRival_alto)
                moto = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - moto_ancho),
                            moto_y, moto_ancho, moto_alto)
                camion = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - camion_ancho),
                     camion_y, camion_ancho, camion_alto)
                score = -1
                velocidad_auto = 3
                velocidad_auto_giro = 0.8
                velocidad_autoRival = 2
                velocidad_moto = 1
                velocidad_camion = 1
                paused = not paused
            
    ventana.fill((0, 0, 0))
    ventana.blit(score_surface, (10, 10))
    for linea in lineas_centro:
        pygame.draw.rect(ventana, (255, 255, 255), linea)
        linea.move_ip(0, velocidad_auto)
        if linea.top >= ventana.get_height():
            linea.bottom = 0
                
    
    pygame.draw.rect(ventana, (255, 255, 255), borde_derecho)
    pygame.draw.rect(ventana, (255, 255, 255), borde_izquierdo)
    
    
    auto = pygame.Rect(auto_x, auto_y, auto_ancho, auto_alto)
    
    if not paused and (auto.colliderect(autoRival) or auto.colliderect(moto) or auto.colliderect(camion)):
        paused = True
        scores["score"] = score
        print(scores["score"])
    
    if paused:
        pause_text = fuente.render("GAME OVER", True, (255, 0, 0))
        pause_rect = pause_text.get_rect(center=(ventana_rect.width/2, ventana_rect.height/2))
        ventana.blit(pause_text, pause_rect)
        velocidad_auto = 0
        velocidad_auto_giro = 0
        velocidad_autoRival = 0
        velocidad_moto = 0
        velocidad_camion = 0
    keys = pygame.key.get_pressed()
    
    if auto.left > borde_izquierdo.right:
        if keys[pygame.K_a]:
            auto_x -= velocidad_auto_giro
    if auto.right < borde_derecho.left:
        if keys[pygame.K_d]:
            auto_x += velocidad_auto_giro
        
    if auto_anterior_bajo:
        autoRival = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - autoRival_ancho),
                            autoRival_y, autoRival_ancho, autoRival_alto)
        auto_anterior_bajo = False
    
    if autoRival.top >= ventana.get_height():
        auto_anterior_bajo = True
    
    if moto_anterior_bajo:
        moto = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - moto_ancho),
                            moto_y, moto_ancho, moto_alto)
        moto_anterior_bajo = False
    
    if moto.top >= ventana.get_height():
        moto_anterior_bajo = True
    
    if camion_anterior_bajo:
        camion = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - camion_ancho),
                     camion_y, camion_ancho, camion_alto)
        camion_anterior_bajo = False
    
    if camion.top >= ventana.get_height():
        camion_anterior_bajo = True
    
    
    pygame.time.delay(3)
    pygame.draw.rect(ventana, (255, 43, 123), autoRival)
    autoRival.move_ip(0, velocidad_autoRival)
    if score >= 20:  
        pygame.draw.rect(ventana, (34, 12, 244), moto)
        moto.move_ip(0, velocidad_moto)

    if score >= 40:
        if not paused:
            velocidad_auto = 4
            velocidad_auto_giro = 1
            velocidad_autoRival = 3
            velocidad_moto = 2
    
    if score >= 60:
        pygame.draw.rect(ventana, (10, 252, 74), camion)
        camion.move_ip(0, velocidad_camion)
        
    if score >= 80:
        if not paused:
            velocidad_auto = 5
            velocidad_auto_giro = 1.2
            velocidad_autoRival = 4
            velocidad_moto = 3
            velocidad_camion = 2
    if score >= 100:
        if not paused:
            velocidad_auto = 6
            velocidad_auto_giro = 1.4
            velocidad_autoRival = 5
            velocidad_moto = 4
            velocidad_camion = 3
    
    pygame.time.delay(1)
    pygame.draw.rect(ventana, (255, 0, 0), auto)
    pygame.display.flip()
    pygame.display.update()
    
