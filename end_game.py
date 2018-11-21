import text_render
import pygame
class end_game:
    def __init__(self,main_board):
        self.main_board=main_board

        self.again = text_render.create_text("Play Again ?",self.main_board.current.color)
        self.again_rect =pygame.Rect(0,0,0,0)
        self.again_rect.x=main_board.total_width*1/10
        self.again_rect.y=main_board.total_height*2/3
        self.again_rect.w=self.again.get_width()
        self.again_rect.h=self.again.get_height()

        self.end = text_render.create_text("End game ",self.main_board.current.color)
        self.end_rect=pygame.Rect(0,0,0,0)
        self.end_rect.x=self.again_rect.w+self.again_rect.x+main_board.total_width*1/3
        self.end_rect.y=main_board.total_height*2/3
        self.end_rect.w=self.end.get_width()
        self.end_rect.h=self.end.get_height()

    def setup(self):
        self.winner = self.main_board.current.name+" "+"Won !"
        self.winner=text_render.create_text(self.winner,self.main_board.current.color)
        self.winner_pos=self.main_board.total_width/2-self.winner.get_width()/2,self.main_board.total_height/6
        self.main_board.end_setup=True

    def update(self,pos):
        
        if self.again_rect.collidepoint(pos):# if user pressed that button
            self.main_board.reset_all()
            self.main_board.state=1

        elif self.end_rect.collidepoint(pos):
            self.main_board.main_running=False


    def render(self):
        self.main_board.w1.blit(self.again,self.again_rect)
        self.main_board.w1.blit(self.winner,self.winner_pos)
        self.main_board.w1.blit(self.end,self.end_rect)
