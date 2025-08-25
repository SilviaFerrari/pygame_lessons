import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("9 - Gravity and Jump")

clock = pygame.time.Clock()
executing = True

# Movimento verso destra
right_frames = [
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_0.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_1.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_2.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_3.png')).convert_alpha(),
    pygame.image.load(os.path.join(CHS_PATH, 'right_dog_4.png')).convert_alpha()
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
def scale_frames(frames, scale_factor=0.5):
    scaled = []
    for img in frames:
        w, h = img.get_size()
        scaled.append(pygame.transform.scale(img, (int(w * scale_factor), int(h * scale_factor))))
    return scaled

# Ridimensioniamo le liste
right_frames = scale_frames(right_frames)
left_frames = scale_frames(left_frames)

# Posizione iniziale
player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5   # velocità di movimento

# Gestione animazione
frame_index = 0
animation_speed = 0.15          
current_frames = right_frames   
player = current_frames[0]      

# --- PAVIMENTO E SALTO --- #

floor_y = HEIGHT - 50   # posizione del pavimento
gravity = 0.8           # forza con cui cade
jump_strength = -15     # forza del salto (negativa = verso l’alto)
velocity_y = 0          # velocità verticale del cane
is_jumping = False

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                velocity_y = jump_strength
                is_jumping = True

    keys = pygame.key.get_pressed() 

    if keys[pygame.K_RIGHT]:
        player_x += speed
        current_frames = right_frames
        frame_index += animation_speed

    elif keys[pygame.K_LEFT]:
        player_x -= speed
        current_frames = left_frames
        frame_index += animation_speed

    else:
        frame_index = 0     

    # ---- SALTO E GRAVITÀ ---- #

    velocity_y += gravity           # applica la gravità
    player_y += velocity_y          # muove il cane in verticale

    # --- COLLISIONE CON IL PAVIMENTO --- #
    # Se la parte bassa del cane scende oltre il livello del pavimento
    # lo riposizioniamo esattamente sopra il pavimento, evitando che "affondi".

    if player_y >= floor_y - player.get_height():  
        player_y = floor_y - player.get_height()    
        velocity_y = 0      # Azzeriamo la velocità verticale (il salto è finito).
        is_jumping = False  # Indichiamo che il cane NON sta più saltando (può saltare di nuovo).

    # ---- GESTIONE CICLICA DEI FRAME ---- #

    if frame_index >= len(current_frames):
        frame_index = 1

    player = current_frames[int(frame_index)]

    # ---- LIMITAZIONE DEI MOVIMENTI AI BORDI LATERALI ---- #
    if player_x < 0:
        player_x = 0
    if player_x > LENGTH - player.get_width():
        player_x = LENGTH - player.get_width()

    # ---- DISEGNO ---- #
    window.fill(BACKGROUND_COLOR)

    # Disegno il pavimento
    pygame.draw.rect(window, (50, 200, 50), (0, floor_y, LENGTH, HEIGHT - floor_y))

    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()