
# the board class ----------------------------------------
from box import box
from animation import animation

class board:
    #construct with rows ,cols and initialize box_list to empty list
    def __init__(self,rows,columns):
        self.rows= rows
        self.cols =columns
        board.box_list =[]
        board.animations = set() # it is a set
        board.remove_cycle=set()
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
        temp_f = lambda t : board.box_list[t[0]*self.cols+t[1]]
     # returns the postion of (row,col)th box in box_list and replaces the tuple with the box reference in surrounding

        for b in board.box_list:
            temp = map(temp_f,b.surrounding)
            b.surrounding = list(temp)


    def print_max(self): # prints the maximum allowable atoms in each box
        for r in range(0,self.rows):
            for c in range(0,self.cols):
                print(board.box_list[r*self.cols+c].max," " ,end="")

            print()

    def print_surr(self): # prints the surrounding elements of all boxes
        for b in board.box_list:
            print("( %d %d )"%(b.row,b.col),"surr",[(temp.row,temp.col) for temp in b.surrounding])
            # creates a list with tuples for row,col of each box

    def print_holding(self): # prints the current holding of all boxes
        for r in range(0,self.rows):
            for c in range(0,self.cols):
                print(board.box_list[r*self.cols+c].holding,end=" ")

            print()

    def update(self):
        if board.remove_cycle: # if there are animations to be removed
        # then remove them
            self.remove_all()

        for b in self.box_list: # for all the boxes
            b.update() # update events in all boxes

        for a in self.animations:# for each animation in animations
            a.update() # update animations

        self.running = bool(self.animations) # this variable will be needed for pygame
        # if there are no animations running then the game state can be checked
        # more on this later


    def remove_animation(self,anim):
        board.remove_cycle.add(anim)

    def remove_all(self):
        # for each animation in remove_cycle remove that animation from
        # the animations list
        # why im doing this is because i cant remove an animation when im iterating through the animation list
        # itself and so i need to store them for the next cycle

        for a in board.remove_cycle:
            self.animations.discard(a) # remove animation from animations

            print("discard: " ,a) # for debug only not required by the game
            print("discarded data:" , "from pos",a.box_from.pos,"to pos",a.box_to.pos,"\n" )

        board.remove_cycle.clear()
        #clear the remove_cycle as all to be removed animations have been removed

    def add_atom(self,index):
        board.box_list[index].add_atom()
        # as of now im calling directly but then this will
        # be a much more complex function later
