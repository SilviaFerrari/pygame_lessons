import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'
FONTS_PATH = "assets/fonts"

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("11.1 - Simple Start Screen")

clock = pygame.time.Clock()
executing = True

# ---- GAME STATES ---- #
START = 0
PLAYING = 1

# Quando il gioco si avvia, lo stato sarà sempre START
state = START   

'''
Dobbiamo definire degli stati di gioco (variabili booleane)
per poter capire dove ci troviamo e che azioni dobbiamo fare.
Più schermate o livelli vogliamo implementare, più stati ci serviranno.
'''

# ---- PLAYER ---- #
player = pygame.image.load(os.path.join(CHS_PATH, 'seal.png')).convert_alpha()  

orig_w, orig_h = player.get_size()
scale_factor = 0.3
player = pygame.transform.scale(player, (int(orig_w * scale_factor), int(orig_h * scale_factor)))

player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5  

# ---- FONTS ---- #

# Carichiamo i font che ci servono
font_path = os.path.join(FONTS_PATH, "bubble_pixel.ttf")
big_bubble_font = pygame.font.Font(font_path, 60)           # Faccio due versione dello stesso font
small_bubble_font = pygame.font.Font(font_path, 30)         # Una più piccola e una più grande

# Definisco il testo e stile del titolo e del sottotitolo
title_text = big_bubble_font.render("Seal Adventure", True, (255, 255, 0))
start_text = small_bubble_font.render("Premi SPAZIO per iniziare", True, (255, 255, 255))

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

        # Tasto spazio per avviare il gioco
        if state == START and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            state = PLAYING     # Cambio lo stato del gioco

    # ---- START SCREEN ---- #

    if state == START:
        # Disegno il colore di sfondo e le scritte definite prima
        window.fill((0, 90, 100))
        window.blit(title_text, (LENGTH//2 - title_text.get_width()//2, HEIGHT//2 - 100))
        window.blit(start_text, (LENGTH//2 - start_text.get_width()//2, HEIGHT//2))
        
        pygame.display.flip()
        clock.tick(FPS)
        continue   # Salta il resto del loop finché non si entra in PLAYING    

    # ---- STATO DEL GIOCO = PLAYING ---- #
    keys = pygame.key.get_pressed() 

    if keys[pygame.K_LEFT]: 
        player_x -= speed   

    if keys[pygame.K_RIGHT]:
        player_x += speed   

    if keys[pygame.K_UP]:   
        player_y -= speed   

    if keys[pygame.K_DOWN]:
        player_y += speed   

    window.fill(BACKGROUND_COLOR)
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()