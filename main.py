import pygame, sys
from pygame.locals import *
import random

import pygame.locals
 
pygame.init()
 
FPS = 60
FramePerSec = pygame.time.Clock()

# Global variable
BLACK_TYPE = 'black'
WHITE_TYPE = 'white'
KING = "king"
QUEEN = "queen"
PAWN = "pawn"
BISHOP = "bishop"
KNIGHT = "knight"
ROOK = "rook"

# Predefined some colors
BLUE_COLOR  = (0, 0, 255)
RED_COLOR   = (255, 0, 0)
GREEN_COLOR = (115, 149, 82)
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

CASE_SIZE = 80
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
DISPLAYSURF.fill(WHITE_COLOR)
pygame.display.set_caption("Chess Python")

#Asset loading
white_pawn_img = pygame.image.load("assets/white_pawn.png")
white_pawn_img.convert()
white_pawn_img = pygame.transform.rotozoom(white_pawn_img,1,0.5)

white_queen_img = pygame.image.load("assets/white_queen.png")
white_queen_img.convert()
white_queen_img = pygame.transform.rotozoom(white_queen_img,1,0.5)

white_rook_img = pygame.image.load("assets/white_rook.png")
white_rook_img.convert()
white_rook_img = pygame.transform.rotozoom(white_rook_img,1,0.5)

white_king_img = pygame.image.load("assets/white_king.png")
white_king_img.convert()
white_king_img = pygame.transform.rotozoom(white_king_img,1,0.5)

white_knight_img =pygame.image.load("assets/white_knight.png")
white_knight_img.convert()
white_knight_img = pygame.transform.rotozoom(white_knight_img,1,0.5)

white_bishop_img = pygame.image.load("assets/white_bishop.png")
white_bishop_img.convert()
white_bishop_img = pygame.transform.rotozoom(white_bishop_img,1,0.5)

black_pawn_img = pygame.image.load("assets/black_pawn.png")
black_pawn_img.convert()
black_pawn_img = pygame.transform.rotozoom(black_pawn_img,1,0.5)

black_queen_img = pygame.image.load("assets/black_queen.png")
black_queen_img.convert()
black_queen_img = pygame.transform.rotozoom(black_queen_img,1,0.5)

black_rook_img = pygame.image.load("assets/black_rook.png")
black_rook_img.convert()
black_rook_img = pygame.transform.rotozoom(black_rook_img,1,0.5)

black_king_img = pygame.image.load("assets/black_king.png")
black_king_img.convert()
black_king_img = pygame.transform.rotozoom(black_king_img,1,0.5)

black_knight_img =pygame.image.load("assets/black_knight.png")
black_knight_img.convert()
black_knight_img = pygame.transform.rotozoom(black_knight_img,1,0.5)

black_bishop_img = pygame.image.load("assets/black_bishop.png")
black_bishop_img.convert()
black_bishop_img = pygame.transform.rotozoom(black_bishop_img,1,0.5)


# Chess piece Logic
class Piece():
    def __init__(self,piece_type,piece_color,position,white_img,black_img):
        self.position = position
        self.piece_type = piece_type
        self.piece_color = piece_color
        self.black_img= black_img
        self.white_img = white_img
        self.available_move = []
        self.begin_position = True

    def move(self,newPosition):
        self.position = newPosition
        self.begin_position = False
    
    def draw(self):
        if(self.piece_color==BLACK_TYPE) :
            rect = self.black_img.get_rect()
            rect.center = self.position[1]*CASE_SIZE+CASE_SIZE/2,self.position[0]*CASE_SIZE+CASE_SIZE/2
            DISPLAYSURF.blit(self.black_img,rect)
        else:
            rect = self.white_img.get_rect()
            rect.center = self.position[1]*CASE_SIZE+CASE_SIZE/2,self.position[0]*CASE_SIZE+CASE_SIZE/2
            DISPLAYSURF.blit(self.white_img,rect)
        # pygame.draw.circle(DISPLAYSURF,color,(self.position[1]*CASE_SIZE+CASE_SIZE/2,self.position[0]*CASE_SIZE+CASE_SIZE/2),10)


class Pawn(Piece):
    def __init__(self, piece_color, position):
        super().__init__(PAWN, piece_color, position,white_pawn_img,black_pawn_img)

        
class Queen(Piece):
    def __init__(self, piece_color, position):
        super().__init__(QUEEN, piece_color, position,white_queen_img,black_queen_img)
    
      
class King(Piece):
    def __init__(self, piece_color, position):
        super().__init__(KING, piece_color, position,white_king_img,black_king_img)


class Knight(Piece):
    def __init__(self, piece_color, position):
        super().__init__(KNIGHT, piece_color, position,white_knight_img,black_knight_img)


class Bishop(Piece):
    def __init__(self, piece_color, position):
        super().__init__(BISHOP, piece_color, position,white_bishop_img,black_bishop_img)


class Rook(Piece):
    def __init__(self, piece_color, position):
        super().__init__(ROOK, piece_color, position,white_rook_img,black_rook_img)



#Board methods
class Board():
    def __init__(self):
        self.black_pieces =  [
            Rook(BLACK_TYPE,(0,0)),
            Knight(BLACK_TYPE,(0,1)),
            Bishop(BLACK_TYPE,(0,2)),
            Queen(BLACK_TYPE,(0,3)),
            King(BLACK_TYPE,(0,4)),
            Bishop(BLACK_TYPE,(0,5)),
            Knight(BLACK_TYPE,(0,6)),
            Rook(BLACK_TYPE,(0,7)),
            Pawn(BLACK_TYPE,(1,0)),
            Pawn(BLACK_TYPE,(1,1)),
            Pawn(BLACK_TYPE,(1,2)),
            Pawn(BLACK_TYPE,(1,3)),
            Pawn(BLACK_TYPE,(1,4)),
            Pawn(BLACK_TYPE,(1,5)),
            Pawn(BLACK_TYPE,(1,6)),
            Pawn(BLACK_TYPE,(1,7)),
        ]
        self.white_pieces = [
            Rook(WHITE_TYPE,(7,0)),
            Knight(WHITE_TYPE,(7,1)),
            Bishop(WHITE_TYPE,(7,2)),
            Queen(WHITE_TYPE,(7,3)),
            King(WHITE_TYPE,(7,4)),
            Bishop(WHITE_TYPE,(7,5)),
            Knight(WHITE_TYPE,(7,6)),
            Rook(WHITE_TYPE,(7,7)),
            Pawn(WHITE_TYPE,(6,0)),
            Pawn(WHITE_TYPE,(6,1)),
            Pawn(WHITE_TYPE,(6,2)),
            Pawn(WHITE_TYPE,(6,3)),
            Pawn(WHITE_TYPE,(6,4)),
            Pawn(WHITE_TYPE,(6,5)),
            Pawn(WHITE_TYPE,(6,6)),
            Pawn(WHITE_TYPE,(6,7))
        ]
        
    def check_case(self,position):
        for piece in self.black_pieces:
            if(piece.position==position):
                return piece
        for piece in self.white_pieces:
            if(piece.position==position):
                return piece
        return None

    def move_piece(self,piece:Piece,position):
        target = self.check_case(position=position)
        if(target != None):
            if(target.piece_color== BLACK_TYPE):
                self.black_pieces.remove(target)
            else :
                self.white_pieces.remove(target)
        piece.move(position)

    def pawn_move(self,pawn : Piece):
        pawn.available_move = []
        if(pawn.piece_color == BLACK_TYPE):
            if(pawn.begin_position==True and self.check_case((pawn.position[0]+2,pawn.position[1]))==None):
                pawn.available_move.append((pawn.position[0]+2,pawn.position[1]))
            if(self.check_case((pawn.position[0]+1,pawn.position[1]))==None):
                pawn.available_move.append((pawn.position[0]+1,pawn.position[1]))
            if(self.check_case((pawn.position[0]+1,pawn.position[1]+1))!=None):
                other_piece = self.check_case((pawn.position[0]+1,pawn.position[1]+1))
                print(other_piece.position)
                if(other_piece.piece_color == WHITE_TYPE):
                    pawn.available_move.append((pawn.position[0]+1,pawn.position[1]+1))
            if(self.check_case((pawn.position[0]+1,pawn.position[1]-1))!=None):
                other_piece = self.check_case((pawn.position[0]+1,pawn.position[1]-1))
                if(other_piece.piece_color == WHITE_TYPE):
                    pawn.available_move.append((pawn.position[0]+1,pawn.position[1]-1))
        else :
            if(pawn.begin_position==True and self.check_case((pawn.position[0]-2,pawn.position[1]))==None):
                pawn.available_move.append((pawn.position[0]-2,pawn.position[1]))
            if(self.check_case((pawn.position[0]-1,pawn.position[1]))==None):
                pawn.available_move.append((pawn.position[0]-1,pawn.position[1]))
            if(self.check_case((pawn.position[0]-1,pawn.position[1]+1))!=None):
                other_piece = self.check_case((pawn.position[0]-1,pawn.position[1]+1))
                if(other_piece.piece_color == BLACK_TYPE):
                    pawn.available_move.append((pawn.position[0]-1,pawn.position[1]+1))
            if(self.check_case((pawn.position[0]-1,pawn.position[1]-1))!=None):
                other_piece = self.check_case((pawn.position[0]-1,pawn.position[1]-1))
                if(other_piece.piece_color == BLACK_TYPE):
                    pawn.available_move.append((pawn.position[0]-1,pawn.position[1]-1))
    
    def calc_board_move(self):
        for piece in self.black_pieces:
            match piece.piece_type:
                case 'pawn':
                    self.pawn_move(piece)
        for piece in self.white_pieces:
            match piece.piece_type:
                case 'pawn':
                    self.pawn_move(piece)
        return None

#Game methods
class Game():

    def __init__(self):
        self.board = Board()
        self.selectedPieces : Piece = None

    def select_case(self,position):
        if(self.selectedPieces!=None):
            for move in self.selectedPieces.available_move:
                if(position==move):
                    self.board.move_piece(self.selectedPieces,position)
                    self.selectedPieces = None
                    self.board.calc_board_move()
                    return None
        for piece in self.board.black_pieces:
            if(piece.position==position):
                self.selectedPieces = piece
                return piece
        for piece in self.board.white_pieces:
            if(piece.position==position):
                self.selectedPieces = piece
                return piece
        return None
    
    def draw_possible_move(self,piece : Piece):
        for pos in piece.available_move:
            pygame.draw.circle(DISPLAYSURF,BLACK_COLOR,(pos[1]*CASE_SIZE+CASE_SIZE/2,pos[0]*CASE_SIZE+CASE_SIZE/2),10)

    
    def print_pieces(self):
        for piece in self.board.black_pieces:
            piece.draw()
        
        for piece in self.board.white_pieces:
            piece.draw()
    
    def display_game_screen(self):
        self.print_board()
        self.print_pieces()
        if(self.selectedPieces != None):
            self.draw_possible_move(self.selectedPieces)


# Display chess board
    def print_board(self):
        pygame.draw.rect(DISPLAYSURF,BLACK_COLOR,[0,0,CASE_SIZE*8+1,CASE_SIZE*8+1])
        for x in range(8):
            for y in range(8):
                if((x+y)%2) :
                    color_case = GREEN_COLOR
                else:
                    color_case = WHITE_COLOR
                pygame.draw.rect(DISPLAYSURF,color_case,[CASE_SIZE*x,CASE_SIZE*y,CASE_SIZE,CASE_SIZE],0)


# Display chess piece



game = Game()
game.board.calc_board_move()
# Game cycle
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(pos[0] < CASE_SIZE*8 + 1 and pos[1]<CASE_SIZE*8 +1):
                chess_x = int(pos[1]/CASE_SIZE)
                chess_y = int(pos[0]/CASE_SIZE)
                piece = game.select_case((chess_x,chess_y))
                
                

    game.display_game_screen()
    pygame.display.update()
    # FramePerSec.tick(FPS)