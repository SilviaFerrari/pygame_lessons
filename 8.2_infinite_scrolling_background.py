import pygame, os

pygame.init()

LENGTH = 1000
HEIGHT = 600
FPS = 60

CHS_PATH = 'assets/characters'
BCKS_PATH = 'assets/backgrounds'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Infinite Background Scrolling")

clock = pygame.time.Clock()
executing = True

# Carichiamo lo sfondo con DIMENSIONI UGUALI ALLA FINESTRA
background = pygame.image.load(os.path.join(BCKS_PATH, "beach.jpg")).convert()
background = pygame.transform.scale(background, (LENGTH, HEIGHT))

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

right_frames = scale_frames(right_frames)
left_frames = scale_frames(left_frames)

# Posizione del player FISSO AL CENTRO DELLA FINESTRA
player_x = LENGTH // 2
player_y = HEIGHT - 150
speed = 5

# Gestione animazione
frame_index = 0
animation_speed = 0.15
current_frames = right_frames
player = current_frames[0]

# --- BACKGROUND SCROLLING --- #
bg_scroll_x = 0   # quanto si è spostato lo sfondo

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    keys = pygame.key.get_pressed()

    # Movimento solo destra/sinistra
    if keys[pygame.K_RIGHT]:
        bg_scroll_x -= speed  # lo sfondo si muove a sinistra
        current_frames = right_frames
        frame_index += animation_speed
    elif keys[pygame.K_LEFT]:
        bg_scroll_x += speed  # lo sfondo si muove a destra
        current_frames = left_frames
        frame_index += animation_speed
    else:
        frame_index = 0

    # --- LOOP INFINITO DEL BACKGROUND --- #

    # Se lo sfondo si sposta oltre la sua larghezza, ricomincia
    if bg_scroll_x <= -LENGTH:
        bg_scroll_x = 0
    if bg_scroll_x >= LENGTH:
        bg_scroll_x = 0

    # ---- ANIMAZIONE PLAYER ---- #
    if frame_index >= len(current_frames):
        frame_index = 1
    player = current_frames[int(frame_index)]

    # Disegniamo due copie dello sfondo: una in posizione corrente, l’altra subito dopo
    window.blit(background, (bg_scroll_x, 0))
    window.blit(background, (bg_scroll_x + LENGTH, 0))
    window.blit(background, (bg_scroll_x - LENGTH, 0))

    # Disegniamo il cane (fisso al centro)
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()