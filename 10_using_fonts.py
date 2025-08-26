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

# Carico il font esterno
font_path = os.path.join(FONTS_PATH, "bubble_pixel.ttf")
bubble_font = pygame.font.Font(font_path, 40)

font_path = os.path.join(FONTS_PATH, "mario_kart_DS.ttf")
mario_font = pygame.font.Font(font_path, 80)

font_path = os.path.join(FONTS_PATH, "robotic_pixel.ttf")
robotic_font = pygame.font.Font(font_path, 50)

# Renderizzo il testo
text_surface_1 = bubble_font.render("Ciao, questo e' un testo!", True, (255, 255, 255))
text_rect_1 = text_surface_1.get_rect(center=(LENGTH // 2, 100))

text_surface_2 = mario_font.render("Super Mario Kart!", True, (255, 255, 255))
text_rect_2 = text_surface_2.get_rect(center=(LENGTH // 2, HEIGHT // 2))

text_surface_3 = robotic_font.render("Ciao, questo e' un testo!", True, (255, 255, 255))
text_rect_3 = text_surface_3.get_rect(center=(LENGTH // 2, 500))

while executing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executing = False

    window.fill(BACKGROUND_COLOR)
    window.blit(text_surface_1, text_rect_1)
    window.blit(text_surface_2, text_rect_2)
    window.blit(text_surface_3, text_rect_3)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()