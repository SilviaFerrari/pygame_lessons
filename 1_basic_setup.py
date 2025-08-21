import pygame  # importiamo la libreria pygame-ce

# Inizializzazione di tutte le funzioni di pygame (grafica, suoni, ecc.)
pygame.init()

# Definiamo la dimensione e il colore della finestra di gioco e frame
LENGTH = 800
HEIGHT = 600
BACKGROUND_COLOR = (30, 30, 30)  # RGB: rosso, verde, blu
FPS = 60

# Creiamo la finestra di gioco con le dimensioni scelte
window = pygame.display.set_mode((LENGTH, HEIGHT))

# Diamo un titolo alla finestra
pygame.display.set_caption("Gioco di esempio")

# Creiamo un oggetto "clock" per controllare il numero di fotogrammi al secondo
clock = pygame.time.Clock()

# Variabile per gestire il ciclo principale (se diventa False, il gioco si chiude)
executing = True

# ----- CICLO PRINCIPALE DEL GIOCO ----- #

while executing:
    
    for event in pygame.event.get():    # Gestione degli eventi (input da tastiera, mouse, chiusura finestra, ecc.)
        if event.type == pygame.QUIT:   # se l'utente chiude la finestra
            executing = False           # esci dal ciclo principale

    # ----- AGGIORNAMENTO LOGICA DI GIOCO ----- #

    # Riempiamo lo sfondo con il colore scelto
    window.fill(BACKGROUND_COLOR)  
    
    # Qui disegneremo oggetti, testi, immagini, ecc.
    
    # Aggiorniamo lo schermo
    pygame.display.flip()

    # FPS = fotogrammi al secondo
    clock.tick(FPS) 

# Quando il ciclo principale finisce chiudiamo pygame
pygame.quit()