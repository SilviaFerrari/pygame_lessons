import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("5 - Control + Animation")

clock = pygame.time.Clock()
executing = True

# Movimento verso il basso
front_frames = [
    pygame.image.load(os.path.join(CHS_PATH, 'front_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'front_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'front_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'front_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'front_dog_4.png')).convert_alpha()
]

# Movimento verso destra
right_frames = [
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_4.png')).convert_alpha()
]

# Movimento verso l'alto
back_frames = [
    pygame.image.load(os.path.join(CHS_PATH, 'back_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'back_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'back_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'back_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'back_dog_4.png')).convert_alpha()
]

# Movimento verso sinistra
left_frames = [
    pygame.image.load(os.path.join(CHS_PATH, 'left_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'left_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'left_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'left_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'left_dog_4.png')).convert_alpha()
]

# Funzione per ridimensionare tutti i frame in una lista
def scale_frames(frames, scale_factor): # La funzione richiede la lista di frame da ridimensionare
    scaled_frames = []                  # Definisce la nuova lista di frame
    for img in frames:                  # Per ogni frame prende larghezza e altezza
        w, h = img.get_size()           # Aggiunge l'immagine ridimensionata alla nuova lista
        scaled_frames.append(pygame.transform.scale(img, (int(w * scale_factor), int(h * scale_factor))))
    return scaled_frames

# Ridimensioniamo le liste
front_frames = scale_frames(front_frames, 0.5)
right_frames = scale_frames(right_frames, 0.5)
back_frames = scale_frames(back_frames, 0.5)
left_frames = scale_frames(left_frames, 0.5)

# Posizione iniziale
player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5   # velocità di movimento

# Gestione animazione
frame_index = 0
animation_speed = 0.15          # più basso = più lento
current_frames = front_frames   # animazione attuale
player = current_frames[0]      # frame attuale

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    keys = pygame.key.get_pressed() # Otteniamo lo stato di tutti i tasti

    # ---- MOVIMENTI IN DIAGIONALE ---- #
    
    if keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:  # Movimento in diagonale giù a destra
        player_y += speed/2
        player_x += speed/2
        current_frames = right_frames
        frame_index += animation_speed

    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]: # Movimento in diagonale giù a sinistra
        player_y += speed/2
        player_x -= speed/2
        current_frames = left_frames
        frame_index += animation_speed

    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:  # Movimento in diagonale sù a destra
        player_y -= speed
        player_x += speed/2
        current_frames = right_frames
        frame_index += animation_speed

    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:   # Movimento in diagonale sù a sinistra
        player_y -= speed
        player_x -= speed/2
        current_frames = left_frames
        frame_index += animation_speed        

    # ---- MOVIMENTI IN LINEA RETTA ---- #       

    elif keys[pygame.K_DOWN]:           # Movimento verso il basso
        player_y += speed
        current_frames = front_frames
        frame_index += animation_speed    

    elif keys[pygame.K_RIGHT]:          # Movimento verso destra
        player_x += speed
        current_frames = right_frames
        frame_index += animation_speed

    elif keys[pygame.K_UP]:             # Movimento verso l'alto
        player_y -= speed
        current_frames = back_frames
        frame_index += animation_speed

    elif keys[pygame.K_LEFT]:           # Movimento verso sinistra
        player_x -= speed
        current_frames = left_frames
        frame_index += animation_speed

    else:
        frame_index = 0     # Se non si preme nulla, usa il frame 0 dell'animazione corrente.

    # ---- GESTIONE CICLICA DEI FRAME ---- #

    if frame_index >= len(current_frames):  # Se ho finito i frame, ricomincio l'animazione dall'indice 1.
        frame_index = 1                     # Il frame 0 serve solo se sono fermo, non per l'animazione.

    player = current_frames[int(frame_index)]   # Seleziona l’immagine corrispondente da mostrare.

    # ---- LIMITAZIONE DEI MOVIMENTI AI BORDI ---- #

    if player_x < 0:
        player_x = 0

    if player_x > LENGTH - player.get_width():
        player_x = LENGTH - player.get_width()

    if player_y < 0:
        player_y = 0

    if player_y > HEIGHT - player.get_height():
        player_y = HEIGHT - player.get_height()

    window.fill(BACKGROUND_COLOR)
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()