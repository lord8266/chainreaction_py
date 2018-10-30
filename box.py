
# the board class ----------------------------------------

from animation import animation
 
class box:
    def __init__(self,main_board):
        box.main_board = main_board
        self.surrounding = []
        self.events = []
        self.holding=0

    def setup(self,row,col):
        # initialize current box row and col
        self.row = row
        self.col = col
        self.pos = row,col
        # conditions for determing the box surrounding locations
        # just some hardcoded stuff
        if col==0 and row==0:
            # surrounding box -> below ,front
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col+1))
            self.max=2

        elif col==box.main_board.cols-1 and row==0:
            # surrounding box -> below ,behind
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col-1))
            self.max=2

        elif col==0 and row==box.main_board.rows-1:
            # surrounding box ->  front ,above
            self.surrounding.append((row,col+1))
            self.surrounding.append((row-1,col))
            self.max=2

        elif col==box.main_board.cols-1 and row==box.main_board.rows-1:
            # surrounding box -> above , behind
            self.surrounding.append((row-1,col))
            self.surrounding.append((row,col-1))
            self.max=2

        elif col==0:
            # surrounding box -> above , below ,front
            self.surrounding.append((row-1,col))
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col+1))
            self.max=3

        elif row==0:
            # surrounding box ->  front, below ,behind
            self.surrounding.append((row,col+1))
            self.surrounding.append((row+1,col))
            self.surrounding.append((row,col-1))
            self.max=3

        elif row==box.main_board.rows-1:
            # surrounding box -> front,above,behind
            self.surrounding.append((row,col+1))
            self.surrounding.append((row-1,col))
            self.surrounding.append((row,col-1))
            self.max=3

        elif col==box.main_board.cols-1:
            # surrounding box -> behind , above, below
            self.surrounding.append((row,col-1))
            self.surrounding.append((row-1,col))
            self.surrounding.append((row+1,col))
            self.max=3

        else:
            # surrounding box -> front ,below, above, behind
            self.surrounding.append((row,col+1))
            self.surrounding.append((row+1,col))
            self.surrounding.append((row-1,col))
            self.surrounding.append((row,col-1))
            self.max=4

    def update(self):
        if self.events:
            temp =self.events[0] # check only first event in one cycle
            #temp.add(self) # add this box to owners list
            #self.owner = temp.box_from.owner # take the owner
            self.color = temp.box_from.color
            #self.owner.add_box(self) # add this box to owner
            self.add_atom() # add the atom in the box

            self.events.pop(0) # pop the first event which came
            # if there are more then handle them in the next cycle
            # not required but i want to do one step at a time

    def add_atom(self):
        self.holding+=1 # increment holding
        # if holding is more than max explode
        if self.holding==self.max:
            self.explode()

    def explode(self):
        self.holding =0 #reset box
        #self.owner.remove(self) # remove this box from the owner
        for b in self.surrounding:
            box.main_board.animations.add(animation(self,b,1)) # here need to create animation
        #self.owner =None
        self.color = None # just to complete
        # color of the box is reset just syas it has no color
