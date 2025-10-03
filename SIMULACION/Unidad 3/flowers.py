import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Flores y Estrellas Fugaces 🌻✨")

# Colores
NEGRO = (10, 10, 30)
AMARILLO = (255, 220, 50)
CAFE = (80, 50, 30)
VERDE = (50, 200, 100)
BLANCO = (255, 255, 255)

# Lista de estrellas fugaces
estrellas = []

for _ in range(10):
    x = random.randint(0, ANCHO)
    y = random.randint(0, ALTO // 2)
    velocidad = random.uniform(3, 6)
    estrellas.append([x, y, velocidad])

# Función para dibujar una flor
def dibujar_flor(x, y, escala=1.0):
    # Pétalos
    for angulo in range(0, 360, 30):
        rad = math.radians(angulo)
        px = x + math.cos(rad) * 40 * escala
        py = y + math.sin(rad) * 40 * escala
        pygame.draw.ellipse(pantalla, AMARILLO, (px - 20*escala, py - 10*escala, 40*escala, 20*escala))
    # Centro
    pygame.draw.circle(pantalla, CAFE, (x, y), int(20*escala))

# Función para dibujar tallos y hojas
def dibujar_tallo(x, y):
    pygame.draw.line(pantalla, VERDE, (x, y), (x, ALTO-50), 5)
    pygame.draw.ellipse(pantalla, VERDE, (x-30, (y+ALTO)//2, 40, 20))
    pygame.draw.ellipse(pantalla, VERDE, (x-10, (y+ALTO)//2+40, 40, 20))

# Bucle principal
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    pantalla.fill(NEGRO)

    # Dibujar estrellas fugaces
    for estrella in estrellas:
        pygame.draw.circle(pantalla, BLANCO, (int(estrella[0]), int(estrella[1])), 2)
        pygame.draw.line(pantalla, BLANCO, (estrella[0], estrella[1]),
                         (estrella[0] - 15, estrella[1] - 15), 2)
        estrella[0] -= estrella[2]
        estrella[1] += estrella[2]
        if estrella[0] < 0 or estrella[1] > ALTO:
            estrella[0] = random.randint(ANCHO, ANCHO+200)
            estrella[1] = random.randint(0, ALTO//2)
            estrella[2] = random.uniform(3, 6)

    # Dibujar flores
    posiciones = [(400, 300), (350, 320), (450, 320), (375, 250), (425, 250)]
    for (x, y) in posiciones:
        dibujar_tallo(x, y)
        dibujar_flor(x, y)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
