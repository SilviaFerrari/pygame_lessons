import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (100, 150, 100)
FPS = 60

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("6 - Obstacles Collision")

clock = pygame.time.Clock()
executing = True

# Movimento verso il basso
front_frames = [
    pygame.image.load(os.path.join('assets', 'front_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'front_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'front_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'front_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'front_dog_4.png')).convert_alpha()
]

# Movimento verso destra
right_frames = [
    pygame.image.load(os.path.join('assets', 'right_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'right_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'right_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'right_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'right_dog_4.png')).convert_alpha()
]

# Movimento verso l'alto
back_frames = [
    pygame.image.load(os.path.join('assets', 'back_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'back_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'back_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'back_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'back_dog_4.png')).convert_alpha()
]

# Movimento verso sinistra
left_frames = [
    pygame.image.load(os.path.join('assets', 'left_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'left_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'left_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'left_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'left_dog_4.png')).convert_alpha()
]

# Carico l'immagine dell'ostacolo
wood = pygame.image.load(os.path.join('assets', 'wood.png')).convert_alpha()
wood = pygame.transform.scale(wood, (150, 150))    # Ridimensiono l'immagine
wood_rect = wood.get_rect(center=(550, 300))       # Creo il rettangolo dell'ostacolo che servirà per la collisione

# Funzione per ridimensionare tutti i frame in una lista
def scale_frames(frames, scale_factor=0.8):
    scaled = []
    for img in frames:
        w, h = img.get_size()
        scaled.append(pygame.transform.scale(img, (int(w * scale_factor), int(h * scale_factor))))
    return scaled

# Ridimensioniamo le liste
front_frames = scale_frames(front_frames)
right_frames = scale_frames(right_frames)
back_frames = scale_frames(back_frames)
left_frames = scale_frames(left_frames)

# Posizione iniziale
player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5   

# Creo il rettangono del player che serve per la collisione
player_rect = front_frames[0].get_rect(center=(player_x, player_y))

# Gestione animazione
frame_index = 0
animation_speed = 0.15          # più basso = più lento
current_frames = front_frames   # animazione attuale
player = current_frames[0]      # frame attuale

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    keys = pygame.key.get_pressed() # Stato di tutti i tasti
    
    old_rect = player_rect.copy()   # Salviamo la posizione per annullare il movimento in caso di collisione

    if keys[pygame.K_DOWN]:
        player_rect.y += speed
        current_frames = front_frames
        frame_index += animation_speed    

    elif keys[pygame.K_RIGHT]:
        player_rect.x += speed
        current_frames = right_frames
        frame_index += animation_speed

    elif keys[pygame.K_UP]:
        player_rect.y -= speed
        current_frames = back_frames
        frame_index += animation_speed

    elif keys[pygame.K_LEFT]:
        player_rect.x -= speed
        current_frames = left_frames
        frame_index += animation_speed

    else:
        frame_index = 0

    # ---- COLLISIONE CON L'OSTACOLO ---- #

    if player_rect.colliderect(wood_rect):
        player_rect = old_rect  # Se si scontra torna indietro    

    # ---- GESTIONE CICLICA DEI FRAME ---- #    

    if frame_index >= len(current_frames):  # Se ho finito i frame, ricomincio l'animazione dall'indice 1.
        frame_index = 1                     # Il frame 0 serve solo se sono fermo, non per l'animazione.

    player = current_frames[int(frame_index)]   # Seleziona l’immagine corrispondente da mostrare.

    if player_rect.left < 0:
        player_rect.left = 0

    if player_rect.right > LENGTH:
        player_rect.right = LENGTH

    if player_rect.top < 0:
        player_rect.top = 0

    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT


    window.fill(BACKGROUND_COLOR)
    window.blit(wood, wood_rect)        # Disegna l'ostacolo
    window.blit(player, player_rect)    # Disegna il player

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()