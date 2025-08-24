import pygame

pygame.init()

# Dimensioni e colore finestra
LENGTH = 800
HEIGHT = 600  

# Colori (RGB: rosso, verde, blu)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)

FPS = 60

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("1 - Drawing Shapes")

clock = pygame.time.Clock()
executing = True

# Posizione iniziale di un rettangolo (x,y)
rect_x = 100
rect_y = 100

# ----- CICLO PRINCIPALE DEL GIOCO ----- #

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    # ----- AGGIORNAMENTO LOGICA DI GIOCO ----- #

    rect_x += 1             # Spostiamo il rettangolo lentamente
    if rect_x > LENGTH:     # Se esce dalla finestra ricomincia da sinistra
        rect_x = -100

    # Riempiamo lo sfondo con un colore
    window.fill(WHITE)  
    
    # Disegno di un rettangolo
    pygame.draw.rect(window, RED, (rect_x, rect_y, 100, 50))

    # Disegno di un cerchio
    pygame.draw.circle(window, GREEN, (400, 300), 75)

    # Disegno di una linea
    pygame.draw.line(window, BLUE, (50, 500), (750, 500), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()