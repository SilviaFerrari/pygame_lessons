import pygame  # importiamo la libreria pygame-ce

# Inizializzazione di tutte le funzioni di pygame (grafica, suoni, ecc.)
pygame.init()

# ---- FINESTRA DI GIOCO ---- #

LENGTH = 800    # dimensione lunghezza in pixel
HEIGHT = 600    # dimensione altezza in pixel
BACKGROUND_COLOR = (100, 30, 30)  # RGB: rosso, verde, blu
FPS = 60        # framerate massimo (FPS = fotogrammi al secondo)
                # Non è altro che la frequenza di aggiornamento delle immagini sullo schermo.

window = pygame.display.set_mode((LENGTH, HEIGHT))  # Creiamo la finestra di gioco con le dimensioni scelte
pygame.display.set_caption("0 - Basic Setup")       # Diamo un titolo alla finestra

clock = pygame.time.Clock() # Controlla il numero di fotogrammi al secondo
executing = True            # Gestisce il ciclo principale (se diventa False, il gioco si chiude)

# ----- CICLO PRINCIPALE DEL GIOCO ----- #

while executing:
    
    for event in pygame.event.get():    # Gestione degli eventi (input da tastiera, mouse, chiusura finestra, ecc.)
        if event.type == pygame.QUIT:   # se l'utente chiude la finestra
            executing = False           # esci dal ciclo principale

    # ----- AGGIORNAMENTO LOGICA DI GIOCO ----- #

    # Riempiamo lo sfondo con il colore scelto
    window.fill(BACKGROUND_COLOR)  
    
    # Qui disegneremo oggetti, testi, immagini, ecc.
    
    pygame.display.flip()   # Aggiorniamo lo schermo
    clock.tick(FPS)         # Misurazione del tempo in pygame

# Quando il ciclo principale finisce chiudiamo pygame
pygame.quit()
