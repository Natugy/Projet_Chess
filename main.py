import pygame
import sys

from chess import Game

# Initialisation
pygame.init()

# Taille de la fenêtre
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu avec Boutons")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
VERT = (76, 175, 80)
VERT_CLAIR = (139, 195, 74)

# Police
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 50)

# Fonctions pour dessiner les boutons
def draw_button(text, x, y, width, height, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    text_surface = button_font.render(text, True, NOIR)
    text_rect = text_surface.get_rect(center=((x + width / 2), (y + height / 2)))
    screen.blit(text_surface, text_rect)

# Actions des boutons
def start_game():
    global menu_active
    menu_active = False
    game = Game()
    game.play_game()

def quit_game():
    pygame.quit()
    sys.exit()

# --- Menu principal ---
menu_active = True

while menu_active:
    screen.fill(BLANC)

    titre = font.render("Menu Principal", True, NOIR)
    screen.blit(titre, (WIDTH//2 - titre.get_width()//2, HEIGHT//4))

    draw_button("JOUER", WIDTH//2 - 100, HEIGHT//2 - 50, 200, 50, VERT, VERT_CLAIR, start_game)
    draw_button("QUITTER", WIDTH//2 - 100, HEIGHT//2 + 30, 200, 50, VERT, VERT_CLAIR, quit_game)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

# --- Jeu après avoir cliqué sur "JOUER" ---

pygame.quit()
