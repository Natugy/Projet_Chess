import copy
import time
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
MOVE_COLOR = (201, 201, 199)
 
# Screen information
CASE_SIZE = 80
SCREEN_WIDTH = CASE_SIZE*8 + 1
SCREEN_HEIGHT = CASE_SIZE*8 + 1

 
DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
DISPLAYSURF.fill(WHITE_COLOR)
pygame.display.set_caption("Chess Python")

# Police
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)


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
        self.begin_position = True
        self.available_move = []
        self.check_move=[]
        self.attack_move=[]
        self.protected =False
        self.value = 0

    def copy(self):
        new_piece = Piece(self.piece_type,self.piece_color,self.position,self.white_img,self.black_img)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        return new_piece

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
        self.canBeTakeEnPassant = False
        self.value = 1

    def copy(self):
        new_piece = Pawn(self.piece_color,self.position)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        new_piece.canBeTakeEnPassant = self.canBeTakeEnPassant
        return new_piece
        
class Queen(Piece):
    def __init__(self, piece_color, position):
        super().__init__(QUEEN, piece_color, position,white_queen_img,black_queen_img)
        self.value = 10
    def copy(self):
        new_piece = Queen(self.piece_color,self.position)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        return new_piece
    
      
class King(Piece):
    def __init__(self, piece_color, position):
        super().__init__(KING, piece_color, position,white_king_img,black_king_img)
        self.small_castle = False
        self.big_castle = False
        self.value =3
    def copy(self):
        new_piece = King(self.piece_color,self.position)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        new_piece.small_castle = self.small_castle
        new_piece.big_castle = self.big_castle
        return new_piece
        


class Knight(Piece):
    def __init__(self, piece_color, position):
        super().__init__(KNIGHT, piece_color, position,white_knight_img,black_knight_img)
        self.value = 3
    def copy(self):
        new_piece = Knight(self.piece_color,self.position)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        return new_piece


class Bishop(Piece):
    def __init__(self, piece_color, position):
        super().__init__(BISHOP, piece_color, position,white_bishop_img,black_bishop_img)
        self.value=3
    def copy(self):
        new_piece = Bishop(self.piece_color,self.position)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        return new_piece


class Rook(Piece):
    def __init__(self, piece_color, position):
        super().__init__(ROOK, piece_color, position,white_rook_img,black_rook_img)
        self.value = 5
    def copy(self):
        new_piece = Rook(self.piece_color,self.position)
        new_piece.begin_position = self.begin_position
        new_piece.value = self.value
        return new_piece


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
        self.white_moves = []
        self.black_moves = []
        self.white_check = False
        self.black_check = False
        self.black_king_pos = (0,4)
        self.white_king_pos = (7,4)
        self.white_check_pieces = []
        self.black_check_pieces = []
        self.white_attack_pieces = []
        self.black_attack_pieces = []
        self.checkMate = False
        self.boardValue = 0

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
        if(piece.piece_type==KING):
            if piece.small_castle == True and abs(position[1]-piece.position[1]) ==2:
                rook = self.check_case(position=(position[0],7))
                rook.move((position[0],5))
            if piece.big_castle == True and abs(position[1]-piece.position[1]) ==2:
                rook = self.check_case(position=(position[0],0))
                rook.move((position[0],3))
            if(piece.piece_color==BLACK_TYPE):
                self.black_king_pos = position
            else:
                self.white_king_pos = position
        
        piece.move(position)

    def pawn_move(self,pawn : Pawn):
        pawn.canBeTakeEnPassant = False
        pawn.available_move = []
        if(pawn.piece_color == BLACK_TYPE and pawn.position[0]==7):
            self.black_pieces.append(Queen(BLACK_TYPE,pawn.position))
            self.black_pieces.remove(pawn)
            return

        if(pawn.piece_color == WHITE_TYPE and pawn.position[0]==0):
            self.white_pieces.append(Queen(WHITE_TYPE,pawn.position))
            self.white_pieces.remove(pawn)
            return

        direction = -1
        if(pawn.piece_color == BLACK_TYPE):
            direction = 1
        if(self.check_case((pawn.position[0]+(1*direction),pawn.position[1]))==None):
            pawn.available_move.append((pawn.position[0]+(1*direction),pawn.position[1]))
            if(pawn.begin_position==True and self.check_case((pawn.position[0]+(2*direction),pawn.position[1]))==None):
                pawn.available_move.append((pawn.position[0]+(2*direction),pawn.position[1]))
        # Attack movement
        left_check = self.check_case((pawn.position[0]+(1*direction),pawn.position[1]-1))
        if(left_check!=None):
            if(left_check.piece_color != pawn.piece_color): 
                pawn.available_move.append((pawn.position[0]+(1*direction),pawn.position[1]-1))
                if(left_check.piece_type==KING):
                    if(pawn.piece_color==WHITE_TYPE):
                        self.white_check_pieces.append(pawn)
                    else:
                        self.black_check_pieces.append(pawn)
            else:
                left_check.protected = True
        right_check = self.check_case((pawn.position[0]+(1*direction),pawn.position[1]+1))
        if(right_check!=None):
            if(right_check.piece_color != pawn.piece_color ):
                pawn.available_move.append((pawn.position[0]+(1*direction),pawn.position[1]+1))
                if(right_check.piece_type==KING):
                    if(pawn.piece_color==WHITE_TYPE):
                        self.white_check_pieces.append(pawn)
                    else:
                        self.black_check_pieces.append(pawn)
            else:
                right_check.protected = True
        pawn.attack_move.append((pawn.position[0]+(1*direction),pawn.position[1]+1))
        pawn.attack_move.append((pawn.position[0]+(1*direction),pawn.position[1]-1))

    
    def rook_move(self,rook : Piece):
        rook.available_move = []
        rook.check_move = []
        x = rook.position[0] -1
        y = rook.position[1]
        nb_ennemy_piece = 0
        add_move = True
        see_king = False
        temp_move = []
        while x >= 0 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : rook.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != rook.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : rook.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            rook.check_move=temp_move.copy()
                            if(rook.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(rook)
                            else:
                                self.black_check_pieces.append(rook)
                        
                else :
                    check_case.protected = True
                    nb_ennemy_piece = nb_ennemy_piece +1    
                add_move =False
            
                
            x= x-1
        if see_king and nb_ennemy_piece <3: 
            rook.attack_move=temp_move.copy()
            if(rook.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(rook)
            else:
                self.black_attack_pieces.append(rook)
        add_move = True
        see_king = False
        nb_ennemy_piece = 0
        temp_move = []
        x = rook.position[0] +1
        y = rook.position[1]
        
        while x < 8 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : rook.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != rook.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : rook.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            rook.check_move=temp_move.copy()
                            if(rook.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(rook)
                            else:
                                self.black_check_pieces.append(rook)
                else :
                    check_case.protected = True   
                    nb_ennemy_piece = nb_ennemy_piece +1        
                add_move =False
            
                
            x= x+1
        if see_king and nb_ennemy_piece <3: 
            rook.attack_move=temp_move.copy()
            if(rook.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(rook)
            else:
                self.black_attack_pieces.append(rook)
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = rook.position[0] 
        y = rook.position[1] -1
        
        while y >= 0 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : rook.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != rook.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : rook.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            rook.check_move=temp_move.copy()
                            if(rook.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(rook)
                            else:
                                self.black_check_pieces.append(rook)
                else :
                    check_case.protected = True     
                    nb_ennemy_piece = nb_ennemy_piece +1     
                add_move =False
            
                
            y= y-1
        if see_king and nb_ennemy_piece <3: 
            rook.attack_move=temp_move.copy()
            if(rook.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(rook)
            else:
                self.black_attack_pieces.append(rook)
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = rook.position[0] 
        y = rook.position[1]+1
        
        while y < 8 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : rook.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != rook.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : rook.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            rook.check_move=temp_move.copy()
                            if(rook.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(rook)
                            else:
                                self.black_check_pieces.append(rook)   
                else :
                    check_case.protected = True      
                    nb_ennemy_piece = nb_ennemy_piece +1
                add_move =False
            
                
            y= y+1    
        if see_king and nb_ennemy_piece <3: 
            rook.attack_move=temp_move.copy()
            if(rook.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(rook)
            else:
                self.black_attack_pieces.append(rook)
        

    def bishop_move(self, bishop : Piece):
        bishop.available_move = []
        bishop.check_move= []
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = bishop.position[0] -1
        y = bishop.position[1] -1
        while x>=0 and y >=0 :
            
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : bishop.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != bishop.piece_color):
                    temp_move.append((x,y))
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : bishop.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            bishop.check_move=temp_move.copy()
                            if(bishop.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(bishop)
                            else:
                                self.black_check_pieces.append(bishop)
                else :
                    check_case.protected = True    
                    nb_ennemy_piece = nb_ennemy_piece +1
                add_move =False
            x =x-1
            y =y-1
        if see_king and nb_ennemy_piece <3: 
            bishop.attack_move=temp_move.copy() 
            if(bishop.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(bishop)
            else:
                self.black_attack_pieces.append(bishop)
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = bishop.position[0] + 1
        y = bishop.position[1] -1
        while x<8 and y >=0 :
            
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : bishop.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != bishop.piece_color):
                    temp_move.append((x,y))
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : bishop.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            bishop.check_move=temp_move.copy()
                            if(bishop.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(bishop)
                            else:
                                self.black_check_pieces.append(bishop)
                else :
                    check_case.protected = True   
                    nb_ennemy_piece = nb_ennemy_piece +1
                add_move =False
            x =x+1
            y =y-1

        if see_king and nb_ennemy_piece <3: 
            bishop.attack_move=temp_move.copy() 
            if(bishop.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(bishop)
            else:
                self.black_attack_pieces.append(bishop)
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = bishop.position[0] -1
        y = bishop.position[1] +1
        while x>=0 and y <8 :
            
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : bishop.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != bishop.piece_color):
                    temp_move.append((x,y))
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : bishop.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            bishop.check_move=temp_move.copy()
                            if(bishop.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(bishop)
                            else:
                                self.black_check_pieces.append(bishop)
                else :
                    check_case.protected = True         
                    nb_ennemy_piece = nb_ennemy_piece +1 
                add_move =False
            x =x-1
            y =y+1
        if see_king and nb_ennemy_piece <3: 
            bishop.attack_move=temp_move.copy() 
            if(bishop.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(bishop)
            else:
                self.black_attack_pieces.append(bishop)
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = bishop.position[0] +1
        y = bishop.position[1] +1
        while x<8 and y <8 :
            
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : bishop.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != bishop.piece_color):
                    temp_move.append((x,y))
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : bishop.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            bishop.check_move=temp_move.copy()
                            if(bishop.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(bishop)
                            else:
                                self.black_check_pieces.append(bishop)
                else :
                    check_case.protected = True      
                    nb_ennemy_piece = nb_ennemy_piece +1    
                add_move =False
            x =x+1
            y =y+1
        if see_king and nb_ennemy_piece <3: 
            bishop.attack_move=temp_move.copy() 
            if(bishop.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(bishop)
            else:
                self.black_attack_pieces.append(bishop)


    def knight_move(self, knight : Piece):
        knight.available_move = []
        for pos in [(2,-1),(2,1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]:
            x = knight.position[0] +pos[0]
            y = knight.position[1] + pos[1]
            if(x <8 and x >=0 and y <8 and y >=0):
                check_case = self.check_case((x,y))
                if(check_case==None):
                    knight.available_move.append((x,y))
                else :
                    if(check_case.piece_color != knight.piece_color):
                        knight.available_move.append((x,y))
                        if(check_case.piece_type==KING):
                            if(knight.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(knight)
                            else:
                                self.black_check_pieces.append(knight)
                    else:
                        check_case.protected = True
                        

    def queen_move(self, queen : Piece):
        queen.available_move = [] 
        queen.check_move=[]
        self.bishop_move(queen)
        x = queen.position[0] -1
        y = queen.position[1]
        nb_ennemy_piece = 0
        add_move = True
        see_king = False
        temp_move = []
        while x >= 0 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : queen.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != queen.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : queen.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            queen.check_move=temp_move.copy()
                            if(queen.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(queen)
                            else:
                                self.black_check_pieces.append(queen)
                else :
                    check_case.protected = True          
                    nb_ennemy_piece = nb_ennemy_piece +1
                add_move =False
            
                
            x= x-1
        if see_king and nb_ennemy_piece<3: 
            queen.attack_move=temp_move.copy()
            if(queen.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(queen)
            else:
                self.black_attack_pieces.append(queen)
        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = queen.position[0] +1
        y = queen.position[1]
        
        while x < 8 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : queen.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != queen.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : queen.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            queen.check_move=temp_move.copy()
                            if(queen.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(queen)
                            else:
                                self.black_check_pieces.append(queen)
                else :
                    check_case.protected = True   
                    nb_ennemy_piece = nb_ennemy_piece +1      
                add_move =False
            
                
            x= x+1
        
        if see_king and nb_ennemy_piece<3: 
            queen.attack_move=temp_move.copy()
            if(queen.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(queen)
            else:
                self.black_attack_pieces.append(queen)

        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = queen.position[0] 
        y = queen.position[1] -1
        
        while y >= 0 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : queen.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != queen.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : queen.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            queen.check_move=temp_move.copy()
                            if(queen.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(queen)
                            else:
                                self.black_check_pieces.append(queen)
                else :
                    check_case.protected = True 
                    nb_ennemy_piece = nb_ennemy_piece +1        
                add_move =False
            
                
            y= y-1
        if see_king and nb_ennemy_piece<3: 
            queen.attack_move=temp_move.copy()
            if(queen.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(queen)
            else:
                self.black_attack_pieces.append(queen)

        add_move = True
        see_king = False
        temp_move = []
        nb_ennemy_piece = 0
        x = queen.position[0] 
        y = queen.position[1]+1
        
        while y < 8 :
            check_case = self.check_case((x,y))
            if(check_case==None):
                if add_move : queen.available_move.append((x,y))
                temp_move.append((x,y))
            else :
                if(check_case.piece_color != queen.piece_color):
                    nb_ennemy_piece = nb_ennemy_piece +1
                    if add_move : queen.available_move.append((x,y))
                    if(check_case.piece_type==KING):
                        see_king =True
                        if(add_move):
                            queen.check_move=temp_move.copy()
                            if(queen.piece_color==WHITE_TYPE):
                                self.white_check_pieces.append(queen)
                            else:
                                self.black_check_pieces.append(queen)
                else :
                    check_case.protected = True    
                    nb_ennemy_piece = nb_ennemy_piece +1      
                add_move =False
            
                
            y= y+1    
        if see_king and nb_ennemy_piece<3: 
            queen.attack_move=temp_move.copy()
            if(queen.piece_color==WHITE_TYPE):
                self.white_attack_pieces.append(queen)
            else:
                self.black_attack_pieces.append(queen)

    def king_move(self, king : King):
        king.available_move = []
        king.small_castle =False
        king.big_castle = False
        for pos in [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]:
            x = king.position[0] +pos[0]
            y = king.position[1] + pos[1]
            newPos = (x,y)
            valid = False
            if(x <8 and x >=0 and y <8 and y >=0):
                valid = True
            if (king.piece_color==BLACK_TYPE):
                if newPos in self.white_moves :
                    valid =False
            if (king.piece_color==WHITE_TYPE):
                if newPos in self.black_moves :
                    valid =False
            if valid :
                check_case = self.check_case((x,y))
                if(check_case==None):
                    king.available_move.append((x,y))
                else :
                    if(check_case.piece_color != king.piece_color and check_case.protected==False):
                        king.available_move.append((x,y))
        if king.piece_color == BLACK_TYPE and king.begin_position==True:
            # small castle
            big_rook = self.check_case((0,0))
            if big_rook !=None and big_rook.piece_type==ROOK and big_rook.begin_position ==True:
                if self.check_case((0,1)) == None and  (0,1) not in self.white_moves and self.check_case((0,2)) == None and  (0,2) not in self.white_moves and self.check_case((0,3)) == None and  (0,3) not in self.white_moves :
                    king.available_move.append((0,2))
                    king.big_castle = True
            small_rook = self.check_case((0,7))
            if small_rook !=None and small_rook.piece_type==ROOK and small_rook.begin_position ==True:
                if self.check_case((0,5)) == None and  (0,5) not in self.white_moves and self.check_case((0,6)) == None and  (0,6) not in self.white_moves:
                    king.available_move.append((0,6))
                    king.small_castle = True
        if king.piece_color == WHITE_TYPE and king.begin_position==True:
            # small castle
            big_rook = self.check_case((7,0))
            if big_rook !=None and big_rook.piece_type==ROOK and big_rook.begin_position ==True:
                if self.check_case((7,1)) == None and  (7,1) not in self.black_moves and self.check_case((7,2)) == None and  (7,2) not in self.black_moves and self.check_case((7,3)) == None and  (7,3) not in self.black_moves :
                    king.available_move.append((7,2))
                    king.big_castle = True
            small_rook = self.check_case((7,7))
            if small_rook !=None and small_rook.piece_type==ROOK and small_rook.begin_position ==True:
                if self.check_case((7,5)) == None and  (7,5) not in self.black_moves and self.check_case((7,6)) == None and  (7,6) not in self.black_moves:
                    king.available_move.append((7,6))
                    king.small_castle = True

    def calc_black_board_move(self):
        self.black_moves = []
        self.black_check_pieces = []
        self.black_attack_pieces = []
        for piece in self.black_pieces:
            match piece.piece_type:
                case 'pawn':
                    self.pawn_move(piece)
                case 'rook':
                    self.rook_move(piece)
                case 'bishop':
                    self.bishop_move(piece)
                case 'knight':
                    self.knight_move(piece)
                case 'queen':
                    self.queen_move(piece)
                case 'king' :
                    self.king_move(piece)
            if piece.piece_type != PAWN:
                for move in piece.available_move:
                    self.black_moves.append(move)
            else :
                for move in piece.attack_move:
                    self.black_moves.append(move)


    def calc_white_board_move(self):
        self.white_moves = []
        self.white_check_pieces=[]
        self.white_attack_pieces=[]
        for piece in self.white_pieces:
            match piece.piece_type:
                case 'pawn':
                    self.pawn_move(piece)
                case 'rook':
                    self.rook_move(piece)
                case 'bishop':
                    self.bishop_move(piece)
                case 'knight':
                    self.knight_move(piece)
                case 'queen':
                    self.queen_move(piece)
                case 'king' :
                    self.king_move(piece)
            for move in piece.available_move:
                self.white_moves.append(move)

    def reinit_protection_piece(self):
        for piece in self.black_pieces:
            piece.protected = False
            
        for piece in self.white_pieces:
            piece.protected = False

    def verify_white_check(self):
        res = False    
        if len(self.black_check_pieces) > 1:
            res = True    
            for piece in self.white_pieces:
                if(piece.piece_type!=KING):
                    piece.available_move = []
        elif len(self.black_check_pieces)==1 :
            res = True    
            check_piece = self.black_check_pieces[0]
            
            self.white_moves = []
            for piece in self.white_pieces:
                temp = []
                if(piece.piece_type!=KING):
                    for move in piece.available_move:
                        if move in check_piece.check_move or move == check_piece.position: 
                            temp.append(move)
                    piece.available_move =temp
                else : 
                    for move in piece.available_move:
                        # print(check_piece.protected)
                        if (move == check_piece.position and check_piece.protected==False):
                            temp.append(move)
                        elif move != check_piece.position and move not in check_piece.available_move:
                            temp.append(move)
                    piece.available_move =temp
        return res
    
    def verify_black_check(self):   
        res = False
        if len(self.white_check_pieces) > 1:
            res: True
            for piece in self.black_pieces:
                if(piece.piece_type!=KING):
                    piece.available_move = []
        elif len(self.white_check_pieces)==1 :
            res: True
            check_piece = self.white_check_pieces[0]
            for piece in self.black_pieces:
                temp = []
                if(piece.piece_type!=KING):
                    for move in piece.available_move:
                        if move in check_piece.check_move or move == check_piece.position: 
                            temp.append(move)
                    piece.available_move =temp
                else : 
                    for move in piece.available_move:
                        # print(check_piece.protected)
                        if (move == check_piece.position and check_piece.protected==False):
                            temp.append(move)
                        elif move != check_piece.position and move not in check_piece.available_move:
                            temp.append(move)
                    piece.available_move =temp
        return res
   
    def verify_white_illegal_move(self):
        if len(self.black_attack_pieces) >0 :
            for check_piece in self.black_attack_pieces : 
                for piece in self.white_pieces:
                    temp = []
                    if(piece.piece_type!=KING and piece.position in check_piece.attack_move):
                        for move in piece.available_move:
                            if move in check_piece.attack_move or move == check_piece.position: 
                                temp.append(move)
                        piece.available_move =temp
                    elif piece.piece_type==KING: 
                        for move in piece.available_move:
                            # print(check_piece.protected)
                            if (move == check_piece.position and check_piece.protected==False):
                                temp.append(move)
                            elif move != check_piece.position and move not in check_piece.attack_move:
                                temp.append(move)
                        piece.available_move =temp

    def verify_black_illegal_move(self):
        if len(self.white_attack_pieces) >0 :
            for check_piece in self.white_attack_pieces : 
                for piece in self.black_pieces:
                    temp = []
                    if(piece.piece_type!=KING and piece.position in check_piece.attack_move):
                        for move in piece.available_move:
                            if move in check_piece.attack_move or move == check_piece.position: 
                                temp.append(move)
                        piece.available_move =temp
                    else : 
                        for move in piece.available_move:
                            # print(check_piece.protected)
                            if (move == check_piece.position and check_piece.protected==False):
                                temp.append(move)
                            elif move != check_piece.position and move not in check_piece.attack_move:
                                temp.append(move)
                        piece.available_move =temp

    def calc_board_value(self):
        self.white_moves=[]
        self.black_moves=[]
        self.boardValue = 0
        for piece in self.white_pieces:
            for move in piece.available_move:
                self.white_moves.append(move)
                self.boardValue = self.boardValue+ piece.value

        for piece in self.black_pieces:
            for move in piece.available_move:
                self.black_moves.append(move)
                self.boardValue = self.boardValue- piece.value
        
        return self.boardValue
    def verify_check_mate(self,last_move_color):
        if(last_move_color==BLACK_TYPE and len(self.white_moves)==0):
            if len(self.black_check_pieces)>0:
                print('CHECKMATE BLACK')
                self.checkMate =True
            else:
                print('PAT')
                self.checkMate =True
        if(last_move_color==WHITE_TYPE and len(self.black_moves)==0):    
            if len(self.white_check_pieces)>0:
                print('CHECKMATE BLACK')
                self.checkMate =True
            else:
                print('PAT')
                self.checkMate =True


    def calc_board_move(self,last_move_color):
        self.reinit_protection_piece()
        if(last_move_color==BLACK_TYPE):    
            self.calc_black_board_move()
            if not self.verify_black_check(): self.verify_black_illegal_move()
            self.calc_white_board_move()
            if not self.verify_white_check():  self.verify_white_illegal_move()
        else:
            self.calc_white_board_move()
            if not self.verify_white_check():  self.verify_white_illegal_move()
            self.calc_black_board_move()
            if not self.verify_black_check(): self.verify_black_illegal_move()
        self.calc_board_value()
        self.verify_check_mate(last_move_color)
        return self.boardValue
    
    def copyBoard(self):
        board = Board()
        board.white_pieces = []
        board.black_pieces = []
        for piece in self.black_pieces:
            board.black_pieces.append(piece.copy())
        for piece in self.white_pieces:
            board.white_pieces.append(piece.copy())
        # board.calc_board_move(self.currentColor)
        return board

    def estimate_move(self,colorPlayer):
        listPieceMove=[]
        listValue = []
        copyBoard = self.copyBoard()
        copyBoard.calc_board_move(WHITE_TYPE)
        if(colorPlayer == WHITE_TYPE):
            currentPieceList = self.white_pieces
        else : 
            currentPieceList = self.black_pieces
        for piece in currentPieceList:
            original_position = piece.position
            for move in piece.available_move:
                copyBoard = self.copyBoard()
                copyPiece = copyBoard.check_case(original_position)
                copyBoard.move_piece(copyPiece,move)
                copyBoard.calc_board_move(colorPlayer)
                currentValue = copyBoard.calc_board_value()
                listValue.append(currentValue)
                listPieceMove.append((piece,move))
                copyPiece.move(original_position)      
        search = max(listValue) if colorPlayer == WHITE_TYPE else min(listValue)
        bestPiece = listPieceMove[listValue.index(search)][0]
        bestMove = listPieceMove[listValue.index(search)][1]
        copyBoard = self.copyBoard()
        copyBoard.move_piece(bestPiece,bestMove)
        copyBoard.move_piece(copyPiece,move)
        copyBoard.calc_board_move(colorPlayer)
        return bestPiece, bestMove, search, copyBoard

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

    def copyBoard(self):
        board = Board()
        board.white_pieces = []
        board.black_pieces = []
        for piece in self.board.black_pieces:
            board.black_pieces.append(piece.copy())
        for piece in self.board.white_pieces:
            board.white_pieces.append(piece.copy())
        # board.calc_board_move(self.currentColor)
        return board
    
    def estimate_move(self,colorPlayer):
        return self.board.estimate_move(colorPlayer)


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
            if(self.currentPlayer.isAi == False):    
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
                            self.estimate_move(self.selectedPieces)
            else:
                self.currentPlayer.play_move()
                time.sleep(0.1)
            self.display_game_screen()
            self.gameRunning = not self.board.checkMate
            pygame.display.update()
            # FramePerSec.tick(FPS)
        # SCREEN_HEIGHT = SCREEN_HEIGHT +100
        DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT+100,SCREEN_WIDTH))
        DISPLAYSURF.fill(WHITE_COLOR)
        while True:
            for event in pygame.event.get():              
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
            self.display_game_screen()
            titre = font.render("CheckMate", True, BLACK_COLOR)
            DISPLAYSURF.blit(titre, (SCREEN_WIDTH//2 - titre.get_width()//2, (SCREEN_HEIGHT+100)//4))
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
    def __init__(self, game, colorPlayer):
        super().__init__(game, colorPlayer)
    
    def play_move(self):
        bestPiece, bestMove, value = self.game.estimate_move(self.colorPlayer)
        self.choose_piece(bestPiece)
        self.choose_move(bestMove)

