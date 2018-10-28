
# doesnt do anything as of now just sets up the boxes and connecting surrounding

class board:
    #construct with rows ,cols and initialize box_list to empty list
    def __init__(self,rows,columns):
        self.rows= rows
        self.cols =columns
        board.box_list =[]

    def make_boxes(self): 

        for r in range(0,self.rows):
            for c in range(0,self.cols):
                #for each box first contruct box with board object reference
                temp = box(self) # self is the board instance
                # look at setup in box
                temp.setup(r,c)
                board.box_list.append(temp)


      # when making each box the rest of the boxes arent always available
      # like surrounding for 1,1 would include 2,1 which hasnt been made
      # so first store the surrounding data in tuples and then convert them into boxes
      # look at the setup function
        temp_f = lambda t : board.box_list[t[0]*self.rows+t[1]]
     # returns the postion of (row,col)th box in box_list and replaces the tuple with the box reference in surrounding

        for b in board.box_list:
            temp = map(temp_f,b.surrounding)
            b.surrounding = list(temp)

#------------------------------------------------------------------------------------------------

class box:
    def __init__(self,main_board):
        box.main_board = main_board
        self.surrounding = []
        self.holding=0

    def setup(self,row,col):
        # initialize current box row and col
        self.row = row
        self.col = col
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

#------------------------------------------------------------------------------------------------

a=board(5,5)
a.make_boxes()
