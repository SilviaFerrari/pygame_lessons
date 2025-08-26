import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
FPS = 60

BCKS_PATH = 'assets/backgrounds'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("8.1 - Simple Backgroung")

clock = pygame.time.Clock()
executing = True

# Caricamento dello sfondo
background = pygame.image.load(os.path.join(BCKS_PATH, 'village_map.png')).convert()

# Se vuoi adattarlo alla finestra (opzionale)
background = pygame.transform.scale(background, (LENGTH, HEIGHT))

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    # Disegna lo sfondo all'angolo in alto a sinistra
    window.blit(background, (0, 0))   
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()