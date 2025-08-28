import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (0, 90, 100)
FPS = 60

CHS_PATH = 'assets/characters'
FONTS_PATH = "assets/fonts"

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("11.2 - Button Start Screen")

clock = pygame.time.Clock()
executing = True

# ---- GAME STATES ---- #
START = 0
PLAYING = 1

# Quando il gioco si avvia, lo stato sarà sempre START
state = START   

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

# Definisco il testo del titolo
title_surface = big_bubble_font.render("Seal Adventure", True, (255, 255, 0))

# Bottone start
button_text = small_bubble_font.render("START", True, (255, 255, 255))  # scritta dentro il bottone
button_width, button_height = 200, 80   # dimensioni del bottone
button_rect = pygame.Rect(LENGTH // 2 - button_width // 2, HEIGHT // 2, button_width, button_height)

'''
Il rettangolo serve per poter determinare 'la collisione col mouse',
così come si controlla la collisione con altri rettangoli, è possbile
rilevare il click del mouse (MOUSEBUTTONDOWN) sopra al rettangolo del bottone.
'''

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

        # Se siamo nella schermata iniziale e viene premuto il bottone start...
        if state == START and event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                state = PLAYING     # ... si passa alla schermata di gioco

    # ---- START SCREEN ---- #

    if state == START:
        window.fill((0, 90, 100))
        window.blit(title_surface, (LENGTH//2 - title_surface.get_width()//2, HEIGHT//2 - 100))
        pygame.draw.rect(window, (200, 50, 50), button_rect, border_radius=15)
        text_rect = button_text.get_rect(center=button_rect.center)
        window.blit(button_text, text_rect)
        
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