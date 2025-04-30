import pygame

# Chargement et transformation des assets
def load_and_scale(path, scale=0.5):
    image = pygame.image.load(path).convert_alpha()
    return pygame.transform.rotozoom(image, 0, scale)

# Images des pièces blanches
white_pawn_img = load_and_scale("assets/white_pawn.png")
white_queen_img = load_and_scale("assets/white_queen.png")
white_rook_img = load_and_scale("assets/white_rook.png")
white_king_img = load_and_scale("assets/white_king.png")
white_knight_img = load_and_scale("assets/white_knight.png")
white_bishop_img = load_and_scale("assets/white_bishop.png")

# Images des pièces noires
black_pawn_img = load_and_scale("assets/black_pawn.png")
black_queen_img = load_and_scale("assets/black_queen.png")
black_rook_img = load_and_scale("assets/black_rook.png")
black_king_img = load_and_scale("assets/black_king.png")
black_knight_img = load_and_scale("assets/black_knight.png")
black_bishop_img = load_and_scale("assets/black_bishop.png")
