import pygame

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)
FPS = 60

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Gioco di esempio")

clock = pygame.time.Clock()
executing = True

seal = pygame.image.load("seal.png")  # carica l’immagine
seal = pygame.transform.scale(seal, (200, 150))  # ridimensiona l’immagine
seal_x = 0  # posizione iniziale sull’asse X
seal_y = HEIGHT // 2 - seal.get_height() // 2  # centra l’immagine verticalmente
seal_speed = 2  # velocità di movimento (pixel per frame)

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    seal_x += seal_speed  # sposta l’immagine verso destra
    if seal_x > LENGTH:   # se esce dallo schermo a destra
        seal_x = -seal.get_width()  # ricomincia da sinistra

    window.fill(BACKGROUND_COLOR)
    
    # --- NUOVE RIGHE --- #
    window.blit(seal, (seal_x, seal_y))  # disegna l’immagine nella posizione attuale
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()