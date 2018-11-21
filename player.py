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
        self.name_surface = text_render.create_text(self.name,self.color)
        self.holding=0
        self.pos = (main_board.total_box_width+main_board.multiplier/4,main_board.multiplier*(i+0.33))
        self.update_holding()
        self.holding_pos=(self.pos[0]+self.name_surface.get_width()+10,self.pos[1])

    def change_color(surface,color):
        w,h = surface.get_width(),surface.get_height()

        temp_surf = surface.copy()
        pixels_array=pygame.surfarray.pixels3d(temp_surf)
        for rows in pixels_array:
            for col in rows:
                col[0] =color[0]
                col[1]=color[1]
                col[2]=color[2]

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
