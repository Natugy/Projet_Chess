import copy
import time
import pygame, sys
from pygame.locals import *
import random

import pygame.locals

from pieces import *
from board import *
pygame.init()
 
 
DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
DISPLAYSURF.fill(WHITE_COLOR)
pygame.display.set_caption("Chess Python")

# Police
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)



#Game methods
class Game():

    def __init__(self):
        self.board = Board()
        self.selectedPieces : Piece = None
        self.currentColor = WHITE_TYPE
        self.gameRunning = True
        self.playerWhite = Player()
        self.playerBlack = Player()
        self.currentPlayer = self.playerWhite

    def get_white_pieces(self):
        return self.board.white_pieces

    def get_black_pieces(self):
        return self.board.black_pieces
    
    def set_selected_piece(self,piece):
        self.selectedPieces = piece

    
    def estimate_move(self,colorPlayer,depth):
        return self.board.estimate_move(colorPlayer,depth)


    def select_case(self,position):
        if(self.selectedPieces!=None):
            for move in self.selectedPieces.available_move:
                if(position==move):
                    self.board.move_piece(self.selectedPieces,position)
                    self.selectedPieces = None
                    self.board.calc_board_move(self.currentColor)
                    if(self.currentColor==WHITE_TYPE) : 
                        self.currentColor = BLACK_TYPE
                        self.currentPlayer = self.playerBlack
                    else : 
                        self.currentColor = WHITE_TYPE
                        self.currentPlayer = self.playerWhite
                    return None
        if(self.currentColor==WHITE_TYPE) : 
            for piece in self.board.white_pieces:
                if(piece.position==position):
                    self.selectedPieces = piece
                    return piece
        else :
            for piece in self.board.black_pieces:
                if(piece.position==position):
                    self.selectedPieces = piece
                    return piece
        return None
    
    def draw_possible_move(self,piece : Piece):
        for pos in piece.available_move:
            if(self.board.check_case(pos)==None):
                pygame.draw.circle(DISPLAYSURF,MOVE_COLOR,(pos[1]*CASE_SIZE+CASE_SIZE/2,pos[0]*CASE_SIZE+CASE_SIZE/2),10)
            else:
                pygame.draw.circle(DISPLAYSURF,MOVE_COLOR,(pos[1]*CASE_SIZE+CASE_SIZE/2,pos[0]*CASE_SIZE+CASE_SIZE/2),40,width=8)

    

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


    def init_game(self,playerWhite,playerBlack):
        self.playerBlack = playerBlack
        self.playerWhite = playerWhite
        self.currentPlayer = self.playerWhite

    def play_game(self):
        DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
        DISPLAYSURF.fill(WHITE_COLOR)
        pygame.display.set_caption("Chess Python")
        self.board.calc_board_move(WHITE_TYPE)
        while self.gameRunning: 
            # if(self.currentPlayer.isAi == False):    
            for event in pygame.event.get():              
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if(pos[0] < CASE_SIZE*8 + 1 and pos[1]<CASE_SIZE*8 +1):
                        chess_x = int(pos[1]/CASE_SIZE)
                        chess_y = int(pos[0]/CASE_SIZE)
                        piece = self.select_case((chess_x,chess_y))
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        self.currentPlayer.play_move()
                        time.sleep(0.1)
            # else:
            #     self.currentPlayer.play_move()
            #     time.sleep(0.1)
            self.display_game_screen()
            self.gameRunning = not self.board.checkMate
            pygame.display.update()
            # FramePerSec.tick(FPS)
        # SCREEN_HEIGHT = SCREEN_HEIGHT +100
        DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
        DISPLAYSURF.fill(WHITE_COLOR)
        while True:
            for event in pygame.event.get():              
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            self.display_game_screen()
            titre = font.render("CheckMate", True, BLACK_COLOR)
            DISPLAYSURF.blit(titre, (SCREEN_WIDTH//2 - titre.get_width()//2, (SCREEN_HEIGHT)//4))
            pygame.display.update()



class Player():
    def __init__(self):
        self.isAi = False
    def play_move(self):
        pass

class AI(Player):
    def __init__(self, game: Game, colorPlayer ):
        self.game = game
        self.colorPlayer = colorPlayer
        self.isAi = True

    def choose_piece(self,piece : Piece):
        self.game.set_selected_piece(piece)
    
    def choose_move(self,position):
        self.game.select_case(position)
    
    def play_move(self):
        pass
    

class DumbAi(AI):
    def __init__(self,game,color):
        super().__init__(game,color)
    
    def play_move(self):
        if(self.colorPlayer == WHITE_TYPE):
            currentPieceList = self.game.get_white_pieces()
        else : 
            currentPieceList = self.game.get_black_pieces()
        randomInt = random.randint(0, len(currentPieceList)-1)
        currentPiece = currentPieceList[randomInt]
        self.choose_piece(currentPiece)
        while len(currentPiece.available_move) == 0:
            randomInt = random.randint(0, len(currentPieceList)-1)
            currentPiece = currentPieceList[randomInt]
            self.choose_piece(currentPiece)
        randomInt = random.randint(0,len(currentPiece.available_move)-1)
        self.choose_move(currentPiece.available_move[randomInt])

class MinMaxAi(AI):
    def __init__(self, game, colorPlayer,depth=0):
        super().__init__(game, colorPlayer)
        self.depth = depth
    
    def play_move(self):
        bestPiece, bestMove, value = self.game.estimate_move(self.colorPlayer,self.depth)
        self.choose_piece(bestPiece)
        self.choose_move(bestMove)

