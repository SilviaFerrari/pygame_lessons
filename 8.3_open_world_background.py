import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'
BCKS_PATH = 'assets/backgrounds'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("8.3 - Open World Backgorung")

clock = pygame.time.Clock()
executing = True

# Carichiamo uno sfondo PIÙ GRANDE della finestra (es: 1600x1200)
background = pygame.image.load(os.path.join(BCKS_PATH, "village_map.png")).convert()
bg_width, bg_height = background.get_size()

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

# Posizione del player nel ** MONDO DI GIOCO NON NELLA FINESTRA! **
player_x, player_y = bg_width // 2, bg_height // 2
speed = 5   

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

    if keys[pygame.K_DOWN]:             # Movimento verso il basso
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
        frame_index = 0     

    # ---- GESTIONE CICLICA DEI FRAME ---- #

    if frame_index >= len(current_frames):  
        frame_index = 1                     

    player = current_frames[int(frame_index)]   

    # ---- LIMITAZIONE DEL PLAYER AI BORDI ---- #

    if player_x < 0:
        player_x = 0

    if player_x > bg_width - player.get_width():    # Usa lo sfondo, non la finestra
        player_x = bg_width - player.get_width()

    if player_y < 0:
        player_y = 0

    if player_y > bg_height - player.get_height():  # Usa lo sfondo, non la finestra
        player_y = bg_height - player.get_height()

    # ---- CAMERA ---- #

    # E' un "rettangolo virtuale" che rappresenta cosa vediamo, CENTRATA SUL PLAYER
    camera_x = player_x - LENGTH // 2
    camera_y = player_y - HEIGHT // 2

    # Impediamo alla camera di uscire dai bordi dello sfondo
    if camera_x < 0: 
        camera_x = 0

    if camera_y < 0: 
        camera_y = 0

    if camera_x > bg_width - LENGTH: 
        camera_x = bg_width - LENGTH

    if camera_y > bg_height - HEIGHT: 
        camera_y = bg_height - HEIGHT

    # ---- DISEGNO DELLA VIEWPORT ---- #

    # Disegniamo SOLO la porzione di sfondo che coincide con la finestra.
    window.blit(background, (0, 0), (camera_x, camera_y, LENGTH, HEIGHT))

    # La posizione del player sullo schermo NON è player_x, player_y,
    # ma la sua posizione relativa alla camera.
    screen_x = player_x - camera_x
    screen_y = player_y - camera_y
    window.blit(player, (screen_x, screen_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()