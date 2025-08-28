import pygame, os

pygame.init()

LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (100, 30, 30)
FPS = 60

FONTS_PATH = "assets/fonts"

window = pygame.display.set_mode((LENGTH, HEIGHT))
pygame.display.set_caption("10 - Using Fonts")

clock = pygame.time.Clock()
executing = True

# ---- IMPORT E CREAZIONE DEI FONT ---- #

font_path = os.path.join(FONTS_PATH, "bubble_pixel.ttf")    # Assegno alla variabile font_path il percorso del file dove è definito il font che voglio importare
bubble_font = pygame.font.Font(font_path, 40)               # Creo il font Bubble Pixel, grandezza 40px

font_path = os.path.join(FONTS_PATH, "mario_kart_DS.ttf")   # Assegno alla variabile font_path il percorso del file dove è definito il font che voglio importare
mario_font = pygame.font.Font(font_path, 80)                # Creo il font Mario Kart, grandezza 80px

font_path = os.path.join(FONTS_PATH, "robotic_pixel.ttf")   # Assegno alla variabile font_path il percorso del file dove è definito il font che voglio importare
robotic_font = pygame.font.Font(font_path, 50)              # Creo il font Robotic Pixel, grandezza 50px

# Renderizzo il testo, ovvero creo una surface con dentro il testo disegnato
text_surface_bubble = bubble_font.render("Ciao, questo e' un testo!", True, (255, 255, 255))
text_rect_1 = text_surface_bubble.get_rect(center=(LENGTH // 2, 100))

text_surface_mario = mario_font.render("Super Mario Kart!", True, (255, 255, 255))
text_rect_2 = text_surface_mario.get_rect(center=(LENGTH // 2, HEIGHT // 2))

text_surface_robotic = robotic_font.render("Ciao, questo e' un testo!", True, (255, 255, 255))
text_rect_3 = text_surface_robotic.get_rect(center=(LENGTH // 2, 500))

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    window.fill(BACKGROUND_COLOR)
    window.blit(text_surface_bubble, text_rect_1)
    window.blit(text_surface_mario, text_rect_2)
    window.blit(text_surface_robotic, text_rect_3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()