import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 100)
FPS = 60

CHS_PATH = 'assets/characters'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("3 - Frame Animation")

clock = pygame.time.Clock()
executing = True

# Caricamento dei frame per simulare il movimento
frames = [
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_4.png')).convert_alpha()
]

# Ridimensionamento proporzionale di tutti i frame
orig_w, orig_h = frames[0].get_size()   # Prendiamo la larghezza e altezza originali della prima immagine
scale_factor = 1                        # Scegliamo un fattore di scala (0.5 = metà dimensioni, 1 = dimensione originale)

frames = [pygame.transform.scale(frame, 
            (int(orig_w * scale_factor), int(orig_h * scale_factor))) for frame in frames]

# Dati dei frame
frame_index = 0                                     # Indica quale frame mostrare
animation_speed = 0.15                              # Controlla la velocità del cambio frame
dog_x = 0                                           # Definisco la coordinata iniziale sull’asse X
dog_y = HEIGHT // 2 - frames[0].get_height() // 2   # Definisco la coordinata iniziale sull’asse Y (centro verticalmente)
dog_speed = 2                                       # Definisco la velocità di movimento (pixel per frame)

while executing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            executing = False           

    # Movimento del personaggio
    dog_x += dog_speed
    if dog_x > LENGTH:
        dog_x = -frames[frame_index].get_width()

    # Aggiorna l’indice del frame --> animazione
    frame_index += animation_speed
    if frame_index >= len(frames):
        frame_index = 0

    window.fill(BACKGROUND_COLOR)

    # Disegna il frame corrente dell’animazione
    current_frame = frames[int(frame_index)]
    window.blit(current_frame, (dog_x, dog_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()