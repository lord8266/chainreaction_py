
# doesnt do anything as of now just sets up the boxes and connecting surrounding

from board import board


# im importing the class itself
# so i dont have to say board.board .

#------------------------------------------------------------------------------------------------

a=board(5,5)
a.make_boxes()

print("start\n")

# this is not how things will happen in the real game
# just for demonstration
a.print_holding()
print()
a.add_atom(0)
a.add_atom(0) # the box will explode here

a.update()
a.update() # im calling update again and again
# this will be in a loop and this update will be called again and again there
# if the game is running at 60fps
# then update is called 60 times a second
a.print_holding()
print()

a.add_atom(1)
a.add_atom(5)
a.add_atom(0)
a.update() # need to call only once here since so animations

a.print_holding()
print()

a.add_atom(5)

for i in range(5):
    a.update()
a.print_holding()
