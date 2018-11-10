
# doesnt do anything as of now just sets up the boxes and connecting surrounding

from board import board
import pygame
data = {"rows":6,"cols":6,"multiplier":100,"speed":9}
# no of rows ,cols and the multiplier says the size of each box
# each box is a square

pygame.init()
w1 = pygame.display.set_mode((data["cols"]*data["multiplier"],data["rows"]*data["multiplier"]))
icon=pygame.image.load("assets/atoms_c.ico")
pygame.display.set_icon(icon)
pygame.display.set_caption("chainreaction2d")
data["w1"]=w1
clock = pygame.time.Clock()

game = board(data)

print("start\n")

running =True

def event_handle(pos):
    id = pos[0]//data["multiplier"] +data["cols"]*(pos[1]//data["multiplier"])
    game.add_atom(id)
    game.print_holding()


while running:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running=False
        elif e.type==pygame.MOUSEBUTTONDOWN:
            event_handle(e.pos)
    w1.fill((0,0,0))
    game.run()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
