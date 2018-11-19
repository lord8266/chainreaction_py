
# the board class ----------------------------------------

from animation import animation
import pygame
import random
class box:
    def __init__(self,main_board):
        box.main_board = main_board
        self.surrounding = []
        self.events = []
        self.holding=0
        self.angle=0
        self.owner=None
        self.rotate_dir= random.choice([1,-1])
        self.speed =random.randrange(*self.main_board.rotation_speed)
    def setup(self,row,col):
        # initialize current box row and col
        self.row = row
        self.col = col
        self.pos = [col*box.main_board.multiplier,row*box.main_board.multiplier]
        # conditions for determing the box surrounding locations
        # just some hardcoded stuff
        if col==0 and row==0:
            # surrounding box -> below ,front
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col+1))

        elif col==box.main_board.cols-1 and row==0:
            # surrounding box -> below ,behind
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col-1))

        elif col==0 and row==box.main_board.rows-1:
            # surrounding box ->  front ,above
            self.surrounding.append((row,col+1))
            self.surrounding.append((row-1,col))

        elif col==box.main_board.cols-1 and row==box.main_board.rows-1:
            # surrounding box -> above , behind
            self.surrounding.append((row-1,col))
            self.surrounding.append((row,col-1))

        elif col==0:
            # surrounding box -> above , below ,front
            self.surrounding.append((row-1,col))
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col+1))

        elif row==0:
            # surrounding box ->  front, below ,behind
            self.surrounding.append((row,col+1))
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col-1))

        elif row==box.main_board.rows-1:
            # surrounding box -> front,above,behind
            self.surrounding.append((row,col+1))
            self.surrounding.append((row-1,col))
            self.surrounding.append((row,col-1))

        elif col==box.main_board.cols-1:
            # surrounding box -> behind , above, below
            self.surrounding.append((row,col-1))
            self.surrounding.append((row-1,col))
            self.surrounding.append((row+1,col))

        else:
            # surrounding box -> front ,below, above, behind
            self.surrounding.append((row,col+1))
            self.surrounding.append((row+1,col))
            self.surrounding.append((row-1,col))
            self.surrounding.append((row,col-1))

        self.max=len(self.surrounding)

    def update(self):
        ret = False
        if self.events:
            ret =True
            temp =self.events[0] # check only first event in one cycle
            #temp.add(self) # add this box to owners list
            #self.owner = temp.box_from.owner # take the owner
            self.color = temp.box_from.color
            if self.owner!=None:
                self.owner.rem_box(self)
            #self.owner.add_box(self) # add this box to owner
             # add the atom in the box
            temp.owner.add_box(self)
            self.add_atom()
            self.main_board.animation_owners.remove(temp.owner)#remove the animation from list
            self.events.pop(0) # pop the first event which came
            # if there are more then handle them in the next cycle
            # not required but i want to do one step at a time
        self.angle+=self.speed*self.rotate_dir
        if abs(self.angle)==360:
            self.angle=0
        return ret

    def render(self):
        if(self.holding!=0):
            main_img = self.owner.img[self.holding-1]
            img = pygame.transform.rotate(main_img,self.angle)
            rect1,rect2 =img.get_rect(),main_img.get_rect()
            w1=box.main_board.w1
            loc = self.pos.copy()
            loc[0]-=(rect1.width-rect2.width)/2
            loc[1]-=(rect1.height-rect2.height)/2
            w1.blit(img,loc)

    def add_atom(self):
        self.holding+=1 # increment holding
        # if holding is more than max explode
        if self.holding==self.max:

            self.explode()

    def explode(self):
         #reset box
        for b in self.surrounding:
            box.main_board.animations.add(animation(self,b,self.main_board.speed)) # here need to create animation
        self.owner.rem_box(self)
        self.color = None # just to complete
        self.holding =0

        # color of the box is reset just syas it has no color
