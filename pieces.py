from chess import *
from assets import *
from constants import *

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

