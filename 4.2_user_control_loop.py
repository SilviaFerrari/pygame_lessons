import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("4.2 - User Control Loop")

clock = pygame.time.Clock()
executing = True

# Carichiamo l’immagine del personaggio
player = pygame.image.load(os.path.join(CHS_PATH, 'seal.png')).convert_alpha()  

# Ridimensioniamo proporzionalmente con un fattore di scala
orig_w, orig_h = player.get_size()
scale_factor = 0.3
player = pygame.transform.scale(player, (int(orig_w * scale_factor), int(orig_h * scale_factor)))

# Posizione iniziale
player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5  # velocità di movimento

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    # ---- INPUT DA TASTIERA ---- #

    keys = pygame.key.get_pressed() # Otteniamo lo stato di tutti i tasti

    # In questo caso si usano le 4 frecce
    if keys[pygame.K_LEFT]: 
        player_x -= speed   # Decremento la coordinata X

    if keys[pygame.K_RIGHT]:
        player_x += speed   # Incremento la coordinata X

    if keys[pygame.K_UP]:   
        player_y -= speed   # Decremento la coordinata Y

    if keys[pygame.K_DOWN]:
        player_y += speed   # Incremento la coordinata Y

    # ---- LOOP DEI MOVIMENTI AI BORDI ---- #

    if player_x < 0:                            # Se esce da sinistra rientra da destra
        player_x = LENGTH - player.get_width()

    if player_x > LENGTH:  # Se esce da destra rientra da sinistra
        player_x = 0

    if player_y < 0:                            # Se esce dall'alto rientra dal basso
        player_y = HEIGHT - player.get_height()

    if player_y > HEIGHT: # Se esce dal basso rientra dall'alto
        player_y = 0

    window.fill(BACKGROUND_COLOR)
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()