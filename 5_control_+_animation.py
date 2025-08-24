import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("4 - User Control")

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

# Funzione per ridimensionare tutti i frame in una lista
def scale_frames(frames, scale_factor=0.5):
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

    # ---- MOVIMENTO E SELEZIONE ANIMAZIONE ---- #

    if keys[pygame.K_DOWN]:
        player_y += speed
        current_frames = front_frames
        frame_index += animation_speed

    elif keys[pygame.K_RIGHT]:
        player_x += speed
        current_frames = right_frames
        frame_index += animation_speed

    elif keys[pygame.K_UP]:
        player_y -= speed
        current_frames = back_frames
        frame_index += animation_speed

    elif keys[pygame.K_LEFT]:
        player_x -= speed
        current_frames = left_frames
        frame_index += animation_speed

    else:
        frame_index = 0 # Se non si preme nulla, sta fermo sul primo frame dell'animazione corrente

    # Gestione ciclica dei frame
    if frame_index >= len(current_frames):
        frame_index = 1

    player = current_frames[int(frame_index)]

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