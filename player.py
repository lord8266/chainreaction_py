import pygame

class player:
    def __init__(self,main_board,data):
        self.main_board=main_board
        self.name=data["name"]
        self.color=data["color"]
        player.change_color(main_board.img[0],data["color"])
        self.img = [player.change_color(i,self.color) for i in main_board.img]
        self.grid = player.change_color(main_board.grid,data["color"])
        self.boxes =[]
        self.alive=True
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
        self.boxes.append(box)
        box.owner=self
        self.alive =bool(self.boxes)
    def rem_box(self,box):
        self.boxes.remove(box)
        box.owner=None
        self.alive =bool(self.boxes)
