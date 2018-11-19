import pygame
import text_render
class player:
    def __init__(self,main_board,data,i):
        self.main_board=main_board
        self.name=data["name"]
        self.color=data["color"]
        player.change_color(main_board.img[0],data["color"])
        self.img = [player.change_color(i,self.color) for i in main_board.img]
        self.grid = player.change_color(main_board.grid,data["color"])
        self.boxes =set()
        self.alive=True
        self.name_surface =  text_render.create_text(self.name,self.color)
        self.holding=0
        text_render.create_text(self.name,self.color)
        self.pos = (main_board.total_box_width+main_board.multiplier/4,main_board.multiplier*(i+0.33))
        self.update_holding()
        self.holding_pos=(self.pos[0]+self.holding_text.get_width()*len(self.name)+10,self.pos[1])

    def change_color(surface,color):
        w,h = surface.get_width(),surface.get_height()

        temp_surf = surface.copy()
        for i in range(0,h):
            for j in range(0,w):
                a=temp_surf.get_at((j,i))
                a.r=color[0]
                a.g=color[1]
                a.b=color[2]
                temp_surf.set_at((j,i),a)

        return temp_surf



    def add_box(self,box):
        self.boxes.add(box)
        box.owner=self
        self.alive =True
        self.holding+=box.holding
        self.main_board.update_disp=True
    def rem_box(self,box):
        self.boxes.remove(box)
        box.owner=None
        self.alive =bool(self.boxes)
        self.holding-=box.holding
        self.main_board.update_disp=True
    def render(self):
        self.main_board.w1.blit(self.name_surface,self.pos)
        self.main_board.w1.blit(self.holding_text,self.holding_pos)
    def update_holding(self):
        no=0
        for a in self.boxes:
            no+=a.holding
        self.holding_text = text_render.create_text(str(no),self.color)
