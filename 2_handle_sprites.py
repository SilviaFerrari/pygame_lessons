import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 100)
FPS = 60

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Gioco di esempio")

clock = pygame.time.Clock()
executing = True

# ----- GESTIONE DI UNA SPRITE ----- #

seal = pygame.image.load(os.path.join('assets', 'seal.png')).convert_alpha()  # Carico l'immagine dalla cartella "assets"

seal = pygame.transform.scale(seal, (200, 150))     # Ridimensiono l’immagine
seal_x = 0                                          # Definisco la coordinata iniziale sull’asse X
seal_y = HEIGHT // 2 - seal.get_height() // 2       # Definisco la coordinata iniziale sull’asse Y (centro verticalmente)
seal_speed = 2                                      # Definisco la velocità di movimento (pixel per frame)

''' 
    La coordinata (0,0) è l'angolo sinistro in alto.
    L'asse X cresce positivamente verso destra.
    L'asse Y cresce positivamente verso il basso. 
'''

# ----- RIDIMENSIONAMENTO DINAMICO ----- #
# Assicura che l'immagine sia sempre proporzionata alla finestra.
'''
scale_w = LENGTH // 4   # Calcolo la larghezza
scale_h = HEIGHT // 4   # Calcolo l'altezza
seal = pygame.transform.scale(seal, (scale_w, scale_h))
'''

# ----- RIDIMENSIONAMENTO PROPORZIONALE ----- #
# Ridimensiona l'immagine mantenendone le proporzioni originali.
'''
orig_w, orig_h = seal.get_size()
scale_factor = 0.5
seal = pygame.transform.scale(seal, (int(orig_w * scale_factor), int(orig_h * scale_factor)))
'''

# ----- ROTAZINE E FLIP ----- #

seal_rotated = pygame.transform.rotate(seal, 45)            # Nuova sprite con rotazione di 45°
seal_flipped = pygame.transform.flip(seal, True, False)     # Nuova sprite con flip orizzontale

# ----- CICLO PRINCIPALE DEL GIOCO ----- #

while executing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            executing = False           

    # ----- AGGIORNAMENTO LOGICA DI GIOCO ----- #  

    seal_x += seal_speed            # Sposta l’immagine verso destra
    if seal_x > LENGTH:             # Se esce dallo schermo a destra
        seal_x = -seal.get_width()  # Ricomincia da sinistra
    
    window.fill(BACKGROUND_COLOR)

    # Disegna la sprite ruotata, in alto a destra
    window.blit(seal_rotated, (LENGTH - seal_rotated.get_width() - 50, 50))
    
    # Disegna la sprite specchiata, in basso a sinistra
    window.blit(seal_flipped, (50, HEIGHT - seal_flipped.get_height() - 50))

    # Disegna la sprite che apparirà in movimento
    window.blit(seal, (seal_x, seal_y))

    pygame.display.flip()
    clock.tick(FPS) 
    
pygame.quit()