import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'
SND_PATH = 'assets/sounds'

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("4.1 - User Control Border + Music")

clock = pygame.time.Clock()
executing = True

# ---- PLAYER ---- #
player = pygame.image.load(os.path.join(CHS_PATH, 'seal.png')).convert_alpha()  

orig_w, orig_h = player.get_size()
scale_factor = 0.3
player = pygame.transform.scale(player, (int(orig_w * scale_factor), int(orig_h * scale_factor)))

player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5  # velocità di movimento

# ---- MUSICA DI SOTTOFONDO ---- #

music_file = os.path.join(SND_PATH, "music.wav")
pygame.mixer.music.load(music_file)  # carica il file audio
pygame.mixer.music.set_volume(0.3)   # volume da 0.0 a 1.0 (50%)
pygame.mixer.music.play(-1)          # -1 significa loop infinito

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    # ---- INPUT DA TASTIERA ---- #
    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # ---- DISEGNO ---- #
    window.fill(BACKGROUND_COLOR)
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()