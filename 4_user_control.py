import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)
FPS = 60

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("Gioco di esempio")

clock = pygame.time.Clock()
executing = True

# Carichiamo l’immagine del personaggio
player = pygame.image.load(os.path.join('assets', 'seal.png')).convert_alpha()  

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

    keys = pygame.key.get_pressed()  # Otteniamo lo stato di tutti i tasti

    # In questo caso si usano le 4 frecce
    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    if keys[pygame.K_UP]:
        player_y -= speed

    if keys[pygame.K_DOWN]:
        player_y += speed

    # ---- Limitazione dei movimenti ai bordi della finestra ---- #

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