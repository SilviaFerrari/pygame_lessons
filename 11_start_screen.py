import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'
FONTS_PATH = "assets/fonts"

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("11 - Start Screen")

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

# Carichiamo l’immagine del personaggio
player = pygame.image.load(os.path.join(CHS_PATH, 'seal.png')).convert_alpha()  

# Ridimensioniamo proporzionalmente con un fattore di scala
orig_w, orig_h = player.get_size()
scale_factor = 0.3
player = pygame.transform.scale(player, (int(orig_w * scale_factor), int(orig_h * scale_factor)))

# Posizione iniziale
player_x = LENGTH // 2
player_y = HEIGHT // 2
speed = 5  

# Carichiamo i font che ci servono
font_path = os.path.join(FONTS_PATH, "bubble_pixel.ttf")
big_bubble_font = pygame.font.Font(font_path, 60)           # Faccio due versione dello stesso font
small_bubble_font = pygame.font.Font(font_path, 30)         # Una più piccola e una più grande

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

        # Tasto spazio per avviare il gioco
        if state == START and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            state = PLAYING     # Cambio lo stato del gioco

    # ---- START SCREEN ---- #

    if state == START:
        window.fill((0, 90, 100))
        title_text = big_bubble_font.render("Seal Adventure", True, (255, 255, 0))
        start_text = small_bubble_font.render("Premi SPAZIO per iniziare", True, (255, 255, 255))

        window.blit(title_text, (LENGTH//2 - title_text.get_width()//2, HEIGHT//2 - 100))
        window.blit(start_text, (LENGTH//2 - start_text.get_width()//2, HEIGHT//2))
        
        pygame.display.flip()
        clock.tick(FPS)
        continue   # Salta il resto del loop finché non si entra in PLAYING    

    # ---- STATUS PLAYING ---- #

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

    window.fill(BACKGROUND_COLOR)
    window.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()