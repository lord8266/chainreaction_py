
# doesnt do anything as of now just sets up the boxes and connecting surrounding

from board import board
import pygame

<<<<<<< HEAD
data = {"rows":3,"cols":5,"multiplier":80}
=======
data = {"rows":6,"cols":6,"multiplier":100,"speed":10}
# no of rows ,cols and the multiplier says the size of each box
# each box is a square
>>>>>>> master

pygame.init()
w1 = pygame.display.set_mode((data["cols"]*data["multiplier"],data["rows"]*data["multiplier"]))
clock = pygame.time.Clock()

game = board(data)

print("start\n")

running =True

def event_handle(pos):
    id = pos[0]//data["multiplier"] +data["cols"]*(pos[1]//data["multiplier"])
    game.add_atom(id)
    game.print_holding()

<<<<<<< HEAD
=======

>>>>>>> master
while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            event_handle(e.pos)
    game.run()
<<<<<<< HEAD
=======
    clock.tick(60)
>>>>>>> master

pygame.quit()
