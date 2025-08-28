import pygame, os
import random

pygame.init()

LENGTH = 1000
HEIGHT = 800
BACKGROUND_COLOR = (100, 150, 100)
FPS = 60

CHS_PATH = 'assets/characters'
ITEMS_PATH = 'assets/items'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("7 - Collect Objects and Score")

clock = pygame.time.Clock()
executing = True

# ---- FRAMES PLAYER ---- #

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
    
# ---- OGGETTO RACCOGLIBILE ---- #

bone = pygame.image.load(os.path.join(ITEMS_PATH, 'bone.png')).convert_alpha()                      # Carico l'immagine
bone = pygame.transform.scale(bone, (70, 35))                                                       # La scalo
bone_rect = bone.get_rect(center=(random.randint(50, LENGTH-50), random.randint(50, HEIGHT-50)))    # Ne creo il rettangolo

# ---- SCALING DELLE IMMAGINI ---- #

def scale_frames(frames, scale_factor): 
    scaled_frames = []                  
    for img in frames:                  
        w, h = img.get_size()           
        scaled_frames.append(pygame.transform.scale(img, (int(w * scale_factor), int(h * scale_factor))))
    return scaled_frames

front_frames = scale_frames(front_frames, 0.5)
right_frames = scale_frames(right_frames, 0.5)
back_frames = scale_frames(back_frames, 0.5)
left_frames = scale_frames(left_frames, 0.5)

# ---- PLAYER ---- #
# Creo il rettangolo del player per la collisione
player_rect = front_frames[0].get_rect(center=(LENGTH // 2, HEIGHT // 2))   

speed = 5
frame_index = 0
animation_speed = 0.15
current_frames = front_frames
player = current_frames[0]

# ---- SCORE ---- #
score = 0                                   # Definisco il punteggio di base
arial_font = pygame.font.SysFont("Arial", 30)     # Stile della scritta

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    keys = pygame.key.get_pressed() # Stato dei tasti
    old_rect = player_rect.copy()   # salvo la posizione corrente

    # ---- MOVIMENTO ---- #

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

    # ---- GESTIONE CICLICA DEI FRAME ---- #

    if frame_index >= len(current_frames):  
        frame_index = 1                     

    player = current_frames[int(frame_index)]   

    # ---- COLLISIONE CON L'OSSO E SPAWN ---- #

    if player_rect.colliderect(bone_rect):              # Se collido con l'osso aumento il punteggio
        score += 1  

        safe_position = False                           # Per controllare che l'osso non spawni sul player
        
        while not safe_position:                        # Rigenero una posizione per l'osso finchè non è valida   
            new_x = random.randint(50, LENGTH - 50)
            new_y = random.randint(50, HEIGHT - 50)
            bone_rect.center = (new_x, new_y)

            if not player_rect.colliderect(bone_rect):  # Ricrea il rect del player per sicurezza
                safe_position = True

    # ---- LIMITI SUI BORDI ---- #

    if player_rect.left < 0:
        player_rect.left = 0

    if player_rect.right > LENGTH:
        player_rect.right = LENGTH

    if player_rect.top < 0:
        player_rect.top = 0
        
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT

    # ---- DISEGNO A SCHERMO ---- #

    window.fill(BACKGROUND_COLOR)
    window.blit(bone, bone_rect)
    window.blit(player, player_rect)

    # ---- MOSTRO IL PUNTEGGIO ---- #
    # Crea una superficie contenente il testo
    score_text = arial_font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()