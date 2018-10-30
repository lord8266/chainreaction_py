class animation:
    multiplier = 1 # this is for the pygame part
    # i will explain this later
    
    def __init__(self,box_from,box_to,speed):
        animation.main_board = box_from.main_board # get the main board object
        self.direction = animation.create_vector(box_from,box_to)
        # note that the vector will always be a unit vector since any surrounding box
        # is only one unit away from the source box

        self.speed =speed # speed at which the ball will move

        self.curr_loc = {"x":box_from.col*animation.multiplier,"y":box_from.row*animation.multiplier} # start from that location
        self.dest = {"x":box_to.col*animation.multiplier,"y":box_to.row*animation.multiplier}
        # row is the y component col is the x component
        # this is similar to the fourth quadrant but only y value increases as you go down
        # like 0,0 at origin 0,5 at the bottom of fourth quad  5,0 at the end of x axis (this doesnt change)

        self.box_from = box_from
        self.box_to = box_to

    def create_vector(b1,b2):
        temp_vec =  {'x':(b2.col-b1.col),'y':(b2.row-b1.row)} # create a direction vector
        return temp_vec

    def update(self):
        self.curr_loc['x']+=self.direction['x']*self.speed # multiply by speed
        # displaces position by velocity vector
        # since speed is 1 it is the same as the direction vector
        self.curr_loc['y']+=self.direction['y']*self.speed # move the atom along the position

        self.check_completion() # if completed add this animation to the remove cycle

    def check_completion(self):
        # if dot product of current pos along direction is greater than that of destination along direction
        # then the atom has reached destination

        if animation.dot(self.direction,self.curr_loc)>=animation.dot(self.direction,self.curr_loc):
            self.completion_event()

    def completion_event(self):
        # will add more here later
        animation.main_board.remove_animation(self) # remove this animation from board
        self.box_to.events.append(self) # add this to box_to events

    def dot(vec1,vec2):
        temp = vec1['x']*vec2['x'] + vec1['y']*vec2['y'] # dot product
        # dot product of curr_pos along direction
        # basically this eliminates need for if conditions to check direction like i did in the c++ version
        return temp
