import sys
import pygame
import random

pygame.init()

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

autosRivales = []
autoRival_ancho = 50
autoRival_alto = 80
autoRival_y = -80
autoRival = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - autoRival_ancho),
                            autoRival_y, autoRival_ancho, autoRival_alto)
conteo_autos = 0


lineas_centro = []

linea_centro_ancho = 10
linea_centro_alto = 100
linea_centro_x = (ventana.get_width() - linea_centro_ancho) // 2
linea_centro_y = 25

for i in range(4):
    linea_centro = pygame.Rect(linea_centro_x, linea_centro_y, linea_centro_ancho, linea_centro_alto)
    lineas_centro.append(linea_centro)
    linea_centro_y += linea_centro_alto + 75  
    
print(autosRivales)

auto_anterior_choco = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            score += 1
            score_surface = fuente.render("Score: {}".format(score), True, (255, 255, 255))
            
    ventana.fill((0, 0, 0))
    ventana.blit(score_surface, (10, 10))
    for linea in lineas_centro:
        pygame.draw.rect(ventana, (255, 255, 255), linea)
        linea.move_ip(0, 1)
        if linea.top >= ventana.get_height():
            linea.bottom = 0
                
    
    pygame.draw.rect(ventana, (255, 255, 255), borde_derecho)
    pygame.draw.rect(ventana, (255, 255, 255), borde_izquierdo)
            
    auto = pygame.Rect(auto_x, auto_y, auto_ancho, auto_alto)
    
    keys = pygame.key.get_pressed()
    if auto.left > borde_izquierdo.right:
        if keys[pygame.K_a]:
            auto_x -= 0.8
    if auto.right < borde_derecho.left:
        if keys[pygame.K_d]:
            auto_x += 0.8
        
    if auto_anterior_choco:
        autoRival = pygame.Rect(random.randint(borde_izquierdo.right, borde_derecho.left - autoRival_ancho),
                            autoRival_y, autoRival_ancho, autoRival_alto)
        auto_anterior_choco = False
    
    if autoRival.top >= ventana.get_height():
        auto_anterior_choco = True
    
    pygame.time.delay(3)
    pygame.draw.rect(ventana, (255, 43, 123), autoRival)
    autoRival.move_ip(0, 1)
    pygame.time.delay(1)
    pygame.draw.rect(ventana, (255, 0, 0), auto)
    pygame.display.update()
    
